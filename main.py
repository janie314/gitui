import os
import pathlib
from pyvis.network import Network
import subprocess
import json
import re
import structlog

log = structlog.get_logger()


def git_commits():
    try:
        process = subprocess.Popen(
            [
                "git",
                "log",
                '--pretty=format:{"hash":"%H","author_name":"%an","author_email":"%ae","date":"%ai","message":"%f","parents":"%P"},',
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        stdout, stderr = process.communicate()

        if process.returncode != 0:
            log.error(
                f"722842af-6695-4ead-a484-a65763db9bae Problem running git log command: {stderr}"
            )
            return None

        try:
            commits = json.loads("[" + re.sub(r",\s*$", "", stdout) + "]")
            return [
                {
                    **commit,
                    "parents": commit["parents"].split(" ")
                    if commit["parents"]
                    else None,
                }
                for commit in commits
            ]
        except json.JSONDecodeError:
            print(
                f"b5e5942e-697a-45c2-b713-d32562aec7b2 Problem decoding JSON from git log output: {stdout}"
            )
            return None

    except Exception as e:
        print(
            f"3c111df2-4d0b-4a1e-8184-f5245054e166 Problem running git log command: {e}"
        )
        return None


def git_diagram():
    commits = git_commits()
    nt = Network("500px", "500px")
    for commit in commits:
        nt.add_node(commit["hash"], label=commit["hash"])
    for commit in commits:
        if commit["parents"]:
            for parent in commit["parents"]:
                nt.add_edge(commit["hash"], parent)
    # nt.add_edge(1, 2)
    script_dir = pathlib.Path(__file__).parent.absolute()
    out_dir = script_dir / "out"
    os.makedirs(out_dir, exist_ok=True)
    os.chdir(out_dir)
    nt.write_html("nx.html", notebook=False)


def main():
    git_diagram()


if __name__ == "__main__":
    main()
