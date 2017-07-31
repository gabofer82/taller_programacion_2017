import sqlite3


class BaseDeDatos:
    def __init__(self):
        self._database_path = 'data.sql'
        self._conn = sqlite3.connect(self._database_path)
        self._cursor = self._conn.cursor()

    def get(self, sql):
        """
        Ejecuta el sql recibido, este debe ser un select.
        :param sql: str
        :return: bool
        """
        try:
            self._cursor.execute(sql)
            dataset = []
            for row in self._cursor:
                dataset.append(row)
            return dataset
        except Exception as e:
            print (e.message)
            return []


    def post(self, sql):
        """
        Ejecuta el sql recibido, este debe ser un insert o update.
        :param sql: str
        :return: list
        """
        try:
            self._cursor.execute(sql)
            self._conn.commit()
            return self._cursor.lastrowid
        except Exception as e:
            print (e.message)
            return -1

    def delete(self, sql):
        """
        Ejecuta el sql recibido, este debe ser un update porque es un delete
        lógico.
        :param sql: str
        :return: bool
        """
        self._cursor.execute(sql)
        try:
            self._conn.commit()
            return True
        except Exception as e:
            print (e.message)
            return False

    def obtener_uno(self, id_):
        """
        Obtiene y retorna un objeto según el id dado.
        :param id_: int >= 0
        :return: object
        """
        pass

    def obtener_listado(self, **kwargs):
        """
        Obtiene y retorna un listado de objetos según los filtros pasados.
        :param kwargs: dict 
        :return: dict
        """
        pass

    def agregar_objeto(self, obj):
        """
        Convierte un objeto para ser insertado en la base de datos.
        :param obj: object
        :return: object
        """
        pass

    def actualizar_objeto(self, obj):
        """
        Convierte un objeto para actualizar su registro correlativo en la base
        de daots.
        :param obj: object
        :return: object
        """
        pass

    def baja_objeto(self, obj):
        """
        Obtiene el id del objeto para dar una baja lógica en el registro co-
        rrespondiente en la base de datos.
        :param obj: object 
        :return: bool
        """
        pass
