from argparse import ArgumentTypeError
from z.template import apply_template 
from pathlib import Path
from typing import List
import datetime
import re

# Format: <timestamp>--<title>__<tag1>_<tag2>.<ext>
def normalize_name(name: str, tags: str, time: datetime.date | None = None, ext: str ="md"):
    if "-" in name or "_" in name:
        raise ArgumentTypeError("Title cannot have '-' or '_'")
    if "-" in name or "_" in tags:
        raise ArgumentTypeError("Note cannot have '-' or '_'")

    # timestamp
    if time:
        f = time.strftime("%Y%m%dT%H%M%S")
    else:
        f = datetime.datetime.now().strftime("%Y%m%dT%H%M%S")

    # title
    f += "--"
    f += re.sub(r" ", "-", name).strip()

    # tags
    f += "__"
    for tag in tags.split(","):
        tag = tag.strip()
        tag = re.sub(r" ", "-", tag)
        f += tag + "_"
    f = f[:-1]

    # ext
    if ext[0] == ".":
        f += ext
    else:
        f += "." + ext
    return f

def create_file(name: str, silo: str, template: str = "default.md"):
    if silo:
        Path(silo).mkdir(exist_ok=True)
        if silo[-1] != "/":
            silo += "/"
    content = apply_template(Path.home().joinpath(".config/z-py/templates"), template)
    with open(silo + name, "w") as f:
        f.write(content)
    return

def main(args):
    file = normalize_name(args.name, args.tags)
    create_file(file, args.silo) 

if __name__ == "__main__":
    main(None)
