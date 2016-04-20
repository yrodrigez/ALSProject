from google.appengine.api import users
from google.appengine.ext import ndb
from Classes.tarea import Tarea
from jinja2 import Environment, FileSystemLoader

import os
import webapp2
import jinja2
import time
from datetime import datetime

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
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
                "tareas": tareas,
                "user": self.user
            }

            template = JINJA_ENVIRONMENT.get_template('templates/listar_tareas.html')
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")


class AddTarea(webapp2.RedirectHandler):
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
                "tareas": tareas,
                "user": self.user
            }

            template = JINJA_ENVIRONMENT.get_template('templates/add_tarea.html')
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")

    def post(self):
        if self.user is not None:
            logout_link = users.create_logout_url("/")
            tareas = Tarea.query(Tarea.user == self.user.user_id()).order(Tarea.fecha_entrega)

            template_values = {
                "user_name": self.user.nickname(),
                "logout_link": logout_link,
                "tareas": tareas,
                "user": self.user
            }

            tarea = Tarea()
            tarea.user = self.user.user_id()
            tarea.titulo = self.request.get("titulo").strip()
            tarea.descripcion = self.request.get("descripcion")

            fecha = self.request.get("fecha").strip().split("-")
            dia_hora = fecha[2].split("T")
            hora = dia_hora[1].split(":")
            m_fecha = datetime(int(fecha[0]), int(fecha[1]), int(dia_hora[0]), int(hora[0]), int(hora[1]))

            tarea.fecha_entrega = m_fecha

            tarea.put()
            time.sleep(1)

            template = JINJA_ENVIRONMENT.get_template('templates/listar_tareas.html')
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")


class BorrarTarea(webapp2.RedirectHandler):
    def post(self):
        pass