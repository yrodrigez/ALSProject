# asignaturas.py
from google.appengine.api import users
from google.appengine.ext import ndb

from Classes.asignatura import Asignatura
from google.appengine.api import users
from Classes.tarea import Tarea

import os
import webapp2
import jinja2
import time
from datetime import datetime, timedelta

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=["jinja2.ext.autoescape"],
    autoescape=True)


class ListarAsignaturas(webapp2.RedirectHandler):
    def __init__(self, request=None, response=None):
        self.initialize(request, response)
        self.user = users.get_current_user()

    def get(self):
        if self.user is not None:
            logout_link = users.create_logout_url("/")
            asignaturas = Asignatura.query(Asignatura.user == self.user.user_id())

            template_values = {
                "user_name": self.user.nickname(),
                "logout_link": logout_link,
                "asignaturas": asignaturas,
                "user": self.user,

            }

            template = JINJA_ENVIRONMENT.get_template('templates/asignaturas/listar.html')
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")


class AddAsignatura(webapp2.RedirectHandler):
    def __init__(self, request=None, response=None):
        self.initialize(request, response)
        self.user = users.get_current_user()

    def get(self):
        if self.user is not None:
            logout_link = users.create_logout_url("/")

            error = ""
            info = ""
            try:
                error = self.request.GET["error"]
            except:
                pass
            try:
                info = self.request.GET["info"]
            except:
                pass

            template_values = {
                "error": error,
                "info": info,
                "user_name": self.user.nickname(),
                "logout_link": logout_link,
                "user": self.user
            }

            template = JINJA_ENVIRONMENT.get_template('templates/asignaturas/add.html')
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")

    def post(self):
        if self.user is not None:
            asignatura = Asignatura()
            asignatura.nombre = self.request.get("nombre")
            asignatura.user = self.user.user_id()

            asignatura.put()
            time.sleep(1)

            self.redirect("/listar_asignaturas")
        else:
            self.redirect("/")


class BorrarAsignatura(webapp2.RedirectHandler):
    def __init__(self, request=None, response=None):
        self.initialize(request, response)
        self.user = users.get_current_user()

    def post(self):
        if self.user is not None:
            id = self.request.get('id')
            asignatura = ndb.Key(urlsafe=id).get()

            asignatura.key.delete()
            time.sleep(1)

            self.redirect("/listar_asignaturas?info=Asignatura "+asignatura.nombre+" eliminada")
        else:
            self.redirect("/")

