#!/usr/bin/python3
import os
import cgi
import cgitb
import json
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
import logging
import datetime
from db_handler import Database

cgitb.enable()
logger = logging.getLogger()
database = Database.instance()

print("Content-Type: application/json;charset=utf-8")
print()


class Datos(declarative_base()):
    __tablename__ = 'datos'

    dni = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    fecha_nacimiento = Column(Date)
    direccion = Column(String)
    telefono = Column(String)
    mail = Column(String)
    estado_civil = Column(String)

    def __init__(self, dni,nombre, apellido, fecha_nacimiento, direccion, telefono, mail, estado_civil):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.direccion = direccion
        self.telefono = telefono
        self.mail = mail
        self.estado_civil = estado_civil


def alta_datos():
    try:

        form = cgi.FieldStorage()
        fechaNacimiento = datetime.datetime.strptime(form.getvalue('fecha_nacimiento'), "%m/%d/%Y").strftime("%Y-%m-%d")
        dni = form.getvalue('dni')
        if database.existe_usuario(dni):
            return {'error': True, 'dni': True}
        datos = Datos(
            dni,
            form.getvalue('nombre'),
            form.getvalue('apellido'),
            fechaNacimiento,
            form.getvalue('direccion'),
            form.getvalue('telefono'),
            form.getvalue('mail'),
            form.getvalue('estado_civil')
        )
        logger.error(datos.dni, datos.nombre,datos.apellido,datos.fecha_nacimiento,datos.direccion,datos.telefono,datos.mail,datos.estado_civil)
        database.insert_datos(datos)
        datosGuardados = database.get_datos()
        logger.error(datosGuardados)
        return {'error': False}
    except:
        return {'error': True}


if os.environ['REQUEST_METHOD'] == 'POST':
    response = alta_datos()
if not response:
    response = {}

print(json.JSONEncoder().encode(response))
