# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
import logging
logger = logging.getLogger(__name__)

def includeme(config):
    config.add_route("hello", "/")
    config.scan(".views")
