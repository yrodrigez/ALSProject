# asignatura.py

from google.appengine.ext import ndb
__author__ = "Yago Rodriguez"


class Asignatura(ndb.Model):
    nombre = ndb.StringProperty(required=True)
    user = ndb.StringProperty(required=True)
    id = ndb.StringProperty()


