from pathlib import Path
import argparse
from z import create, tags
import sys

def init_parser():
    parser = argparse.ArgumentParser(prog="z.py", description="top level prog")
    sub_parsers = parser.add_subparsers(help="subcommand help")
    
    create_parser = sub_parsers.add_parser("create", help="create note")
    create_parser.set_defaults(func=create.main)
    create_parser.add_argument("name", help="name of note to create")
    create_parser.add_argument("-t", "--tags", nargs="?", default="", const="", help="comma seperated list of tags for note")
    create_parser.add_argument("-s", "--silo", nargs="?", default="", const="", help="Optionally create note in silo")

    tags_parser = sub_parsers.add_parser("tags", help="edit tags")
    tags_parser.set_defaults(func=tags.main)
    tags_parser.add_argument("file", help="name of file to create")

    return parser

def main():
    z_file = Path("./.z")
    if not z_file.is_file():
        raise Exception("You aren't in a z-py folder! Re-run in a z.py folder") 
    parser = init_parser()
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    sys.exit(main())
