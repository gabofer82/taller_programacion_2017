# -*- coding: utf-8 -*-
from .basededatos import BaseDeDatos
from .perpersona import PerPersona


class PerPaciente(BaseDeDatos):

    def obtener_uno(self, id_):
        """
        Obtiene y retorna un objeto según el id dado.
        :param id_: int >= 0
        :return: object
        """
        if id_ >= 0:
            id_ = (id_,)
            sql = 'SELECT * FROM pacientes WHERE id=?'
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
                sql = 'SELECT * FROM pacientes LIMIT(10) OFFSET(?) WHERE ' \
                      'baja=0'
                data = (offset,)
                dataset = self.obtener(sql, data, True)
            else:
                sql = 'SELECT * FROM pacientes WHERE baja=0'
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
        sql = 'INSERT INTO pacientes VALUES (null, ?, ?, ?, ?, ?)'
        pk = self.salvar(sql, (obj.pk_persona, obj.activo, obj.penalizado,
                         1, obj.baja))  # obj.obj_ficha_paciente.pk
        return pk

    def actualizar_objeto(self, obj):
        """
        Prepara los datos de un objeto para actualizar su registro correlativo 
        en la base de datos.
        :param obj: object
        :return: bool
        """
        sql = 'UPDATE pacientes SET personaId = ?, activo = ?, penalizado = ?,\
               fichaPacienteId = ? WHERE id = ?'
        return self.actualizar(sql, (obj.pk_persona, obj.activo,
                                     obj.penalizado,
                                     1, obj.pk))
        # TODO: arreglar ficha de paciente: hardcoding

    def baja_objeto(self, obj):
        """
        Obtiene el id del objeto para dar una baja lógica en el registro co-
        rrespondiente en la base de datos.
        :param obj: object 
        :return: bool
        """
        sql = 'UPDATE pacientes SET baja = ? WHERE id = ?'
        return self.actualizar(sql, (1, obj.pk))
