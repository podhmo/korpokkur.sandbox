# -*- coding:utf-8 -*-

from zope.interface import implementer
from korpokkur.interfaces import IScaffoldTemplate
from korpokkur.pyramid_presentation.helpers import get_package_name
from korpokkur.input import compute_value
import os.path

import logging
logger = logging.getLogger(__name__)

@compute_value
def compute_path(input, _):
    xxx = os.path.join(input.load("name"), input.load("route_name"))
    return xxx

@compute_value
def compute_view_definition(input, _):
    fmt = """\
@view_config(route_name="{route_name}", renderer="{renderer}")
def {function_name}(context, request):
    return {{}}
"""
    route_name=input.load("route_name")
    return fmt.format(
        route_name=route_name, 
        renderer="{}.html".format(input.load("path")), 
        function_name="{}_view".format(route_name.replace(".", "_"))
    )

@compute_value
def compute_add_route(input, _):
    fmt = """config.add_route("{route_name}", "{path}")"""
    return fmt.format(
        route_name=input.load("route_name"), 
        path=input.load("path"))

## see: korpokkur.interfaces:IScaffoldTemplate
@implementer(IScaffoldTemplate)
class Template(object):
    """create new route scaffold"""
    source_directory = os.path.join(os.path.abspath(os.path.dirname(__file__)), "+package+")
    ##varname -> description, default
    expected_words = {
        "name": ("module name", "hello"), 
        "route_name": ("route name", "greeting"), 
        "path": ("path", compute_path), 
    }
    marker_comments = {
        "*add_route*": "# [marker] add route", 
        "*view_definition*": "# [marker] view definition"
    }
    cache = {
        "package": get_package_name, 
        "path": compute_path, 
        "*add_route*": compute_add_route, 
        "*view_definition*": compute_view_definition
    }
    template_engine = "mako"

