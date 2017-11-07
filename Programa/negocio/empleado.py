# -*- coding: utf-8 -*-
import operator
from PySide.QtCore import QAbstractTableModel, Qt, SIGNAL

from persona import Persona
from persistencia.perempleado import PerEmpleado


class Empleado(Persona):
    def __init__(self, pk, pk_persona, tipo, nombres, apellidos,
                 domicilio, obj_documento, obj_ubicacion_geo, col_telefonos,
                 obj_sucursal, baja=False):
        self.pk = pk
        self.tipo = tipo
        self.obj_sucursal = obj_sucursal
        self.baja = baja
        super(Empleado, self).__init__(pk_persona, nombres, apellidos,
                                       col_telefonos, domicilio, obj_documento,
                                       obj_ubicacion_geo)

    def salvar(self):
        super(Empleado, self).salvar()
        self.pk = PerEmpleado().agregar_objeto(self)
        return True

    def actualizar(self):
        super(Empleado, self).actualizar()
        return PerEmpleado().actualizar_objeto(self)

    def dar_baja(self):
        super(Empleado, self).dar_baja()
        return PerEmpleado().baja_objeto(self)

    # def __str__(self):
    #     return unicode(self).encode("utf-8")

    def __unicode__(self):
        return u"{} {}, CI: {}: Activo: {}".format(
            self.nombres, self.apellidos, self.obj_documento.numero,
            self.activo)


class ModeloTablaEmpleados(QAbstractTableModel):
    def __init__(self, parent, dataset, *args):
        super(ModeloTablaEmpleados, self).__init__(parent, *args)
        self.dataset = self.adaptador_dataset(dataset)
        self.headers = [u'ID', u'Tipo', u'Documento', u'Nombres', u'Apellidos',
                        u'Teléfono', u'Domicilio']

    def adaptador_dataset(self, dataset):
        new_dataset = []
        for k, v in dataset.iteritems():
            # temp = (v.obj_documento.numero, v.nombres, v.apellidos,
            #         v.telefonos[0], v)
            temp = (v.pk, v.obj_documento.tipo, v.obj_documento.numero,
                    v.nombres, v.apellidos, v.col_telefonos[0].numero,
                    v.domicilio, v)
            new_dataset.append(temp)

        return new_dataset

    def rowCount(self, *args, **kwargs):
        return len(self.dataset)

    def columnCount(self, *args, **kwargs):
        """
        Estructura del dataset
        [
        (data1, data2, data3,),
        (data1, data2, data3,),
        (data1, data2, data3,)
        ]
        :param args: 
        :param kwargs: 
        :return: 
        """
        return len(self.dataset[0])

    def data(self, index, role, *args, **kwargs):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
        return self.dataset[index.row()][index.column()]

    def get_object(self, index):
        return self.dataset[index.row()][-1]

    def headerData(self, col, orientation, role, *args, **kwargs):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            if len(self.headers) > col:
                return self.headers[col]
            else:
                return None

    def sort(self, col, order, *args, **kwargs):
        """sort table by given column number col"""
        self.emit(SIGNAL("layoutAboutToBeChanged()"))
        self.dataset = sorted(self.dataset,
                             key=operator.itemgetter(col))
        if order == Qt.DescendingOrder:
            self.mylist.reverse()
        self.emit(SIGNAL("layoutChanged()"))
