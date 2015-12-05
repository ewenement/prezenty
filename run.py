#!/usr/bin/env python
# encoding: utf-8

import os

import cherrypy
from jinja2 import Environment, FileSystemLoader

import settings
import models


DIR_PATH = os.path.dirname(os.path.realpath(__file__))
STATIC_PATH = os.path.join(DIR_PATH, "Static")
TEMPLATES_PATH = os.path.join(DIR_PATH, "Templates")

# jinja enviorment
env = Environment(loader=FileSystemLoader(TEMPLATES_PATH), autoescape=False)


# === WIDOK ===

class Main_Page(object):

    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('index.html')
        return tmpl.generate({})

    @cherrypy.expose('listy_ewy')
    def ewas_gift_lists(self):
        tmpl = env.get_template('ewas_gift_lists.html')
        ctx = {
            'lists': {
                1: u'na urodziny',
                2: u'na imieniny',
                3: u'na dzień kotka',
            }
        }
        return tmpl.generate(ctx)

    @cherrypy.expose('lista_ewy')
    def ewas_gift_list(self):
        tmpl = env.get_template('ewas_gift_list.html')
        ctx = {
            'gifts': [
                [1, u'buttplug z ogonem', 20, 'sexlaski.pl/sklep'],
                [2, u'kocie żarcie', 20, 'sexlaski.pl/sklep'],
                [4, u'kajdanki', 50, 'definefetish.com/sklep'],
                [3, u'strój księżniczki Lei', 200, 'starwars.com/store/perversions'],
            ]
        }

        return tmpl.generate(ctx)

    @cherrypy.expose('dodaj_do_listy')
    def add_gift_to_list(self, list_id, **kwargs):
        tmpl = env.get_template('add_gift_to_list.html')
        return tmpl.generate(kwargs)


# ====== URUCHOMIENIE SERWERA ======

root = Main_Page()

cherrypy.config.update(settings.conf)
print (u'Zaczynam działać na {0}:{1}'.format(
        settings.conf['server.socket_host'],
        settings.conf['server.socket_port'],
    ))
cherrypy.quickstart(root, '/', config=settings.section)
