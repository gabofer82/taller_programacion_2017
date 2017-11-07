# -*- coding: utf-8 -*-
from .basededatos import BaseDeDatos


class PerEmpleado(BaseDeDatos):

    def obtener_uno(self, id_):
        """
        Obtiene y retorna un objeto según el id dado.
        :param id_: int >= 0
        :return: object
        """
        if id_ >= 0:
            id_ = (id_,)
            sql = 'SELECT * FROM empleados WHERE id=?'
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
            total_filas = self.contar_filas('pacientes')
            offset = kwargs['pagina'] * 10  #resultados por pagina
            dataset = None
            if offset < total_filas:  # TODO: ver aca el asunto de paginacion
                sql = 'SELECT * FROM empleados LIMIT(10) OFFSET(?) WHERE ' \
                      'baja=0'
                data = (offset,)
                dataset = self.obtener(sql, data, True)
            else:
                sql = 'SELECT * FROM empleados WHERE baja=0'
                dataset = self.obtener(sql, lista=True)

            return dataset
        else:
            return []

    def agregar_objeto(self, obj):
        """
        Prepara los datos de un objeto para ser insertado en la base de datos.
        :param obj: object
        :return: int
        """
        # obj.pk_persona = PerPersona().agregar_objeto(obj)
        sql = 'INSERT INTO empleados VALUES (null, ?, ?, ?, ?, ?)'
        pk = self.salvar(sql, ("", obj.pk_persona, obj.obj_sucursal.pk,
                               obj.tipo, obj.baja))
        return pk

    def actualizar_objeto(self, obj):
        """
        Prepara los datos de un objeto para actualizar su registro correlativo 
        en la base de datos.
        :param obj: object
        :return: bool
        """
        sql = 'UPDATE empleados SET personaId = ?, sucursalId = ?, tipo = ?\
                WHERE id = ?'
        return self.actualizar(sql, (obj.pk_persona, obj.obj_sucursal.pk,
                                     obj.tipo, obj.pk))

    def baja_objeto(self, obj):
        """
        Obtiene el id del objeto para dar una baja lógica en el registro co-
        rrespondiente en la base de datos.
        :param obj: object 
        :return: bool
        """
        sql = 'UPDATE empleados SET baja = ? WHERE id = ?'
        return self.actualizar(sql, (1, obj.pk))
