# -*- coding: utf-8 -*-


class FichaPaciente(object):
    def __init__(self, pk, obj_reserva, obj_analisis, baja=False):
        self.pk = pk
        self.obj_reserva = obj_reserva
        self.obj_analisis = obj_analisis
        self.baja = baja