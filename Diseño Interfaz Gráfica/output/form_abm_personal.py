# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'abm_personal.ui'
#
# Created: Tue Nov  7 12:23:06 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_dlg_abm_paciente(object):
    def setupUi(self, dlg_abm_paciente):
        dlg_abm_paciente.setObjectName("dlg_abm_paciente")
        dlg_abm_paciente.resize(640, 624)
        dlg_abm_paciente.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(dlg_abm_paciente)
        self.verticalLayout.setObjectName("verticalLayout")
        self.glyt_datos = QtGui.QGridLayout()
        self.glyt_datos.setObjectName("glyt_datos")
        self.txt_apellidos = QtGui.QLineEdit(dlg_abm_paciente)
        self.txt_apellidos.setObjectName("txt_apellidos")
        self.glyt_datos.addWidget(self.txt_apellidos, 1, 1, 1, 1)
        self.txt_numero_documento = QtGui.QLineEdit(dlg_abm_paciente)
        self.txt_numero_documento.setObjectName("txt_numero_documento")
        self.glyt_datos.addWidget(self.txt_numero_documento, 2, 1, 1, 1)
        self.lbl_apellidos = QtGui.QLabel(dlg_abm_paciente)
        self.lbl_apellidos.setObjectName("lbl_apellidos")
        self.glyt_datos.addWidget(self.lbl_apellidos, 1, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.glyt_datos.addItem(spacerItem, 0, 2, 1, 1)
        self.lbl_nombres = QtGui.QLabel(dlg_abm_paciente)
        self.lbl_nombres.setObjectName("lbl_nombres")
        self.glyt_datos.addWidget(self.lbl_nombres, 0, 0, 1, 1)
        self.vlyt_telefonos = QtGui.QVBoxLayout()
        self.vlyt_telefonos.setObjectName("vlyt_telefonos")
        self.hlyt_telefono = QtGui.QHBoxLayout()
        self.hlyt_telefono.setObjectName("hlyt_telefono")
        self.txt_telefono = QtGui.QLineEdit(dlg_abm_paciente)
        self.txt_telefono.setObjectName("txt_telefono")
        self.hlyt_telefono.addWidget(self.txt_telefono)
        self.btn_agregar_telefono = QtGui.QPushButton(dlg_abm_paciente)
        self.btn_agregar_telefono.setObjectName("btn_agregar_telefono")
        self.hlyt_telefono.addWidget(self.btn_agregar_telefono)
        self.vlyt_telefonos.addLayout(self.hlyt_telefono)
        self.glyt_datos.addLayout(self.vlyt_telefonos, 3, 1, 1, 1)
        self.lbl_numero_documento = QtGui.QLabel(dlg_abm_paciente)
        self.lbl_numero_documento.setObjectName("lbl_numero_documento")
        self.glyt_datos.addWidget(self.lbl_numero_documento, 2, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.glyt_datos.addItem(spacerItem1, 1, 2, 1, 1)
        self.txt_domicilio = QtGui.QLineEdit(dlg_abm_paciente)
        self.txt_domicilio.setObjectName("txt_domicilio")
        self.glyt_datos.addWidget(self.txt_domicilio, 4, 1, 1, 1)
        self.lbl_ciudad = QtGui.QLabel(dlg_abm_paciente)
        self.lbl_ciudad.setObjectName("lbl_ciudad")
        self.glyt_datos.addWidget(self.lbl_ciudad, 5, 0, 1, 1)
        self.cbox_sucursal = QtGui.QComboBox(dlg_abm_paciente)
        self.cbox_sucursal.setObjectName("cbox_sucursal")
        self.glyt_datos.addWidget(self.cbox_sucursal, 6, 1, 1, 1)
        self.lbl_telefono = QtGui.QLabel(dlg_abm_paciente)
        self.lbl_telefono.setObjectName("lbl_telefono")
        self.glyt_datos.addWidget(self.lbl_telefono, 3, 0, 1, 1)
        self.lbl_domicilio = QtGui.QLabel(dlg_abm_paciente)
        self.lbl_domicilio.setObjectName("lbl_domicilio")
        self.glyt_datos.addWidget(self.lbl_domicilio, 4, 0, 1, 1)
        self.cbox_ciudad = QtGui.QComboBox(dlg_abm_paciente)
        self.cbox_ciudad.setObjectName("cbox_ciudad")
        self.glyt_datos.addWidget(self.cbox_ciudad, 5, 1, 1, 1)
        self.gbox_categoria = QtGui.QGroupBox(dlg_abm_paciente)
        self.gbox_categoria.setObjectName("gbox_categoria")
        self.horizontalLayout = QtGui.QHBoxLayout(self.gbox_categoria)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.chkbox_laboratorista = QtGui.QRadioButton(self.gbox_categoria)
        self.chkbox_laboratorista.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.chkbox_laboratorista.setObjectName("chkbox_laboratorista")
        self.horizontalLayout.addWidget(self.chkbox_laboratorista)
        self.chkbox_administrativo = QtGui.QRadioButton(self.gbox_categoria)
        self.chkbox_administrativo.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.chkbox_administrativo.setChecked(True)
        self.chkbox_administrativo.setObjectName("chkbox_administrativo")
        self.horizontalLayout.addWidget(self.chkbox_administrativo)
        self.glyt_datos.addWidget(self.gbox_categoria, 5, 2, 2, 1)
        self.lbl_sucursal = QtGui.QLabel(dlg_abm_paciente)
        self.lbl_sucursal.setObjectName("lbl_sucursal")
        self.glyt_datos.addWidget(self.lbl_sucursal, 6, 0, 1, 1)
        self.txt_nombres = QtGui.QLineEdit(dlg_abm_paciente)
        self.txt_nombres.setObjectName("txt_nombres")
        self.glyt_datos.addWidget(self.txt_nombres, 0, 1, 1, 1)
        self.gbox_tipo_documento = QtGui.QGroupBox(dlg_abm_paciente)
        self.gbox_tipo_documento.setObjectName("gbox_tipo_documento")
        self.hlyt_tipo_documento = QtGui.QHBoxLayout(self.gbox_tipo_documento)
        self.hlyt_tipo_documento.setObjectName("hlyt_tipo_documento")
        self.rbtn_pasaporte = QtGui.QRadioButton(self.gbox_tipo_documento)
        self.rbtn_pasaporte.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.rbtn_pasaporte.setObjectName("rbtn_pasaporte")
        self.hlyt_tipo_documento.addWidget(self.rbtn_pasaporte)
        self.rbtn_cedula = QtGui.QRadioButton(self.gbox_tipo_documento)
        self.rbtn_cedula.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.rbtn_cedula.setChecked(True)
        self.rbtn_cedula.setObjectName("rbtn_cedula")
        self.hlyt_tipo_documento.addWidget(self.rbtn_cedula)
        self.glyt_datos.addWidget(self.gbox_tipo_documento, 3, 2, 2, 1)
        self.verticalLayout.addLayout(self.glyt_datos)
        self.hlyt_botones_control = QtGui.QHBoxLayout()
        self.hlyt_botones_control.setObjectName("hlyt_botones_control")
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlyt_botones_control.addItem(spacerItem2)
        self.btn_limpiar = QtGui.QPushButton(dlg_abm_paciente)
        self.btn_limpiar.setEnabled(False)
        self.btn_limpiar.setObjectName("btn_limpiar")
        self.hlyt_botones_control.addWidget(self.btn_limpiar)
        self.btn_baja = QtGui.QPushButton(dlg_abm_paciente)
        self.btn_baja.setEnabled(False)
        self.btn_baja.setObjectName("btn_baja")
        self.hlyt_botones_control.addWidget(self.btn_baja)
        self.btn_actualizar = QtGui.QPushButton(dlg_abm_paciente)
        self.btn_actualizar.setEnabled(False)
        self.btn_actualizar.setObjectName("btn_actualizar")
        self.hlyt_botones_control.addWidget(self.btn_actualizar)
        self.btn_agregar = QtGui.QPushButton(dlg_abm_paciente)
        self.btn_agregar.setEnabled(True)
        self.btn_agregar.setObjectName("btn_agregar")
        self.hlyt_botones_control.addWidget(self.btn_agregar)
        self.verticalLayout.addLayout(self.hlyt_botones_control)
        self.lbl_visualizar_ficha = QtGui.QLabel(dlg_abm_paciente)
        self.lbl_visualizar_ficha.setObjectName("lbl_visualizar_ficha")
        self.verticalLayout.addWidget(self.lbl_visualizar_ficha)
        self.table_personal = QtGui.QTableView(dlg_abm_paciente)
        self.table_personal.setObjectName("table_personal")
        self.verticalLayout.addWidget(self.table_personal)
        self.btnbox_ok_cancel = QtGui.QDialogButtonBox(dlg_abm_paciente)
        self.btnbox_ok_cancel.setOrientation(QtCore.Qt.Horizontal)
        self.btnbox_ok_cancel.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.btnbox_ok_cancel.setObjectName("btnbox_ok_cancel")
        self.verticalLayout.addWidget(self.btnbox_ok_cancel)

        self.retranslateUi(dlg_abm_paciente)
        QtCore.QObject.connect(self.btnbox_ok_cancel, QtCore.SIGNAL("accepted()"), dlg_abm_paciente.accept)
        QtCore.QObject.connect(self.btnbox_ok_cancel, QtCore.SIGNAL("rejected()"), dlg_abm_paciente.reject)
        QtCore.QMetaObject.connectSlotsByName(dlg_abm_paciente)

    def retranslateUi(self, dlg_abm_paciente):
        dlg_abm_paciente.setWindowTitle(QtGui.QApplication.translate("dlg_abm_paciente", "Administrar Personal", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_apellidos.setText(QtGui.QApplication.translate("dlg_abm_paciente", "Apellidos *", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_nombres.setText(QtGui.QApplication.translate("dlg_abm_paciente", "Nombres *", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_agregar_telefono.setText(QtGui.QApplication.translate("dlg_abm_paciente", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_numero_documento.setText(QtGui.QApplication.translate("dlg_abm_paciente", "Número de documento *", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_ciudad.setText(QtGui.QApplication.translate("dlg_abm_paciente", "Ciudad *", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_telefono.setText(QtGui.QApplication.translate("dlg_abm_paciente", "Teléfono * (1)", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_domicilio.setText(QtGui.QApplication.translate("dlg_abm_paciente", "Domicilio", None, QtGui.QApplication.UnicodeUTF8))
        self.gbox_categoria.setTitle(QtGui.QApplication.translate("dlg_abm_paciente", "Permisos", None, QtGui.QApplication.UnicodeUTF8))
        self.chkbox_laboratorista.setText(QtGui.QApplication.translate("dlg_abm_paciente", "&Laboratorista", None, QtGui.QApplication.UnicodeUTF8))
        self.chkbox_administrativo.setText(QtGui.QApplication.translate("dlg_abm_paciente", "Administrativo", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_sucursal.setText(QtGui.QApplication.translate("dlg_abm_paciente", "Sucursal *", None, QtGui.QApplication.UnicodeUTF8))
        self.gbox_tipo_documento.setTitle(QtGui.QApplication.translate("dlg_abm_paciente", "Tipo de documento", None, QtGui.QApplication.UnicodeUTF8))
        self.rbtn_pasaporte.setText(QtGui.QApplication.translate("dlg_abm_paciente", "Pasapor&te", None, QtGui.QApplication.UnicodeUTF8))
        self.rbtn_cedula.setText(QtGui.QApplication.translate("dlg_abm_paciente", "Céd&ula", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_limpiar.setText(QtGui.QApplication.translate("dlg_abm_paciente", "Limpiar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_baja.setText(QtGui.QApplication.translate("dlg_abm_paciente", "Dar Baja", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_actualizar.setText(QtGui.QApplication.translate("dlg_abm_paciente", "Actualizar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_agregar.setText(QtGui.QApplication.translate("dlg_abm_paciente", "Agregar", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_visualizar_ficha.setText(QtGui.QApplication.translate("dlg_abm_paciente", "Doble click para visualizar ficha", None, QtGui.QApplication.UnicodeUTF8))

