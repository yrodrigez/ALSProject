from google.appengine.api import users
from google.appengine.ext import ndb
from Classes.tarea import Tarea

import os
import webapp2
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=["jinja2.ext.autoescape"],
    autoescape=True)


class ListarTareas(webapp2.RedirectHandler):
    def get(self):
        pass


class AddTarea(webapp2.RedirectHandler):
    def get(self):
        pass


class BorrarTarea(webapp2.RedirectHandler):
    def post(self):
        pass