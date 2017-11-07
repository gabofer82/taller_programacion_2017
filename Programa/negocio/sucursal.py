# -*- coding: utf-8 -*-
import operator
from PySide.QtCore import QAbstractTableModel, Qt, SIGNAL

from persistencia.persucursal import PerSucursal


class Sucursal(object):
    def __init__(self, pk, domicilio, col_telefonos, obj_ubicacion_geo,
                 baja=False):
        self.pk = pk
        self.domicilio = domicilio
        self.col_telefonos = col_telefonos
        self.obj_ubicacion_geo = obj_ubicacion_geo
        self.baja = baja

    def salvar(self):
        self.pk = PerSucursal().agregar_objeto(self)
        for obj_t in self.col_telefonos:
            obj_t.pk = obj_t.salvar(self)
        return True

    def actualizar(self):
        PerSucursal().actualizar_objeto(self)
        for obj_t in self.col_telefonos:
            obj_t.actualizar()
        return True

    def dar_baja(self):
        self.baja = True
        PerSucursal().baja_objeto(self)
        for obj_t in self.col_telefonos:
            obj_t.dar_baja()
        return True


class ModeloTablaSucursales(QAbstractTableModel):
    def __init__(self, parent, dataset, *args):
        super(ModeloTablaSucursales, self).__init__(parent, *args)
        self.dataset = self.adaptador_dataset(dataset)
        self.headers = [u'ID', u'Domicilio', u'Teléfono', u'Ciudad',
                        u'Departamento']

    def adaptador_dataset(self, dataset):
        new_dataset = []
        for k, v in dataset.iteritems():
            temp = (v.pk, v.domicilio, v.col_telefonos[0].numero,
                    v.obj_ubicacion_geo.ciudad,
                    v.obj_ubicacion_geo.departamento, v)
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