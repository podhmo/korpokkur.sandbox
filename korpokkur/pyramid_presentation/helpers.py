# -*- coding:utf-8 -*-
import ast
import os.path
import logging
logger = logging.getLogger(__name__)
from korpokkur.input import compute_value

def guess_package_name_from_module(m):
    for stmt in m.body:
        if isinstance(stmt, ast.Expr) and stmt.value.func.id == "setup":
            for kwd in stmt.value.keywords:
                if kwd.arg == "name":
                    return (kwd.value.s)

def guess_package_name_from_filename(f):
    with open(f) as rf:
        m = ast.parse(rf.read())
        return guess_package_name_from_module(m)

##print(guess_package_name_from_filename("./setup.py"))

@compute_value
def get_package_name(input, name):
    root = input.load(":root:")
    setup_path = os.path.join(root, "setup.py")
    logger.debug(":root: is %s", root)
    return guess_package_name_from_filename(setup_path).split(".", 1)[0]

def copyfile(context, filename=None):
    filename = filename or context[":dst:"]
    with open(filename) as rf:
        context.write(rf.read().strip("\n"))
    return ""
