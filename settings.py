#!/usr/bin/env python
# encoding: utf-8

import os

from jinja2 import Environment, FileSystemLoader

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
STATIC_PATH = os.path.join(DIR_PATH, "Static")
TEMPLATES_PATH = os.path.join(DIR_PATH, "Templates")

if "OS" in os.environ and "Windows" in os.environ['OS']:
    TEST_RUN = True
else:
    TEST_RUN = False
TEST_RUN = True

# prepare jinja error pages
# jinja enviorment
env = Environment(loader=FileSystemLoader(TEMPLATES_PATH))
ERR_404_TEMPLATE = env.get_template('404.html').render().encode('utf-8')
ERR_500_TEMPLATE = env.get_template('500.html').render().encode('utf-8')


def get_error_page(status, message, traceback, version):
    if status.startswith('404'):
        return ERR_404_TEMPLATE
    elif status.startswith('500'):
        return ERR_500_TEMPLATE
    return u"Ups."

conf = {
    "server.socket_host": "127.0.0.1" if TEST_RUN else "0.0.0.0",
    "server.socket_port": 8095 if TEST_RUN else 10000,
    "server.thread_pool": 5,
    "server.max_request_body_size": 1000000,
    "tools.encode.on": True,
    "tools.encode.encoding": "utf-8",
    "error_page.404": get_error_page,
    "error_page.413": get_error_page,
    "error_page.500": get_error_page,
    "log.error_file": DIR_PATH + "/Errors.txt",
    "log.screen": TEST_RUN,
    'engine.autoreload_on': True if TEST_RUN else False,
}


section = {
    "/": {
        "tools.staticdir.on": True,
        "tools.staticdir.root": DIR_PATH,
        "tools.staticdir.dir": "Static",
    },
    "/favicon.ico": {
        "tools.staticfile.on": True,
        "tools.staticfile.filename": DIR_PATH + "/Static/favicon.ico"
    }
}

# write a pid file
if not TEST_RUN:
    with open('MarkerIcons.pid', 'w') as f:
        #f.write(str(os.getpid()))
        pass
