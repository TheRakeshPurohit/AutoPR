from git.repo import Repo
@patch("requests.get")
    assert outputs == [
        {
            "issue": None,
            "pull_request": PullRequest(
                messages=[Message(body="", author="PireIre")],
                number=10,
                title="Add find-todos action",
                author="PireIre",
                timestamp="2023-08-18T21:20:59Z",
                base_branch="main",
                head_branch="find-todos-action",
                base_commit_sha=git_sha,
            ),
            "pr_diff": "diff --git a/newscript.py b/newscript.py\nnew file mode 100644\nindex 0000000..02d3dc2\n--- /dev/null\n+++ b/newscript.py\n@@ -0,0 +1 @@\n+#TODO do stuff here\n\\ No newline at end of file\n",
            "summary": "Here is a summary of the changes in the pull request for each file:\n\n📄 newscript.py:\n- Added a new file `newscript.py` with mode 100644.\n- Added a line of code `#TODO do stuff here` at line 1.\n\nPlease note that the diff was trimmed for brevity.",
        }
    ]