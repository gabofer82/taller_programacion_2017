# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'abm_sucursal.ui'
#
# Created: Tue Nov  7 08:48:35 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_abm_sucursal(object):
    def setupUi(self, abm_sucursal):
        abm_sucursal.setObjectName("abm_sucursal")
        abm_sucursal.resize(640, 480)
        self.verticalLayout = QtGui.QVBoxLayout(abm_sucursal)
        self.verticalLayout.setObjectName("verticalLayout")
        self.form_layout = QtGui.QFormLayout()
        self.form_layout.setObjectName("form_layout")
        self.lbl_domicilio = QtGui.QLabel(abm_sucursal)
        self.lbl_domicilio.setObjectName("lbl_domicilio")
        self.form_layout.setWidget(0, QtGui.QFormLayout.LabelRole, self.lbl_domicilio)
        self.txt_domicilio = QtGui.QLineEdit(abm_sucursal)
        self.txt_domicilio.setObjectName("txt_domicilio")
        self.form_layout.setWidget(0, QtGui.QFormLayout.FieldRole, self.txt_domicilio)
        self.lbl_telefono = QtGui.QLabel(abm_sucursal)
        self.lbl_telefono.setObjectName("lbl_telefono")
        self.form_layout.setWidget(1, QtGui.QFormLayout.LabelRole, self.lbl_telefono)
        self.hlyt_telefonos = QtGui.QHBoxLayout()
        self.hlyt_telefonos.setObjectName("hlyt_telefonos")
        self.txt_telefono = QtGui.QLineEdit(abm_sucursal)
        self.txt_telefono.setObjectName("txt_telefono")
        self.hlyt_telefonos.addWidget(self.txt_telefono)
        self.btn_agregar_telefono = QtGui.QPushButton(abm_sucursal)
        self.btn_agregar_telefono.setObjectName("btn_agregar_telefono")
        self.hlyt_telefonos.addWidget(self.btn_agregar_telefono)
        self.form_layout.setLayout(1, QtGui.QFormLayout.FieldRole, self.hlyt_telefonos)
        self.lbl_ciudad = QtGui.QLabel(abm_sucursal)
        self.lbl_ciudad.setObjectName("lbl_ciudad")
        self.form_layout.setWidget(2, QtGui.QFormLayout.LabelRole, self.lbl_ciudad)
        self.cbox_ciudad = QtGui.QComboBox(abm_sucursal)
        self.cbox_ciudad.setObjectName("cbox_ciudad")
        self.form_layout.setWidget(2, QtGui.QFormLayout.FieldRole, self.cbox_ciudad)
        self.verticalLayout.addLayout(self.form_layout)
        self.hlyt_botones = QtGui.QHBoxLayout()
        self.hlyt_botones.setObjectName("hlyt_botones")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlyt_botones.addItem(spacerItem)
        self.btn_limpiar = QtGui.QPushButton(abm_sucursal)
        self.btn_limpiar.setObjectName("btn_limpiar")
        self.hlyt_botones.addWidget(self.btn_limpiar)
        self.btn_baja = QtGui.QPushButton(abm_sucursal)
        self.btn_baja.setObjectName("btn_baja")
        self.hlyt_botones.addWidget(self.btn_baja)
        self.btn_actualizar = QtGui.QPushButton(abm_sucursal)
        self.btn_actualizar.setObjectName("btn_actualizar")
        self.hlyt_botones.addWidget(self.btn_actualizar)
        self.btn_agregar = QtGui.QPushButton(abm_sucursal)
        self.btn_agregar.setObjectName("btn_agregar")
        self.hlyt_botones.addWidget(self.btn_agregar)
        self.verticalLayout.addLayout(self.hlyt_botones)
        self.table_sucursales = QtGui.QTableView(abm_sucursal)
        self.table_sucursales.setObjectName("table_sucursales")
        self.verticalLayout.addWidget(self.table_sucursales)
        self.buttonBox = QtGui.QDialogButtonBox(abm_sucursal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(abm_sucursal)
        QtCore.QMetaObject.connectSlotsByName(abm_sucursal)

    def retranslateUi(self, abm_sucursal):
        abm_sucursal.setWindowTitle(QtGui.QApplication.translate("abm_sucursal", "Administrar Sucursales", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_domicilio.setText(QtGui.QApplication.translate("abm_sucursal", "Domicilio", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_telefono.setText(QtGui.QApplication.translate("abm_sucursal", "Teléfono/s", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_agregar_telefono.setText(QtGui.QApplication.translate("abm_sucursal", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_ciudad.setText(QtGui.QApplication.translate("abm_sucursal", "Ciudad", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_limpiar.setText(QtGui.QApplication.translate("abm_sucursal", "Limpiar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_baja.setText(QtGui.QApplication.translate("abm_sucursal", "Dar Baja", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_actualizar.setText(QtGui.QApplication.translate("abm_sucursal", "Actualizar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_agregar.setText(QtGui.QApplication.translate("abm_sucursal", "Agregar", None, QtGui.QApplication.UnicodeUTF8))

