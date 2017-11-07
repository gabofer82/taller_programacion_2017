# -*- coding: utf-8 -*-
from persistencia.pertelefono import PerTelefono


class Telefono(object):
    def __init__(self, pk, numero, baja=False):
        self.pk = pk
        self.numero = numero
        self.baja = baja

    def salvar(self, obj_duenio):
        self.pk = PerTelefono().agregar_objeto(self)
        PerTelefono().relacionar_telefono(self, obj_duenio)
        return True

    def actualizar(self):
        PerTelefono().actualizar_objeto(self)
        return True

    def dar_baja(self):
        self.baja = True
        return PerTelefono().baja_objeto(self)
