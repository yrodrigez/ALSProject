# tarea.py
from google.appengine.ext import ndb
__author__ = "Yago Rodriguez"


class Tarea(ndb.Model):
    titulo = ndb.StringProperty(required=True)
    fecha_entrega = ndb.DateTimeProperty(required=True)
    asignatura = ndb.StringProperty(required=True)
