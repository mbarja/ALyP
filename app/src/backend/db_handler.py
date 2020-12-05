#!/usr/bin/python3
import os
import cgi
from http import cookies
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table, Column, String, Integer, MetaData, Date, ForeignKey, tuple_
import logging


logger = logging.getLogger()

class Database:

    __instance = None

    @staticmethod
    def instance():
        if (Database.__instance == None):
            Database.__instance = Database()
        return Database.__instance

    def __init__(self):
        if (Database.__instance is not None):
            return Database.__instance
        db_string = "postgres://admin:admin@app_db:5432/app_db"
        self.db = create_engine(db_string, echo=False)
        self.meta = MetaData(self.db)

        self.datos = Table(
                        'datos',
                        self.meta,
                        Column('dni', Integer, primary_key=True),
                        Column('nombre', String),
                        Column('apellido', String),
                        Column('fecha_nacimiento', Date),
                        Column('direccion', String),
                        Column('telefono', String),
                        Column('mail', String),
                        Column('estado_civil', String),
                       )

    def existe_usuario(self, dni):
        logger.error('existe_usuario')
        result = self.meta.tables["datos"]
        cookie_row = result.select().where(result.c.dni == dni)
        cookies_rs = self.db.execute(cookie_row)
        return cookies_rs.rowcount == 1

    def insert_datos(self, datos):
        statement = self.datos.insert().values(dni=datos.dni, nombre=datos.nombre,apellido=datos.apellido,
                                                  fecha_nacimiento=datos.fecha_nacimiento,
                                                  direccion=datos.direccion, telefono=datos.telefono,
                                                  mail=datos.mail, estado_civil=datos.estado_civil)
        logger.error(statement)
        self.db.execute(statement)

    def get_datos(self):
        logger.error('get_datos')
        result = self.meta.tables["datos"]
        datos_row = result.select()
        datos_rs = self.db.execute(datos_row)
        if (datos_rs.rowcount != 0):
            d, a = {}, []
            for rowproxy in datos_rs:
                # rowproxy.items() returns an array like [(key0, value0), (key1, value1)]
                for column, value in rowproxy.items():
                    # build up the dictionary
                    d = {**d, **{column: value}}
                a.append(d)
            return a
        else:
            logger.error("no hay datos")
            return []
