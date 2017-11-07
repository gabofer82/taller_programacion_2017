# -*- coding: utf-8 -*-
import sqlite3
import os


class BaseDeDatos:
    def __init__(self):

        self._database_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), 'data_sqlite3')
        try:
            self._conn = sqlite3.connect(self._database_path)
        except Exception as e:
            print(e.message)
            return None
        self._cursor = self._conn.cursor()

    def obtener(self, sql, data=None, lista=False):
        """
        Ejecuta el sql recibido, este debe ser un select.
        :param sql: str, data: tuple, lista: bool
        :return: list
        """
        try:
            if data:
                self._cursor.execute(sql, data)
            else:
                self._cursor.execute(sql)
            if lista:
                return self._cursor.fetchall()
            else:
                return self._cursor.fetchone()

        except Exception as e:
            print (e.message)
            return []

    def salvar(self, sql, data):
        """
        Ejecuta el sql recibido, este debe ser un insert.
        :param sql: str, data: tuple
        :return: int
        """
        try:
            self._cursor.execute(sql, data)
            self._conn.commit()
            return self._cursor.lastrowid
        except Exception as e:
            print (e.message)
            return -1

    def actualizar(self, sql, data):
        """
        Ejecuta el sql recibido, este debe ser un update.
        :param sql: str
        :param data: tuple
        :return: bool
        """
        try:
            self._cursor.execute(sql, data)
            self._conn.commit()
            return True
        except Exception as e:
            print (e.message)
            return False

    def borrar(self, sql, data):
        """
        Ejecuta el sql recibido, este debe ser un update porque es un delete
        lógico.
        :param sql: str
        :param data: tuple
        :return: bool
        """
        try:
            self._cursor.execute(sql, data)
            self._conn.commit()
            return True
        except Exception as e:
            print (e.message)
            return False

    def obtener_uno(self, id_):
        """
        Obtiene y retorna un objeto según el id dado.
        Debe ser sobreescrito en subclase.
        :param id_: int >= 0
        :return: object
        """
        pass

    def obtener_listado(self, **kwargs):
        """
        Obtiene y retorna un listado de objetos según los filtros pasados.
        Debe ser sobreescrito en subclase.
        :param kwargs: dict 
        :return: dict
        """
        pass

    def agregar_objeto(self, obj):
        """
        Convierte un objeto para ser insertado en la base de datos.
        Debe ser sobreescrito en subclase.
        :param obj: object
        :return: object
        """
        pass

    def actualizar_objeto(self, obj):
        """
        Convierte un objeto para actualizar su registro correlativo en la base
        de datos.
        Debe ser sobreescrito en subclase.
        :param obj: object
        :return: object
        """
        pass

    def baja_objeto(self, obj):
        """
        Obtiene el id del objeto para dar una baja lógica en el registro co-
        rrespondiente en la base de datos.
        Debe ser sobreescrito en subclase.
        :param obj: object 
        :return: bool
        """
        pass

    def contar_filas(self, tabla):
        """
        Obtiene el numero total del filas de la tabla indicada en el parametro.
        :param tabla: str 
        :return: int
        """
        try:
            sql = 'SELECT * FROM {}'.format(tabla)
            self._cursor.execute(sql)
            res = self._cursor.fetchall()
            return len(res)
        except Exception as e:
            print e

    def ejecutar_script_inicio(self, sqlstream):
        """
        Ejecuta el script que inicia la base de datos.
        
        :param sqlstream: string object 
        :return: None
        """
        self._cursor.executescript(sqlstream)
        self._conn.commit()
        self._conn.close()
