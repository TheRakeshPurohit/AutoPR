import asyncio
from typing import Coroutine, Any

from autopr.log_config import get_logger
from autopr.models.config.elements import ActionConfig, WorkflowInvocation, IterableWorkflowInvocation, ContextAction
from autopr.models.config.entrypoints import Trigger
from autopr.models.events import EventUnion
from autopr.models.executable import Executable, ContextDict
from autopr.services.platform_service import PlatformService
from autopr.services.publish_service import PublishService
from autopr.services.utils import truncate_strings, format_for_publishing
from autopr.services.workflow_service import WorkflowService


class TriggerService:
    def __init__(
        self,
        triggers: list[Trigger],
        publish_service: PublishService,
        workflow_service: WorkflowService,
    ):
        self.triggers = triggers
        self.publish_service = publish_service
        self.workflow_service = workflow_service

        print("Loaded triggers:")
        for t in self.triggers:
            print(t.json(indent=2))

        self.log = get_logger(service="trigger")

    def _get_name_for_executable(self, executable: Executable) -> str:
        if isinstance(executable, str):
            return executable
        if isinstance(executable, ActionConfig):
            return executable.action
        if isinstance(executable, WorkflowInvocation) or isinstance(executable, IterableWorkflowInvocation):
            return executable.workflow
        if isinstance(executable, ContextAction):
            raise RuntimeError("Meaningless trigger! Whatchu tryina do :)")
        raise ValueError(f"Unknown executable type {executable}")

    def _get_triggers_and_contexts_for_event(self, event: EventUnion) -> list[tuple[Trigger, ContextDict]]:
        # Gather all triggers that match the event
        triggers_and_context: list[tuple[Trigger, ContextDict]] = []
        for trigger in self.triggers:
            context = trigger.get_context_for_event(event)
            if context is None:
                continue
            triggers_and_context.append((trigger, context))
        return triggers_and_context

    async def _get_trigger_coros_for_event(
        self,
        triggers_and_context: list[tuple[Trigger, ContextDict]],
    ) -> list[Coroutine[Any, Any, ContextDict]]:
        # Build coroutines for each trigger
        if not triggers_and_context:
            return []
        if len(triggers_and_context) == 1:
            self.publish_service.title = f"AutoPR: {self._get_name_for_executable(triggers_and_context[0][0].run)}"
            return [
                self.handle_trigger(
                    trigger,
                    context,
                    publish_service=self.publish_service,
                )
                for trigger, context in triggers_and_context
            ]
        trigger_titles = [self._get_name_for_executable(trigger.run) for trigger, context in triggers_and_context]
        self.publish_service.title = f"AutoPR: {', '.join(truncate_strings(trigger_titles))}"
        return [
            self.handle_trigger(
                trigger,
                context,
                publish_service=(await self.publish_service.create_child(title=title)),
            )
            for i, ((trigger, context), title) in enumerate(zip(triggers_and_context, trigger_titles))
        ]

    async def trigger_event(
        self,
        event: EventUnion,
    ):
        triggers_and_contexts = self._get_triggers_and_contexts_for_event(event)
        trigger_coros = await self._get_trigger_coros_for_event(triggers_and_contexts)
        if not trigger_coros:
            print(event)
            self.log.debug(f"No triggers for event")
            return

        results = await asyncio.gather(*trigger_coros)

        exceptions = []
        for r in results:
            if isinstance(r, Exception):
                self.log.error("Error in trigger", exc_info=r)
                exceptions.append(r)

        if exceptions:
            await self.publish_service.finalize(False, exceptions)
        else:
            await self.publish_service.finalize(True)
            # TODO split out multiple triggered workflows into separate PRs,
            #  so that automerge can be evaluated separately for each
            if any(trigger.automerge for trigger, _ in triggers_and_contexts):
                await self.publish_service.merge()

        return results

    async def handle_trigger(
        self,
        trigger: Trigger,
        context: ContextDict,
        publish_service: PublishService,
    ) -> ContextDict:
        await publish_service.publish_code_block(
            heading="📣 Trigger",
            code=format_for_publishing(trigger),
            language="json",
        )
        await publish_service.publish_code_block(
            heading="🎬 Starting context",
            code=format_for_publishing(context),
            language="json",
        )

        executable = trigger.run

        # Add params
        if trigger.parameters:
            context["__params__"] = trigger.parameters

        try:
            context = await self.workflow_service.execute(
                executable,
                context,
                publish_service=publish_service,
            )
        except Exception as e:
            self.log.error("Error while executing", executable=executable, exc_info=e)
            raise

        await publish_service.publish_code_block(
            heading="🏁 Final context",
            code=format_for_publishing(context),
            language="json",
        )

        return context