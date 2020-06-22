import argparse

from ltman.main import process_all


parser = argparse.ArgumentParser(description="Download, convert, and normalize online videos.")

parser.add_argument("links", type=str, nargs="+", help="Links to process.")

args = parser.parse_args()

if __name__ == "__main__":
    process_all(args.links)
