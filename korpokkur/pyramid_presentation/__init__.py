# -*- coding:utf-8 -*-

from zope.interface import implementer
from korpokkur.interfaces import IScaffoldTemplate
from .helpers import get_package_name
import os.path

import logging
logger = logging.getLogger(__name__)

## see: korpokkur.interfaces:IScaffoldTemplate
@implementer(IScaffoldTemplate)
class Package(object):
    """presentation part scaffold (include views templates)"""
    source_directory = os.path.join(os.path.abspath(os.path.dirname(__file__)), "+package+")
    ##varname -> description, default
    expected_words = {
        "name": ("module name", "hello"), 
    }
    cache = {"package": get_package_name}
    template_engine = "mako"

