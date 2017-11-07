# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'abm_sucursal.ui'
#
# Created: Tue Nov  7 08:48:35 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from negocio.api import Acceder


class UISucursalABM(object):
    def setupUi(self, abm_sucursal):
        abm_sucursal.setObjectName("abm_sucursal")
        abm_sucursal.resize(640, 480)
        self.vlyt_formulario = QtGui.QVBoxLayout(abm_sucursal)
        self.vlyt_formulario.setObjectName("verticalLayout_2")
        self.lyt_form = QtGui.QFormLayout()
        self.lyt_form.setObjectName("lyt_form")
        self.lbl_domicilio = QtGui.QLabel(abm_sucursal)
        self.lbl_domicilio.setObjectName("lbl_domicilio")
        self.lyt_form.setWidget(0, QtGui.QFormLayout.LabelRole,
                                self.lbl_domicilio)
        self.txt_domicilio = QtGui.QLineEdit(abm_sucursal)
        self.txt_domicilio.setObjectName("txt_domicilio")
        self.lyt_form.setWidget(0, QtGui.QFormLayout.FieldRole,
                                self.txt_domicilio)
        self.lbl_telefono = QtGui.QLabel(abm_sucursal)
        self.lbl_telefono.setObjectName("lbl_telefono")
        self.lyt_form.setWidget(1, QtGui.QFormLayout.LabelRole,
                                self.lbl_telefono)
        self.vlyt_contenedor_telefonos = QtGui.QVBoxLayout()
        self.vlyt_contenedor_telefonos.setObjectName(
            "vlyt_contenedor_telefonos")
        self.hlyt_telefono = QtGui.QHBoxLayout()
        self.hlyt_telefono.setObjectName("hlyt_telefono")
        self.txt_telefono = QtGui.QLineEdit(abm_sucursal)
        self.txt_telefono.setObjectName("txt_telefono")
        self.hlyt_telefono.addWidget(self.txt_telefono)
        self.btn_agregar_telefono = QtGui.QPushButton(abm_sucursal)
        self.btn_agregar_telefono.setObjectName("btn_agregar_telefono")
        self.hlyt_telefono.addWidget(self.btn_agregar_telefono)
        self.vlyt_contenedor_telefonos.addLayout(self.hlyt_telefono)
        self.lyt_form.setLayout(1, QtGui.QFormLayout.FieldRole,
                                self.vlyt_contenedor_telefonos)
        self.lbl_ciudad = QtGui.QLabel(abm_sucursal)
        self.lbl_ciudad.setObjectName("lbl_ciudad")
        self.lyt_form.setWidget(2, QtGui.QFormLayout.LabelRole,
                                self.lbl_ciudad)
        self.cbox_ciudad = QtGui.QComboBox(abm_sucursal)
        self.cbox_ciudad.setObjectName("cbox_ciudad")
        self.lyt_form.setWidget(2, QtGui.QFormLayout.FieldRole,
                                self.cbox_ciudad)
        self.vlyt_formulario.addLayout(self.lyt_form)
        self.hlyt_botones = QtGui.QHBoxLayout()
        self.hlyt_botones.setObjectName("hlyt_botones")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding,
                                       QtGui.QSizePolicy.Minimum)
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
        self.vlyt_formulario.addLayout(self.hlyt_botones)
        self.lbl_visualizar_ficha = QtGui.QLabel(abm_sucursal)
        self.lbl_visualizar_ficha.setObjectName("lbl_visualizar_ficha")
        self.vlyt_formulario.addWidget(self.lbl_visualizar_ficha)
        self.table_sucursales = QtGui.QTableView(abm_sucursal)
        self.table_sucursales.setObjectName("table_sucursales")
        self.vlyt_formulario.addWidget(self.table_sucursales)
        self.btnbox_ok_cancel = QtGui.QDialogButtonBox(abm_sucursal)
        self.btnbox_ok_cancel.setStandardButtons(
            QtGui.QDialogButtonBox.Cancel | QtGui.QDialogButtonBox.Ok)
        self.btnbox_ok_cancel.setObjectName("btnbox_ok_cancel")
        self.vlyt_formulario.addWidget(self.btnbox_ok_cancel)

        self.retranslateUi(abm_sucursal)
        QtCore.QMetaObject.connectSlotsByName(abm_sucursal)

    def retranslateUi(self, abm_sucursal):
        abm_sucursal.setWindowTitle(
            QtGui.QApplication.translate("abm_sucursal",
                                         "Administrar Sucursales", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.lbl_domicilio.setText(
            QtGui.QApplication.translate("abm_sucursal", "Domicilio *", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.lbl_telefono.setText(
            QtGui.QApplication.translate("abm_sucursal", "Teléfono/s * (1)",
                                         None, QtGui.QApplication.UnicodeUTF8))
        self.btn_agregar_telefono.setText(
            QtGui.QApplication.translate("abm_sucursal", "+", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.lbl_ciudad.setText(
            QtGui.QApplication.translate("abm_sucursal", "Ciudad *", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.btn_limpiar.setText(
            QtGui.QApplication.translate("abm_sucursal", "Limpiar", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.btn_baja.setText(
            QtGui.QApplication.translate("abm_sucursal", "Dar Baja", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.btn_actualizar.setText(
            QtGui.QApplication.translate("abm_sucursal", "Actualizar", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.btn_agregar.setText(
            QtGui.QApplication.translate("abm_sucursal", "Agregar", None,
                                         QtGui.QApplication.UnicodeUTF8))


class FormSucursalABM(QtGui.QDialog, UISucursalABM):
    def __init__(self, parent=None):
        super(FormSucursalABM, self).__init__(parent)

        # settings del formulario
        self.numero_telefonos = 1
        self.col_telefonos = []  # finalidad: referenciar las cajas de texto.
        self.col_bloques_telefonos = {}
        self.setupUi(self)
        self.table_sucursales.setSelectionBehavior(
            QtGui.QAbstractItemView.SelectRows)
        header_id = self.table_sucursales.horizontalHeader()
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
        self.obj_sucursal = None
        # acciones previas del formulario
        self.conectarEventos()
        self.cargarComboBoxCiudades()
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
        self.table_sucursales.doubleClicked.connect(self.handlerCargarCampos)
        # self.table_sucursales.clicked.connect(self.handlerFilaSeleccionada)
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
            self.vlyt_contenedor_telefonos.addLayout(hlyt_telefono)
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
        if self.obj_sucursal:
            msgBox = QtGui.QMessageBox()
            msgBox.setIcon(QtGui.QMessageBox.Warning)
            msgBox.setWindowTitle(u"Atención")
            msgBox.setText(u"Relamente desea dar de baja esta sucursal?")
            msgBox.setStandardButtons(
                QtGui.QMessageBox.Yes | QtGui.QMessageBox.Discard |
                QtGui.QMessageBox.Cancel)
            msgBox.setDefaultButton(QtGui.QMessageBox.Discard)
            resp = msgBox.exec_()
            if resp == QtGui.QMessageBox.Yes:
                self.obj_sucursal.baja = True
                Acceder.baja_sucursal(obj_sucursal=self.obj_sucursal)
                self.limpiar_campos()
                self.cargar_tabla()

    def handlerActualizarClicked(self):
            for widget_tel in self.col_telefonos:
                obj_tel = widget_tel.obj_tel
                obj_tel.numero = widget_tel.text()

            self.obj_sucursal.domicilio = self.txt_domicilio.text()
            self.obj_sucursal.obj_ubicacion_geo = self.cbox_ciudad.itemData(
                self.cbox_ciudad.currentIndex())
            Acceder.actualizar_sucursal(obj_sucursal=self.obj_sucursal)

            msgBox = QtGui.QMessageBox()
            msgBox.setIcon(QtGui.QMessageBox.Warning)
            msgBox.setWindowTitle(u"Éxito")
            msgBox.setText(u"Sucursal actualizada.")
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
            telefonos = []  # para agregar a los datos de creacion del paciente
            for tel in self.col_telefonos:
                telefonos.append(tel.text())  # tel es un qlineedit

            domicilio = self.txt_domicilio.text()
            obj_ubicacion_geo = self.cbox_ciudad.itemData(
                self.cbox_ciudad.currentIndex())
            Acceder.nueva_sucursal(pk=None, col_telefonos=telefonos,
                                   domicilio=domicilio,
                                   obj_ubicacion_geo=obj_ubicacion_geo, baja=0)
            msgBox = QtGui.QMessageBox()
            msgBox.setIcon(QtGui.QMessageBox.Warning)
            msgBox.setWindowTitle(u"Éxito")
            msgBox.setText(u"Sucursal añadida a la base de datos del sistema.")
            # QtCore.QTimer.singleShot(2000, msgBox, QtCore.SLOT(u"quit()"))
            msgBox.exec_()
            self.limpiar_campos()
            self.cargar_tabla()

    def handlerCargarCampos(self):
        print "tabla doble cliqueada"
        self.btn_agregar.setEnabled(False)
        self.btn_actualizar.setEnabled(True)
        self.btn_baja.setEnabled(True)
        index = self.table_sucursales.selectedIndexes()[0]
        obj = self.table_sucursales.model().get_object(index)
        self.cargar_campos(obj)

    def handlerFilaSeleccionada(self):
        print "tabla cliqueada"
        self.btn_baja.setEnabled(True)
        sind = self.table_sucursales.selectedIndexes()
        index = self.table_sucursales.selectedIndexes()[0]
        obj = self.table_sucursales.model().get_object(index)
        # self.cargar_campos(obj)

    ########################################################
    #                     UTILIDADES                       #
    ########################################################
    def cargarComboBoxCiudades(self):
        for item in Acceder.get_ubicaciones_geograficas() \
                .itervalues():
            self.cbox_ciudad.addItem(u"{}, {}".format(
                item.ciudad, item.departamento.upper()), item)

    def cargar_campos(self, obj):
        self.limpiar_campos()
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

        index = self.cbox_ciudad.findText(u"{}, {}".format(
            obj.obj_ubicacion_geo.ciudad,
            obj.obj_ubicacion_geo.departamento.upper()),
            QtCore.Qt.MatchFixedString)
        self.cbox_ciudad.setCurrentIndex(index)
        self.obj_sucursal = obj

    def validarFormulario(self):
        flag_valido = True
        if len(self.txt_domicilio.text()) < 1:
            flag_valido = False
        if len(self.col_telefonos[0].text()) < 1:
            # eliminar el widget
            flag_valido = False
        if self.cbox_ciudad.currentIndex() < 0:
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
        self.table_sucursales.setModel(Acceder.get_table_model_sucursales(
            parent=self))

    def limpiar_campos(self):
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
        self.table_sucursales.clearSelection()
        self.obj_sucursal = None

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
        self.vlyt_contenedor_telefonos.addLayout(hlyt_telefono)
        btn_agregar_telefono.nombre_bloque = "tel_{}".format(
            self.numero_telefonos)
        self.col_bloques_telefonos[btn_agregar_telefono.nombre_bloque] = \
            hlyt_telefono
        self.numero_telefonos += 1

