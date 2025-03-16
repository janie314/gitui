import os
import pathlib
from pyvis.network import Network


def main():
    nt = Network("500px", "500px")
    nt.add_node(1, label="Node 1")
    nt.add_node(2, label="Node 2")
    nt.add_edge(1, 2)
    script_dir = pathlib.Path(__file__).parent.absolute()
    out_dir = script_dir / "out"
    os.makedirs(out_dir, exist_ok=True)
    os.chdir(out_dir)
    nt.write_html("nx.html", notebook=False)


if __name__ == "__main__":
    main()
