# tarea.py
from google.appengine.ext import ndb
__author__ = "Yago Rodriguez"


class Tarea(ndb.Model):
    titulo = ndb.StringProperty(required=True)
    fecha_entrega = ndb.DateTimeProperty(auto_now_add=True)
    asignatura = ndb.StringProperty(required=True)
    user = ndb.StringProperty(required=True)
