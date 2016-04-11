# Persona.py

from google.appengine.ext import ndb


class Person(ndb.Model):
        name = ndb.StringProperty(required=True)
        surname = ndb.StringProperty(required=True)
        phone = ndb.IntegerProperty()

