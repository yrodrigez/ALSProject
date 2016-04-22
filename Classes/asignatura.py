# asignatura.py
from google.appengine.ext import ndb

__author__ = "Yago Rodriguez"


class Asignatura(ndb.Model):
    nombre = ndb.StringProperty(Required=True)
    tareas = ndb.KeyProperty(kind="Tarea", repeated=True)