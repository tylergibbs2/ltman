import argparse

from ltman.main import process_all


parser = argparse.ArgumentParser(description="Download, convert, and normalize online videos.")

parser.add_argument("links", type=str, nargs="+", help="Links to process.")

args = parser.parse_args()

if __name__ == "__main__":
    to_process = []
    for link in args.links:
        if link.endswith("txt"):
            with open(link, "r") as f:
                to_process += f.readlines()
        else:
            to_process.append(link)
    process_all(to_process)
