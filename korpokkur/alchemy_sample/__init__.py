# -*- coding:utf-8 -*-

from zope.interface import implementer
from korpokkur.interfaces import IScaffoldTemplate
from korpokkur.pyramid_presentation.helpers import get_package_name
from korpokkur.input import compute_value
import os.path

import logging
logger = logging.getLogger(__name__)

## see: korpokkur.interfaces:IScaffoldTemplate
@implementer(IScaffoldTemplate)
class Template(object):
    """create new route scaffold"""
    source_directory = os.path.join(os.path.abspath(os.path.dirname(__file__)), "app")
    ##varname -> description, default
    expected_words = {
        "filename": ("file name", "alchemy_sample"), 
        "modelname": ("first model name", "MyModel"), 
    }
    cache = {}
    template_engine = "mako"


