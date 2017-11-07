# -*- coding: utf-8 -*-
from persistencia.perubicaciongeografica import PerUbicacion

class UbicacionGeografica(object):
    def __init__(self, pk, ciudad, departamento, baja):
        self.pk = pk
        self.ciudad = ciudad
        self.departamento = departamento
        self.baja = baja

    def salvar(self):
        self.pk = PerUbicacion().agregar_objeto(self)
        return True

    def __str__(self):
        return "{}: {}, {}".format(self.pk, self.ciudad, self.departamento)
