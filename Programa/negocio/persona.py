# -*- coding: utf-8 -*-
from persistencia.perpersona import PerPersona


class Persona(object):
    def __init__(self, pk, nombres, apellidos, col_telefonos, domicilio,
                 obj_documento, obj_ubicacion_geo, baja=False):
        self.pk_persona = pk
        self.nombres = nombres
        self.apellidos = apellidos
        self.col_telefonos = col_telefonos
        self.domicilio = domicilio
        self.obj_documento = obj_documento
        self.obj_ubicacion_geo = obj_ubicacion_geo
        self.baja = baja

    def salvar(self):
        self.obj_documento.salvar()
        self.pk_persona = PerPersona().agregar_objeto(self)
        # self.obj_ubicacion_geo.pk = self.obj_ubicacion_geo.salvar(
        #     self.obj_ubicacion_geo)
        for obj_t in self.col_telefonos:
            obj_t.pk = obj_t.salvar(self)
        return True

    def actualizar(self):
        self.obj_documento.actualizar()
        PerPersona().actualizar_objeto(self)
        for obj_t in self.col_telefonos:
            obj_t.actualizar()
        return True

    def dar_baja(self):
        self.baja = True
        self.obj_documento.dar_baja()
        PerPersona().baja_objeto(self)
        for obj_t in self.col_telefonos:
            obj_t.dar_baja()
        return True