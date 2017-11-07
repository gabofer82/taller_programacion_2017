# -*- coding: utf-8 -*-
from .basededatos import BaseDeDatos


class PerDocumento(BaseDeDatos):

    def obtener_uno(self, id_):
        """
        Obtiene y retorna un objeto según el id dado.
        :param id_: int >= 0
        :return: tuple
        """
        if id_ >= 0:
            id_ = (id_,)
            sql = 'SELECT * FROM documentos WHERE id=?'
            return list(self.obtener(sql, id_))
        else:
            print 'El parámetro debe ser mayor o igual a 0.'
            return None

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
        :return: int
        """
        sql = 'INSERT INTO documentos VALUES (null, ?, ?, ?)'
        pk = self.salvar(sql, (obj.tipo, obj.numero, obj.baja))
        return pk

    def actualizar_objeto(self, obj):
        """
        Convierte un objeto para actualizar su registro correlativo en la base
        de daots.
        :param obj: object
        :return: object
        """
        sql = 'UPDATE documentos SET tipo = ?, numero = ?, baja = ? ' \
              'WHERE id = ?'
        return self.actualizar(sql, (obj.tipo, obj.numero, obj.baja, obj.pk))

    def baja_objeto(self, obj):
        """
        Obtiene el id del objeto para dar una baja lógica en el registro co-
        rrespondiente en la base de datos.
        :param obj: object 
        :return: bool
        """
        sql = 'UPDATE documentos SET baja = ? WHERE id = ?'
        return self.actualizar(sql, (1, obj.pk))
