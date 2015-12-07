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


    @cherrypy.expose('dodaj_liste')
    def add_new_gift_list(self, **kwargs):
        if kwargs:
            session = models.Session()
            session.add(models.GiftList(**kwargs))
            session.commit()

            # redirect
            raise cherrypy.HTTPRedirect("/listy_ewy", 303)

        tmpl = env.get_template('new_list.html')
        return tmpl.generate({})

    @cherrypy.expose('listy_ewy')
    def ewas_gift_lists(self):
        session = models.Session()

        tmpl = env.get_template('ewas_gift_lists.html')
        ctx = {
            'lists': session.query(models.GiftList).all()
        }

        return tmpl.generate(ctx)

    @cherrypy.expose('lista_ewy')
    def ewas_gift_list(self):
        tmpl = env.get_template('ewas_gift_list.html')
        session = models.Session()

        ctx = {
            'gifts': session.query(models.GiftRequest).join(models.GiftProduct).all()
        }

        return tmpl.generate(ctx)

    @cherrypy.expose('dodaj_do_listy')
    def add_gift_to_list(self, **kwargs):
        if kwargs:
            session = models.Session()
            kwargs.update(list_id=1)
            session.add(models.GiftRequest(**kwargs))
            session.commit()

            # redirect
            raise cherrypy.HTTPRedirect("/lista_ewy", 303)

        tmpl = env.get_template('add_gift_to_list.html')
        ctx = {'products': session.query(models.GiftProduct).all()}

        return tmpl.generate(ctx)


# ====== URUCHOMIENIE SERWERA ======

root = Main_Page()

cherrypy.config.update(settings.conf)
print (u'Zaczynam działać na {0}:{1}'.format(
        settings.conf['server.socket_host'],
        settings.conf['server.socket_port'],
    ))
cherrypy.quickstart(root, '/', config=settings.section)
