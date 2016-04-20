from google.appengine.api import users
from google.appengine.ext import ndb
from Classes.tarea import Tarea
from jinja2 import Environment, FileSystemLoader

import os
import webapp2
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)+"../templates"),
    extensions=["jinja2.ext.autoescape"],
    autoescape=True)


class ListarTareas(webapp2.RedirectHandler):
    def __init__(self, request=None, response=None):
        self.initialize(request, response)
        self.user = users.get_current_user()

    def get(self):
        if self.user is not None:
            logout_link = users.create_logout_url("/")
            tareas = Tarea.query(Tarea.user == self.user.user_id()).order(Tarea.fecha_entrega)

            template_values = {
                "user_name": self.user.nickname(),
                "logout_link": logout_link,
                "tareas": tareas
            }

            template = JINJA_ENVIRONMENT.get_template('listar_tareas.html')
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")


class AddTarea(webapp2.RedirectHandler):
    def get(self):
        pass


class BorrarTarea(webapp2.RedirectHandler):
    def post(self):
        pass