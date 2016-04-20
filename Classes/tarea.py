# tarea.py
from google.appengine.ext import ndb
__author__ = "Yago Rodriguez"


class Tarea(ndb.Model):
    titulo = ndb.StringProperty(required=True)
    fecha_entrega = ndb.DateProperty(auto_now_add=True)
    asignatura = ndb.StringProperty()
    descripcion = ndb.StringProperty(required=True)
    user = ndb.StringProperty(required=True)
