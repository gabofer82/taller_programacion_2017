# -*- coding: utf-8 -*-


class InstitucionMedica(object):
    def __init__(self, pk, nombre, direccion, obj_ubicacion_geo):
        self.pk = pk
        self.nombre = nombre
        self.direccion = direccion
        self.obj_ubicacion_geo = obj_ubicacion_geo