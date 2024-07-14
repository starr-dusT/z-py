from z import template_funcs
from pathlib import Path
from typing import List
import re

def read_file(p: Path, n: str):
    f_path = p.joinpath(n)
    with open(f_path, "r") as f:
        return f.read()
    return -1

def split_template(s: str) -> (List[str], str):
    return re.findall(r"{([^}]+)}", s), re.sub(r"{([^}]+)}", "{}", s)

def apply_template(path: Path, name: str):
    fns, s = split_template(read_file(path, name))
    return s.format(*[eval("template_funcs." + fn)() for fn in fns])
