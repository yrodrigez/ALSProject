# tarea.py
from google.appengine.ext import ndb
__author__ = "Yago Rodriguez"

class Tarea(ndb.Model):
    titulo = ndb.StringProperty(required=True)
    fecha_entrega = ndb.DateTimeProperty(auto_now_add=True)
    asignatura = ndb.KeyProperty(required=True)
    descripcion = ndb.StringProperty(required=True)
    user = ndb.StringProperty(required=True)
    id = ndb.StringProperty()
    color = ndb.StringProperty()
    venciendo = ndb.BooleanProperty()