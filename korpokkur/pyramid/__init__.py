# -*- coding:utf-8 -*-

from zope.interface import implementer
from korpokkur.interfaces import IScaffoldTemplate
import os.path

@implementer(IScaffoldTemplate)
class Template(object):
    """individual scaffold set"""
    source_directory = os.path.join(os.path.abspath(os.path.dirname(__file__)), "+package+")
    expected_words = {
    }
    cache = {}
    __dro__ = ["korpokkur.scaffolds.pygitignore:Package"]
    template_engine = "mako" #or jinja2
