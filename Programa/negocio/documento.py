# -*- coding: utf-8 -*-
from persistencia.perdocumento import PerDocumento


class Documento(object):
    def __init__(self, pk, tipo, numero, baja=False):
        self.pk = pk
        self.tipo = tipo
        self.numero = numero
        self.baja = baja

    def salvar(self):
        self.pk = PerDocumento().agregar_objeto(self)
        return True

    def actualizar(self):
        PerDocumento().actualizar_objeto(self)
        return True

    def dar_baja(self):
        self.baja = True
        return PerDocumento().baja_objeto(self)
