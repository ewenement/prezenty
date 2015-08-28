#!/usr/bin/env python
# encoding: utf-8

import os

import cherrypy
from jinja2 import Environment, FileSystemLoader

import settings

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
STATIC_PATH = os.path.join(DIR_PATH, "Static")
TEMPLATES_PATH = os.path.join(DIR_PATH, "Templates")

# jinja enviorment
print TEMPLATES_PATH
env = Environment(loader=FileSystemLoader(TEMPLATES_PATH), autoescape=False)


# === WIDOK ===
class Main_Page(object):

    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('index.html')
        return tmpl.generate({})

    @cherrypy.expose
    def ico(self, **kwargs):
        return str(kwargs)


# ====== URUCHOMIENIE SERWERA ======

root = Main_Page()

cherrypy.config.update(settings.conf)
print (u'Zaczynam działać na {0}:{1}'.format(
        settings.conf['server.socket_host'],
        settings.conf['server.socket_port'],
    ))
cherrypy.quickstart(root, config=settings.section)
