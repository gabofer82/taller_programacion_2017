# -*- coding: utf-8 -*-
from .basededatos import BaseDeDatos


class PerPersona(BaseDeDatos):

    def obtener_uno(self, id_):
        """
        Obtiene y retorna un objeto según el id dado.
        :param id_: int >= 0
        :return: object
        """
        if id_ >= 0:
            id_ = (id_,)
            sql = 'SELECT * FROM persona WHERE id=?'
            fila = self.obtener(sql, id_)
            return fila
        else:
            print 'El parámetro debe ser mayor o igual a 0.'
            return None

    def obtener_listado(self, **kwargs):
        """
        Obtiene y retorna un listado de objetos según los filtros pasados.
        :param kwargs: dict 
        :return: dict
        """
        if 'pagina' in kwargs:
            total_filas = self.contar_filas('persona')
            offset = kwargs['pagina'] * 10  #resultados por pagina
            if offset < total_filas:  # TODO: ver aca el asunto de paginacion
                sql = 'SELECT * FROM persona LIMIT(10) OFFSET(?)'
                data = (offset,)
                lista_de_filas = self.obtener(sql, data, True)
                return lista_de_filas
            return None
        else:
            return None

    def agregar_objeto(self, obj):
        """
        Prepara los datos de un objeto para ser insertado en la base de datos.
        :param obj: object
        :return: int
        """
        sql = 'INSERT INTO persona VALUES (null, ?, ?, ?, ?, ?, ?)'
        pk = self.salvar(sql, (obj.nombres, obj.apellidos, obj.domicilio,
                                obj.obj_documento.pk,
                                obj.obj_ubicacion_geo.pk, obj.baja))
        return pk

    def actualizar_objeto(self, obj):
        """
        Prepara los datos de un objeto para actualizar su registro correlativo 
        en la base de datos.
        :param obj: object
        :return: bool
        """
        sql = 'UPDATE pacientes SET nombres = ?, apellidos = ?, domicilio = ?,\
               documentoId = ?, ubicacionGeoId = ?, baja = ? WHERE id = ?'
        return self.actualizar(sql, (obj.nombres, obj.apellidos, obj.domicilio,
                                     obj.obj_documento.pk,
                                     obj.obj_ubicacion_geo.pk, obj.baja))

    def baja_objeto(self, obj):
        """
        Obtiene el id del objeto para dar una baja lógica en el registro co-
        rrespondiente en la base de datos.
        :param obj: object 
        :return: bool
        """
        sql = 'UPDATE persona SET baja = ? WHERE id = ?'
        return self.actualizar(sql, (1, obj.id_))
