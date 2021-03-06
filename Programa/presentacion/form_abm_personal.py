# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'abm_personal.ui'
#
# Created: Tue Nov  7 12:23:06 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from negocio.api import Acceder


class UIPersonalABM(object):
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
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding,
                                       QtGui.QSizePolicy.Minimum)
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
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding,
                                        QtGui.QSizePolicy.Minimum)
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
        self.rbtn_laboratorista = QtGui.QRadioButton(self.gbox_categoria)
        self.rbtn_laboratorista.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.rbtn_laboratorista.setObjectName("chkbox_laboratorista")
        self.horizontalLayout.addWidget(self.rbtn_laboratorista)
        self.rbtn_administrativo = QtGui.QRadioButton(self.gbox_categoria)
        self.rbtn_administrativo.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.rbtn_administrativo.setChecked(True)
        self.rbtn_administrativo.setObjectName("chkbox_administrativo")
        self.horizontalLayout.addWidget(self.rbtn_administrativo)
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
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding,
                                        QtGui.QSizePolicy.Minimum)
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
        self.btnbox_ok_cancel.setStandardButtons(
            QtGui.QDialogButtonBox.Cancel | QtGui.QDialogButtonBox.Ok)
        self.btnbox_ok_cancel.setObjectName("btnbox_ok_cancel")
        self.verticalLayout.addWidget(self.btnbox_ok_cancel)

        self.retranslateUi(dlg_abm_paciente)
        QtCore.QObject.connect(self.btnbox_ok_cancel,
                               QtCore.SIGNAL("accepted()"),
                               dlg_abm_paciente.accept)
        QtCore.QObject.connect(self.btnbox_ok_cancel,
                               QtCore.SIGNAL("rejected()"),
                               dlg_abm_paciente.reject)
        QtCore.QMetaObject.connectSlotsByName(dlg_abm_paciente)

    def retranslateUi(self, dlg_abm_paciente):
        dlg_abm_paciente.setWindowTitle(
            QtGui.QApplication.translate("dlg_abm_paciente",
                                         "Administrar Personal", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.lbl_apellidos.setText(
            QtGui.QApplication.translate("dlg_abm_paciente", "Apellidos *",
                                         None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_nombres.setText(
            QtGui.QApplication.translate("dlg_abm_paciente", "Nombres *", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.btn_agregar_telefono.setText(
            QtGui.QApplication.translate("dlg_abm_paciente", "+", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.lbl_numero_documento.setText(
            QtGui.QApplication.translate("dlg_abm_paciente",
                                         "Número de documento *", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.lbl_ciudad.setText(
            QtGui.QApplication.translate("dlg_abm_paciente", "Ciudad *", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.lbl_telefono.setText(
            QtGui.QApplication.translate("dlg_abm_paciente", "Teléfono * (1)",
                                         None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_domicilio.setText(
            QtGui.QApplication.translate("dlg_abm_paciente", "Domicilio", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.gbox_categoria.setTitle(
            QtGui.QApplication.translate("dlg_abm_paciente", "Permisos", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.rbtn_laboratorista.setText(
            QtGui.QApplication.translate("dlg_abm_paciente", "&Laboratorista",
                                         None, QtGui.QApplication.UnicodeUTF8))
        self.rbtn_administrativo.setText(
            QtGui.QApplication.translate("dlg_abm_paciente", "Administrativo",
                                         None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_sucursal.setText(
            QtGui.QApplication.translate("dlg_abm_paciente", "Sucursal *",
                                         None, QtGui.QApplication.UnicodeUTF8))
        self.gbox_tipo_documento.setTitle(
            QtGui.QApplication.translate("dlg_abm_paciente",
                                         "Tipo de documento", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.rbtn_pasaporte.setText(
            QtGui.QApplication.translate("dlg_abm_paciente", "Pasapor&te",
                                         None, QtGui.QApplication.UnicodeUTF8))
        self.rbtn_cedula.setText(
            QtGui.QApplication.translate("dlg_abm_paciente", "Céd&ula", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.btn_limpiar.setText(
            QtGui.QApplication.translate("dlg_abm_paciente", "Limpiar", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.btn_baja.setText(
            QtGui.QApplication.translate("dlg_abm_paciente", "Dar Baja", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.btn_actualizar.setText(
            QtGui.QApplication.translate("dlg_abm_paciente", "Actualizar",
                                         None, QtGui.QApplication.UnicodeUTF8))
        self.btn_agregar.setText(
            QtGui.QApplication.translate("dlg_abm_paciente", "Agregar", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.lbl_visualizar_ficha.setText(
            QtGui.QApplication.translate("dlg_abm_paciente",
                                         "Doble click para visualizar ficha",
                                         None, QtGui.QApplication.UnicodeUTF8))


class FormPersonalABM(QtGui.QDialog, UIPersonalABM):
    def __init__(self, parent=None):
        super(FormPersonalABM, self).__init__(parent)

        # settings del formulario
        self.numero_telefonos = 1
        self.col_telefonos = []  # finalidad: referenciar las cajas de texto.
        self.col_bloques_telefonos = {}
        self.setupUi(self)
        self.table_personal.setSelectionBehavior(
            QtGui.QAbstractItemView.SelectRows)
        header_id = self.table_personal.horizontalHeader()
        header_id.setResizeMode(0, QtGui.QHeaderView.Stretch)
        self.btn_agregar_telefono.accion = "agregar"
        self.btn_agregar_telefono.nombre_bloque = "tel_0"
        self.col_bloques_telefonos[self.btn_agregar_telefono.nombre_bloque] = \
            self.hlyt_telefono
        self.col_telefonos.append(self.txt_telefono)
        self.btn_actualizar.setEnabled(False)
        self.btn_baja.setEnabled(False)
        self.btn_agregar.setEnabled(True)
        self.btn_limpiar.setEnabled(False)
        self.obj_personal = None
        # acciones previas del formulario
        self.conectarEventos()
        self.cargarComboBoxCiudades()
        self.cargarComboBoxSucursales()
        self.cargar_tabla()
        # self._obj_articulo_buscado = None

    ########################################################
    #                     CONECTORES                       #
    ########################################################
    def conectarEventos(self):
        # Acciones
        # self.actionSalir.triggered.connect(self.handlerCerrarClicked)
        # Botones
        self.btn_agregar_telefono.clicked.connect(
            lambda: self.handlerAgregarTelefonoClicked(
                self.btn_agregar_telefono))
        self.btn_limpiar.clicked.connect(self.handlerLimpiarClicked)
        self.btn_baja.clicked.connect(self.handlerBajaClicked)
        self.btn_actualizar.clicked.connect(self.handlerActualizarClicked)
        self.btn_agregar.clicked.connect(self.handlerAgregarClicked)
        self.table_personal.doubleClicked.connect(self.handlerCargarCampos)
        # self.table_pacientes.clicked.connect(self.handlerFilaSeleccionada)
        # botones generados dinamicamente
        # for k, btn in self._dict_btn_lineas_facturacion.items():
        #     # print "Conectar: {}".format(btn.text())
        #     btn.clicked.connect(
        #         lambda boton=btn: self.handlerLineaClicked(boton))

    ########################################################
    #                 MANEJADORES EVENTOS                  #
    ########################################################
    def handlerAgregarTelefonoClicked(self, boton_emisor):
        """
        Se encarga de añadir un bloque para un nuevo teléfono.

        :param boton_emisor: QtGui.QPushButton
        :return: None
        """
        btn_agregar_telefono = QtGui.QPushButton(self)
        if boton_emisor.accion == "agregar":
            hlyt_telefono = QtGui.QHBoxLayout()
            hlyt_telefono.setObjectName(
                "hlyt_telefono_{}".format(self.numero_telefonos))
            txt_telefono = QtGui.QLineEdit(self)
            txt_telefono.setObjectName(
                "txt_telefono_{}".format(self.numero_telefonos))
            self.col_telefonos.append(txt_telefono)
            hlyt_telefono.addWidget(txt_telefono)
            btn_agregar_telefono = QtGui.QPushButton(self)
            btn_agregar_telefono.setObjectName(
                "btn_agregar_telefono_{}".format(self.numero_telefonos))
            btn_agregar_telefono.setText(
                QtGui.QApplication.translate("dlg_abm_paciente", "+", None,
                                             QtGui.QApplication.UnicodeUTF8))

            btn_agregar_telefono.accion = "agregar"

            if len(self.col_bloques_telefonos) > 2:
                btn_agregar_telefono.setEnabled(False)

            hlyt_telefono.addWidget(btn_agregar_telefono)
            boton_emisor.setText(
                QtGui.QApplication.translate("dlg_abm_paciente", "-", None,
                                             QtGui.QApplication.UnicodeUTF8))
            boton_emisor.accion = "eliminar"
            btn_agregar_telefono.clicked.connect(
                lambda: self.handlerAgregarTelefonoClicked(
                    btn_agregar_telefono))
            self.vlyt_telefonos.addLayout(hlyt_telefono)
            btn_agregar_telefono.nombre_bloque = "tel_{}".format(
                self.numero_telefonos)
            self.col_bloques_telefonos[btn_agregar_telefono.nombre_bloque] = \
                hlyt_telefono
            self.numero_telefonos += 1
        else:
            layout = self.col_bloques_telefonos[boton_emisor.nombre_bloque]
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    if isinstance(widget, QtGui.QLineEdit):
                        self.col_telefonos.remove(widget)
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())

            del self.col_bloques_telefonos[boton_emisor.nombre_bloque]

            for layout in self.col_bloques_telefonos.itervalues():
                item = layout.itemAt(1)
                if item.widget() is not None:
                    item.widget().setEnabled(True)

    def handlerBajaClicked(self):
        if self.obj_personal:
            msgBox = QtGui.QMessageBox()
            msgBox.setIcon(QtGui.QMessageBox.Warning)
            msgBox.setWindowTitle(u"Atención")
            msgBox.setText(u"Relamente desea dar de baja a {} {}.".format(
                self.obj_personal.nombres, self.obj_personal.apellidos))
            msgBox.setStandardButtons(
                QtGui.QMessageBox.Yes | QtGui.QMessageBox.Discard |
                QtGui.QMessageBox.Cancel)
            msgBox.setDefaultButton(QtGui.QMessageBox.Discard)
            resp = msgBox.exec_()
            if resp == QtGui.QMessageBox.Yes:
                self.obj_personal.baja = True
                Acceder.baja_personal(obj_empleado=self.obj_personal)
                self.limpiar_campos()
                self.cargar_tabla()

    def handlerActualizarClicked(self):
        if self.validarFormulario() and self.obj_personal:
            self.obj_personal.nombres = self.txt_nombres.text()
            self.obj_personal.apellidos = self.txt_apellidos.text()
            self.obj_personal.obj_documento.numero = \
                self.txt_numero_documento.text()
            if self.rbtn_cedula.isChecked():
                self.obj_personal.obj_documento.tipo = u"cédula"
            else:
                self.obj_personal.obj_documento.tipo = u"pasaporte"

            if self.rbtn_administrativo.isChecked():
                self.obj_personal.tipo = u"administrativo"
            else:
                self.obj_personal.tipo = u"laboratorista"

            for widget_tel in self.col_telefonos:
                obj_tel = widget_tel.obj_tel
                obj_tel.numero = widget_tel.text()

            self.obj_personal.domicilio = self.txt_domicilio.text()
            self.obj_personal.obj_ubicacion_geo = self.cbox_ciudad.itemData(
                self.cbox_ciudad.currentIndex())
            self.obj_personal.obj_sucursal = self.cbox_sucursal.itemData(
                self.cbox_sucursal.currentIndex())
            Acceder.actualizar_personal(obj_empleado=self.obj_personal)

            msgBox = QtGui.QMessageBox()
            msgBox.setIcon(QtGui.QMessageBox.Warning)
            msgBox.setWindowTitle(u"Éxito")
            msgBox.setText(u"Empleado actualizado.")
            msgBox.exec_()

            self.limpiar_campos()
            self.btn_actualizar.setEnabled(False)
            self.btn_baja.setEnabled(False)
            self.btn_agregar.setEnabled(True)
            self.cargar_tabla()

    def handlerLimpiarClicked(self):
        self.btn_actualizar.setEnabled(False)
        self.btn_baja.setEnabled(False)
        self.btn_agregar.setEnabled(True)
        self.limpiar_campos()
        self.cargar_tabla()

    def handlerAgregarClicked(self):
        if self.validarFormulario():
            nombres = self.txt_nombres.text()
            apellidos = self.txt_apellidos.text()
            numero_documento = self.txt_numero_documento.text()
            if self.rbtn_cedula.isChecked():
                tipo_documento = u"cédula"
            else:
                tipo_documento = u"pasaporte"

            if self.rbtn_administrativo:
                tipo_empleado = u"administrativo"
            else:
                tipo_empleado = u"laboratorista"

            telefonos = []  # para agregar a los datos de creacion del paciente
            for tel in self.col_telefonos:
                telefonos.append(tel.text())  # tel es un qlineedit

            domicilio = self.txt_domicilio.text()
            obj_ubicacion_geo = self.cbox_ciudad.itemData(
                self.cbox_ciudad.currentIndex())
            obj_sucursal = self.cbox_sucursal.itemData(
                self.cbox_sucursal.currentIndex())
            Acceder.nuevo_personal(accion=u"alta", nombres=nombres,
                                   apellidos=apellidos,
                                   numero_documento=numero_documento,
                                   tipo_documento=tipo_documento,
                                   tipo_empleado=tipo_empleado,
                                   obj_sucursal=obj_sucursal,
                                   col_telefonos=telefonos,
                                   domicilio=domicilio,
                                   obj_ubicacion_geo=obj_ubicacion_geo,
                                   baja=0, pk=None, pk_persona=None)
            msgBox = QtGui.QMessageBox()
            msgBox.setIcon(QtGui.QMessageBox.Warning)
            msgBox.setWindowTitle(u"Éxito")
            msgBox.setText(u"Empleado añadido a la base de datos del sistema.")
            # QtCore.QTimer.singleShot(2000, msgBox, QtCore.SLOT(u"quit()"))
            msgBox.exec_()
            self.limpiar_campos()
            self.cargar_tabla()

    def handlerCargarCampos(self):
        print "tabla doble cliqueada"
        self.btn_agregar.setEnabled(False)
        self.btn_actualizar.setEnabled(True)
        self.btn_baja.setEnabled(True)
        index = self.table_personal.selectedIndexes()[0]
        obj = self.table_personal.model().get_object(index)
        self.cargar_campos(obj)

    def handlerFilaSeleccionada(self):
        print "tabla cliqueada"
        self.btn_baja.setEnabled(True)
        sind = self.table_pacientes.selectedIndexes()
        index = self.table_pacientes.selectedIndexes()[0]
        obj = self.table_pacientes.model().get_object(index)
        # self.cargar_campos(obj)

    ########################################################
    #                     UTILIDADES                       #
    ########################################################
    def cargarComboBoxCiudades(self):
        for item in Acceder.get_ubicaciones_geograficas() \
                .itervalues():
            self.cbox_ciudad.addItem(u"{}, {}".format(
                item.ciudad, item.departamento.upper()), item)

    def cargarComboBoxSucursales(self):
        for item in Acceder.get_sucursales().itervalues():
            self.cbox_sucursal.addItem(u"{}, {} ({})".format(
                item.domicilio, item.obj_ubicacion_geo.ciudad,
                item.obj_ubicacion_geo.departamento.upper()), item)

    def cargar_campos(self, obj):
        self.limpiar_campos()
        self.txt_nombres.setText(obj.nombres)
        self.txt_apellidos.setText(obj.apellidos)
        self.txt_numero_documento.setText(obj.obj_documento.numero)
        if obj.obj_documento.tipo == "pasaporte":
            self.rbtn_pasaporte.setChecked(True)
            self.rbtn_cedula.setChecked(False)
        else:
            self.rbtn_cedula.setChecked(True)
            self.rbtn_pasaporte.setChecked(False)

        if obj.tipo == "administrativo":
            self.rbtn_administrativo.setChecked(True)
            self.rbtn_laboratorista.setChecked(False)
        else:
            self.rbtn_laboratorista.setChecked(True)
            self.rbtn_administrativo.setChecked(False)

        l = len(obj.col_telefonos)
        i = 1
        for tel in obj.col_telefonos:
            if i == 1:
                self.col_telefonos[0].setText(tel.numero)
                self.col_telefonos[0].obj_tel = tel
                if l != 1:
                    self.btn_agregar_telefono.accion = "quitar"
                    self.btn_agregar_telefono.setText(
                        QtGui.QApplication.translate("dlg_abm_paciente", "-",
                                                     None,
                                                     QtGui.QApplication.UnicodeUTF8))
                i += 1
                continue
            elif i == l:
                self.agregar_telefono(tel, True)
                break
            self.agregar_telefono(tel, False)
            i += 1

        self.txt_domicilio.setText(obj.domicilio)
        # cbox ciudad
        index = self.cbox_ciudad.findText(u"{}, {}".format(
            obj.obj_ubicacion_geo.ciudad,
            obj.obj_ubicacion_geo.departamento.upper()),
            QtCore.Qt.MatchFixedString)
        self.cbox_ciudad.setCurrentIndex(index)
        # cbox sucursal
        index = self.cbox_sucursal.findText(u"{}, {} ({})".format(
            obj.obj_sucursal.domicilio,
            obj.obj_sucursal.obj_ubicacion_geo.ciudad,
            obj.obj_sucursal.obj_ubicacion_geo.departamento.upper()),
            QtCore.Qt.MatchFixedString)
        self.cbox_sucursal.setCurrentIndex(index)
        self.obj_personal = obj

    def validarFormulario(self):
        flag_valido = True
        if len(self.txt_nombres.text()) < 1:
            flag_valido = False
        if len(self.txt_apellidos.text()) < 1:
            flag_valido = False
        if len(self.txt_numero_documento.text()) < 1:
            flag_valido = False
        if len(self.col_telefonos[0].text()) < 1:
            # eliminar el widget
            flag_valido = False
        if self.cbox_ciudad.currentIndex() < 0:
            flag_valido = False
        if self.cbox_sucursal.currentIndex() < 0:
            flag_valido = False
        if not flag_valido:
            msgBox = QtGui.QMessageBox()
            msgBox.setIcon(QtGui.QMessageBox.Warning)
            msgBox.setWindowTitle(u"Atención...")
            msgBox.setText(
                "Los campos marcados con asterisco (*) son obligatorios")
            # QtCore.QTimer.singleShot(2000, msgBox, QtCore.SLOT(u"quit()"))
            msgBox.exec_()
            return False
        else:
            return True

    def cargar_tabla(self):
        self.table_personal.setModel(Acceder.get_table_model_personal(
            parent=self))

    def limpiar_campos(self):
        self.txt_nombres.setText("")
        self.txt_apellidos.setText("")
        self.txt_numero_documento.setText("")
        if not self.rbtn_cedula.isChecked():
            self.rbtn_cedula.setChecked(True)
            # self.rbtn_pasaporte.

        if not self.rbtn_administrativo.isChecked():
            self.rbtn_administrativo.setChecked(True)

        # para que quede uno al menos
        largo = len(self.col_bloques_telefonos)
        contador = 1
        bloque_remanente = None
        for layout in self.col_bloques_telefonos.itervalues():
            contador += 1
            if largo < contador:
                bloque_remanente = layout
                break
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())

        self.col_bloques_telefonos = {}  # vacio los bloques de telefonos
        self.col_telefonos = []  # vacio los telefonos
        nombre_bloque = None
        widget = bloque_remanente.itemAt(0).widget()
        if isinstance(widget, QtGui.QLineEdit):
            widget.setText("")
            self.col_telefonos.append(widget)  # un QLineEdit
        widget = bloque_remanente.itemAt(1).widget()
        if isinstance(widget, QtGui.QPushButton):
            widget.setText(QtGui.QApplication.translate("dlg_abm_paciente",
                                                        "+", None,
                                                        QtGui.QApplication.UnicodeUTF8))
            widget.accion = "agregar"
            nombre_bloque = widget.nombre_bloque

        self.col_bloques_telefonos[nombre_bloque] = bloque_remanente

        self.txt_domicilio.setText("")
        self.cbox_ciudad.setCurrentIndex(0)
        self.table_personal.clearSelection()

        self.obj_personal = None

    def agregar_telefono(self, obj_tel, flag):
        """
        Se encarga de añadir un bloque para un nuevo teléfono con texto.

        :param texto: str
        :return: None
        """
        btn_agregar_telefono = QtGui.QPushButton(self)
        hlyt_telefono = QtGui.QHBoxLayout()
        hlyt_telefono.setObjectName(
            "hlyt_telefono_{}".format(self.numero_telefonos))
        txt_telefono = QtGui.QLineEdit(self)
        txt_telefono.setText(obj_tel.numero)
        txt_telefono.setObjectName(
            "txt_telefono_{}".format(self.numero_telefonos))
        txt_telefono.obj_tel = obj_tel
        self.col_telefonos.append(txt_telefono)
        hlyt_telefono.addWidget(txt_telefono)
        btn_agregar_telefono = QtGui.QPushButton(self)
        btn_agregar_telefono.setObjectName(
            "btn_agregar_telefono_{}".format(self.numero_telefonos))
        if flag:
            btn_agregar_telefono.setText(
                QtGui.QApplication.translate("dlg_abm_paciente", "+", None,
                                             QtGui.QApplication.UnicodeUTF8))
            btn_agregar_telefono.accion = "agregar"
        else:
            btn_agregar_telefono.setText(
                QtGui.QApplication.translate("dlg_abm_paciente", "-", None,
                                             QtGui.QApplication.UnicodeUTF8))
            btn_agregar_telefono.accion = "quitar"

        if len(self.col_bloques_telefonos) > 2:
            btn_agregar_telefono.setEnabled(False)

        hlyt_telefono.addWidget(btn_agregar_telefono)
        btn_agregar_telefono.clicked.connect(
            lambda: self.handlerAgregarTelefonoClicked(
                btn_agregar_telefono))
        self.vlyt_telefonos.addLayout(hlyt_telefono)
        btn_agregar_telefono.nombre_bloque = "tel_{}".format(
            self.numero_telefonos)
        self.col_bloques_telefonos[btn_agregar_telefono.nombre_bloque] = \
            hlyt_telefono
        self.numero_telefonos += 1

