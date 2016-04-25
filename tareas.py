from google.appengine.api import users
from google.appengine.ext import ndb
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


class ListarTareas(webapp2.RedirectHandler):
    def __init__(self, request=None, response=None):
        self.initialize(request, response)
        self.user = users.get_current_user()

    def get(self):
        if self.user is not None:
            logout_link = users.create_logout_url("/")
            tareas = Tarea.query(Tarea.user == self.user.user_id()).order(Tarea.fecha_entrega)

            for t in tareas:
                if t.fecha_entrega < datetime.now():
                    t.key.delete()
                if t.fecha_entrega < datetime.now() + timedelta(days=7):
                    t.venciendo = True
                else:
                    t.venciendo = False

            tareas = Tarea.query(Tarea.user == self.user.user_id()).order(Tarea.fecha_entrega)

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
                "user_name": self.user.nickname(),
                "logout_link": logout_link,
                "tareas": tareas,
                "user": self.user,
                "error": error,
                "info": info
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
            tarea = Tarea()
            tarea.user = self.user.user_id()
            tarea.titulo = self.request.get("titulo").strip()
            tarea.descripcion = self.request.get("descripcion")
            tarea.color = self.request.get("color")

            fecha = self.request.get("fecha").strip().split("-")
            try:
                dia_hora = fecha[2].split("T")
                hora = dia_hora[1].split(":")
                m_fecha = datetime(int(fecha[0]), int(fecha[1]), int(dia_hora[0]), int(hora[0]), int(hora[1]))

                tarea.fecha_entrega = m_fecha

                tarea.put()
                time.sleep(1)

                self.redirect("/list?info=Tarea agregada")
            except:
                self.redirect("/list?error=La fecha es vacia")
        else:
            self.redirect("/")


class BorrarTarea(webapp2.RedirectHandler):
    def __init__(self, request=None, response=None):
        self.initialize(request, response)
        self.user = users.get_current_user()

    def post(self):
        if self.user is not None:
            id = self.request.get('id')
            tarea = ndb.Key(urlsafe=id).get()
            tarea.key.delete()
            time.sleep(1)
            self.redirect("/")
        else:
            self.redirect("/")


class EditTarea(webapp2.RedirectHandler):
    def __init__(self, request=None, response=None):
        self.initialize(request, response)
        self.user = users.get_current_user()

    def get(self):
        if self.user is not None:
            logout_link = users.create_logout_url("/")
            id = self.request.get("id")
            tarea = ndb.Key(urlsafe=id).get()

            template_values = {
                "user_name": self.user.nickname(),
                "logout_link": logout_link,
                "user": self.user,
                "tarea": tarea,
            }

            template = JINJA_ENVIRONMENT.get_template('templates/edit_tarea.html')
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")

    def post(self):
        if self.user is not None:
            tarea = ndb.Key(urlsafe=self.request.get("id")).get()
            tarea.titulo = self.request.get("titulo").strip()
            tarea.descripcion = self.request.get("descripcion").strip()
            tarea.color = self.request.get("color")

            fecha = self.request.get("fecha").strip().split("-")
            try:
                dia_hora = fecha[2].split("T")
                hora = dia_hora[1].split(":")
                m_fecha = datetime(int(fecha[0]), int(fecha[1]), int(dia_hora[0]), int(hora[0]), int(hora[1]))

                tarea.fecha_entrega = m_fecha

                tarea.put()
                time.sleep(1)

                self.redirect("/list?info=Tarea editada")
            except:
                self.redirect("/list?error=La fecha es vacia")
        else:
            self.redirect("/")


class ViewTarea(webapp2.RedirectHandler):
    def __init__(self, request=None, response=None):
        self.initialize(request, response)
        self.user = users.get_current_user()

    def get(self):
        if self.user is not None:
            logout_link = users.create_logout_url("/")
            id = self.request.get("id")
            tarea = ndb.Key(urlsafe=id).get()

            template_values = {
                "user_name": self.user.nickname(),
                "logout_link": logout_link,
                "user": self.user,
                "tarea": tarea,
            }

            template = JINJA_ENVIRONMENT.get_template('templates/view_tarea.html')
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")
