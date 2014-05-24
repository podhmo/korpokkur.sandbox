# -*- coding:utf-8 -*-

from zope.interface import implementer
from korpokkur.interfaces import IScaffoldTemplate
from .helpers import get_package_name
import os.path
from korpokkur.input import compute_value
import logging
logger = logging.getLogger(__name__)


@compute_value
def compute_add_module(input, _):
    fmt = """config.include(".{module}")"""
    return fmt.format(module=input.load("name"))

## see: korpokkur.interfaces:IScaffoldTemplate
@implementer(IScaffoldTemplate)
class Package(object):
    """presentation part scaffold (include views templates)"""
    source_directory = os.path.join(os.path.abspath(os.path.dirname(__file__)), "+package+")
    ##varname -> description, default
    expected_words = {
        "name": ("module name", "hello"), 
    }
    marker_comments = {
        "*add_module*": "# [marker] add module", 
    }
    cache = {
        "package": get_package_name,
        "*add_module*": compute_add_module
    }
    template_engine = "mako"

