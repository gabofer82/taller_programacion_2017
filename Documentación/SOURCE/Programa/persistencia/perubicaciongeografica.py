# -*- coding: utf-8 -*-
from .basededatos import BaseDeDatos


class PerUbicacion(BaseDeDatos):

    def obtener_uno(self, id_):
        """
        Obtiene y retorna un objeto según el id dado.
        :param id_: int >= 0
        :return: object
        """
        if id_ >= 0:
            id_ = (id_,)
            sql = 'SELECT * FROM ubicaciones_geograficas WHERE id=?'
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
        dataset = []
        if 'pagina' in kwargs:
            total_filas = self.contar_filas('ubicaciones_geograficas')
            offset = kwargs['pagina'] * 10  #resultados por pagina
            if offset < total_filas:  # TODO: ver aca el asunto de paginacion
                sql = 'SELECT * FROM ubicaciones_geograficas LIMIT(10) '\
                      'OFFSET(?)'
                data = (offset,)
                dataset = self.obtener(sql, data, True)
            dataset = []
        else:
            sql = 'SELECT * FROM ubicaciones_geograficas'
            dataset = self.obtener(sql, lista=True)

        return dataset

    def agregar_objeto(self, obj):
        """
        Prepara los datos de un objeto para ser insertado en la base de datos.
        :param obj: object
        :return: object
        """
        sql = 'INSERT INTO sucursales VALUES (null, ?, ?)'
        id_ = self.salvar(sql, (obj.domicilio, obj.obj_ubigeo.id_,))
        obj.id_ = id_
        return obj


    def actualizar_objeto(self, obj):
        """
        Prepara los datos de un objeto para actualizar su registro correlativo 
        en la base de datos.
        :param obj: object
        :return: bool
        """
        sql = 'UPDATE sucursales SET domicilio = ?, ubicacionGeoId = ? WHERE \
              id = ?'
        return self.actualizar(sql, (obj.domicilio, obj.obj_ubigeo.id_,
                                    obj.id_))

    def baja_objeto(self, obj):
        """
        Obtiene el id del objeto para dar una baja lógica en el registro co-
        rrespondiente en la base de datos.
        :param obj: object 
        :return: bool
        """
        sql = 'UPDATE sucursales SET baja = ? WHERE id = ?'
        return self.actualizar(sql, (1, obj.id_))
