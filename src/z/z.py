from pathlib import Path
import argparse
from z import create
import sys

def init_parser():
    parser = argparse.ArgumentParser(prog="z.py", description="top level prog")
    sub_parsers = parser.add_subparsers(help="subcommand help")
    create_parser = sub_parsers.add_parser("create", help="create note")
    create_parser.set_defaults(func=create.main)
    create_parser.add_argument("name", help="name of note to create")
    create_parser.add_argument("-t", "--tags", nargs="?", default="", const="", help="comma seperated list of tags for note")
    create_parser.add_argument("-s", "--silo", nargs="?", default="", const="", help="Optionally create note in silo")
    return parser

def main():
    z_file = Path("./.z")
    if not z_file.is_file():
        raise Exception("You aren't in a z.py folder. Re-run in a z.py folder") 
    parser = init_parser()
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    sys.exit(main())
