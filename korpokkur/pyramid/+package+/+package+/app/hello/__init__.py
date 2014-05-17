# -*- coding:utf-8 -*-
import logging
logger = logging.getLogger(__name__)

def includeme(config):
    config.add_route("/hello", "/hello")
    config.scan(".views")
