import argparse
import pathlib
from typing import List

from ltman.main import process_all


parser = argparse.ArgumentParser(description="Download, convert, and normalize online videos.")

parser.add_argument("links", type=str, nargs="+", help="Links to process.")

args = parser.parse_args()

def retrieve(passed: List[str]) -> List[str]:
    """
    Retrieves all items that are able to be
    converted, recursively, from the passed list.

    Parameters
    ----------
    passed: List[str]
        The items to search.

    Returns
    -------
    List[str]:
        All found items.
    """
    ret = []

    for item in passed:
        try:
            path = pathlib.Path(item)
            if path.is_file() and path.suffix == ".txt":
                ret += retrieve(path.read_text().split("\n"))
            elif path.is_file():
                ret.append(str(path))
            elif path.is_dir():
                ret += retrieve([str(p) for p in path.iterdir()])
            else:
                ret.append(item)
        except OSError:
            ret.append(item)

    return ret

if __name__ == "__main__":
    process_all(retrieve(args.links))
