# -*- coding: utf-8 -*-
from .basededatos import BaseDeDatos
from negocio.persona import Persona
from negocio.laboratorioexterno import LaboratorioExterno
from negocio.sucursal import Sucursal


class PerTelefono(BaseDeDatos):

    def obtener_uno(self, id_):
        """
        Obtiene y retorna un objeto según el id dado.
        :param id_: int >= 0
        :return: tuple
        """
        if id_ >= 0:
            id_ = (id_,)
            sql = 'SELECT * FROM telefonos WHERE id=?'
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
        sql = 'INSERT INTO telefonos VALUES (null, ?, ?)'
        pk = self.salvar(sql, (obj.numero, obj.baja))

        return pk

    def actualizar_objeto(self, obj):
        """
        Convierte un objeto para actualizar su registro correlativo en la base
        de daots.
        :param obj: object
        :return: object
        """
        sql = 'UPDATE telefonos SET numero = ?, baja = ? WHERE id = ?'
        return self.actualizar(sql, (obj.numero, obj.baja, obj.pk))

    def baja_objeto(self, obj):
        """
        Obtiene el id del objeto para dar una baja lógica en el registro co-
        rrespondiente en la base de datos.
        :param obj: object 
        :return: bool
        """
        sql = 'UPDATE telefonos SET baja = ? WHERE id = ?'
        return self.actualizar(sql, (1, obj.pk))

    def relacionar_telefono(self, obj_tel, obj_duenio):
        """
        Relaciona el teléfono a su propietario.
        :param obj: object 
        :return: bool
        """
        data = (obj_tel.pk, obj_duenio.pk_persona, 0)
        if isinstance(obj_duenio, Persona):
            sql = 'INSERT INTO telefonos_de_personas VALUES (null, ?, ?, ?)'
        if isinstance(obj_duenio, Sucursal):
            sql = 'INSERT INTO telefonos_de_sucursales VALUES (null, ?, ?, ?)'
        if isinstance(obj_duenio, LaboratorioExterno):
            sql = 'INSERT INTO telefonos_de_labs_externos VALUES (null, ?, ' \
                  '?, ?)'
        self.salvar(sql, data)

    def obtener_relacionados(self, pk_duenio, tipo):
        """
                Relaciona el teléfono a su propietario.
                :param obj: object 
                :return: bool
                """
        if tipo == "persona":
            sql = 'SELECT telefonos.id, numero FROM telefonos LEFT JOIN ' \
                  'telefonos_de_personas ON telefonos.id = ' \
                  'telefonos_de_personas.telefonoId WHERE ' \
                  'telefonos_de_personas.personaId=? AND telefonos.baja=0'

        if tipo == "sucursal":
            sql = 'SELECT telefonos.id, numero FROM telefonos LEFT JOIN ' \
                  'telefonos_de_sucursales ON telefonos.id = ' \
                  'telefonos_de_sucursales.telefonoId WHERE ' \
                  'telefonos_de_sucursales.personaId=? AND telefonos.baja=0'

        if tipo == "laboratorio":
            sql = 'SELECT telefonos.id, numero FROM telefonos LEFT JOIN ' \
                  'telefonos_de_labs_externos ON telefonos.id = ' \
                  'telefonos_de_labs_externos.telefonoId WHERE ' \
                  'telefonos_de_labs_externos.personaId=? AND telefonos.baja=0'

        return self.obtener(sql=sql, data=(pk_duenio,), lista=True)