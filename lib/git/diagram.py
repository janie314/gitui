import os
import pathlib
from lib.git.git import git_commits
from pyvis.network import Network


def git_diagram():
    commits = git_commits()
    nt = Network("500px", "500px")
    for commit in commits:
        nt.add_node(commit["hash"], label=commit["short_hash"]+" "+commit["message"])
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
