# -*- coding: utf-8 -*-
from persistencia.peranalisis import PerAnalisis


class ReservaAnalisis(object):
    def __init__(self, pk, obj_institucion, conformado, obj_examen, obj_fecha):
        self.pk = pk
        self.obj_institucion = obj_institucion
        self.conformado = conformado
        self.obj_examen = obj_examen
        self.obj_fecha = obj_fecha

    def salvar(self):
        self.pk = PerAnalisis().salvar()
        return True

    def actualizar(self):
        return PerAnalisis().actualizar_objeto(self)

    def dar_baja(self):
        return PerAnalisis().baja_objeto(self)

    def __unicode__(self):
        return u"{} {}, CI: {}: Activo: {}".format(
            self.nombres, self.apellidos, self.obj_documento.numero,
            self.activo)