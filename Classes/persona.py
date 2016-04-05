# Persona.py


class Person:
    def __init__(self, name, surname, phone):
        self.__name = name
        self.__surname = surname
        self.__phone = phone

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @property
    def phone(self):
        return self.__phone

    def set_name(self, name):
        self.__name = name

    def set_surname(self, surname):
        self.__surname = surname

    def set_phone(self, phone):
        self.__phone = phone

    def __str__(self):
        return "Person\nName: " + self.__name + "\nSurname" + self.__surname + "\nPhone: " + self.phone
