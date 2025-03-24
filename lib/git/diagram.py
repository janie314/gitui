import os
import pathlib
from lib.git.git import git_commits
from pyvis.network import Network
import json


def write_git_diagram_html():
    commits = git_commits()
    nt = Network("1000px", "1000px")
    for i, commit in enumerate(commits):
        nt.add_node(
            commit["hash"],
            label=commit["short_hash"] + "\n" + commit["message"],
            y=i * 10,
        )
    for commit in commits:
        if commit["parents"]:
            for parent in commit["parents"]:
                nt.add_edge(commit["hash"], parent)
    script_dir = pathlib.Path(__file__).parent.absolute()
    out_dir = script_dir / "../../out"
    os.makedirs(out_dir, exist_ok=True)
    os.chdir(out_dir)
    nt.write_html("commits.html", notebook=False)


def write_git_diagram_json():
    commits = git_commits()
    commits_json = json.dumps(commits, separators=(",", ":"))

    script_dir = pathlib.Path(__file__).parent.absolute()
    out_dir = script_dir / "../../out"
    os.makedirs(out_dir, exist_ok=True)
    os.chdir(out_dir)

    with open("commits.json", "w") as f:
        f.write(commits_json)
