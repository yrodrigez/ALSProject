# profesor.py
from google.appengine.ext import ndb

__author__ = "Yago Rodriguez"


class Profesor(ndb.Model):
    nombre = ndb.StringProperty(Required=True)
    asignaturas = ndb.KeyProperty(kind="Asignatura", repeated=True)
    telefono = ndb.IntegerProperty()
    correo = ndb.StringProperty()
