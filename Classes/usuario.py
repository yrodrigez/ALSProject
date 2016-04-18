# persona.py
__author__ = "Yago Rodriguez"
from google.appengine.ext import ndb


class Usuario(ndb.Model):
        """
        Usuario
        @:var name nombre del usuario
        @:var tareas las tarias asociadas al usuario
        """
        name = ndb.StringProperty(required=True)
        tareas = ndb.KeyProperty(kind="Tarea", repeated=True)

