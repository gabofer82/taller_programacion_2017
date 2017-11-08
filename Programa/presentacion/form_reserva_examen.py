# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reserva_examen.ui'
#
# Created: Tue Nov  7 18:24:28 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from negocio.api import Acceder
from form_abm_paciente import FormPacienteABM


class UIReservaExamen(object):
    def setupUi(self, dlg_reserva):
        dlg_reserva.setObjectName("dlg_reserva")
        dlg_reserva.resize(640, 523)
        self.verticalLayout_5 = QtGui.QVBoxLayout(dlg_reserva)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.hlyt_columnas_formulario = QtGui.QHBoxLayout()
        self.hlyt_columnas_formulario.setObjectName("hlyt_columnas_formulario")
        self.vlyt_paciente = QtGui.QVBoxLayout()
        self.vlyt_paciente.setObjectName("vlyt_paciente")
        self.grid_lyt_paciente_arriba = QtGui.QGridLayout()
        self.grid_lyt_paciente_arriba.setObjectName("grid_lyt_paciente_arriba")
        self.cbox_examen = QtGui.QComboBox(dlg_reserva)
        self.cbox_examen.setObjectName("cbox_examen")
        self.grid_lyt_paciente_arriba.addWidget(self.cbox_examen, 3, 1, 1, 1)
        self.chkbox_conformado = QtGui.QCheckBox(dlg_reserva)
        self.chkbox_conformado.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.chkbox_conformado.setObjectName("chkbox_conformado")
        self.grid_lyt_paciente_arriba.addWidget(self.chkbox_conformado, 2, 1, 1, 1)
        self.lbl_institucion_referente = QtGui.QLabel(dlg_reserva)
        self.lbl_institucion_referente.setObjectName("lbl_institucion_referente")
        self.grid_lyt_paciente_arriba.addWidget(self.lbl_institucion_referente, 0, 0, 1, 1)
        self.cbox_institucion_referente = QtGui.QComboBox(dlg_reserva)
        self.cbox_institucion_referente.setObjectName("cbox_institucion_referente")
        self.grid_lyt_paciente_arriba.addWidget(self.cbox_institucion_referente, 0, 1, 1, 1)
        self.lbl_examen = QtGui.QLabel(dlg_reserva)
        self.lbl_examen.setObjectName("lbl_examen")
        self.grid_lyt_paciente_arriba.addWidget(self.lbl_examen, 3, 0, 1, 1)
        self.btn_agregar_institucion = QtGui.QPushButton(dlg_reserva)
        self.btn_agregar_institucion.setObjectName("btn_agregar_institucion")
        self.grid_lyt_paciente_arriba.addWidget(self.btn_agregar_institucion, 1, 1, 1, 1)
        self.vlyt_paciente.addLayout(self.grid_lyt_paciente_arriba)
        self.vlyt_datos_paciente = QtGui.QVBoxLayout()
        self.vlyt_datos_paciente.setObjectName("vlyt_datos_paciente")
        self.lbl_activo = QtGui.QLabel(dlg_reserva)
        font = QtGui.QFont()
        font.setItalic(True)
        self.lbl_activo.setFont(font)
        self.lbl_activo.setStyleSheet("color: green")
        self.lbl_activo.setObjectName("lbl_activo")
        self.vlyt_datos_paciente.addWidget(self.lbl_activo)
        self.lbl_nombre_completo = QtGui.QLabel(dlg_reserva)
        self.lbl_nombre_completo.setObjectName("lbl_nombre_completo")
        self.vlyt_datos_paciente.addWidget(self.lbl_nombre_completo)
        self.lbl_tipo_nro_documento = QtGui.QLabel(dlg_reserva)
        self.lbl_tipo_nro_documento.setObjectName("lbl_tipo_nro_documento")
        self.vlyt_datos_paciente.addWidget(self.lbl_tipo_nro_documento)
        self.lbl_penalizado = QtGui.QLabel(dlg_reserva)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lbl_penalizado.setFont(font)
        self.lbl_penalizado.setStyleSheet("color: red")
        self.lbl_penalizado.setObjectName("lbl_penalizado")
        self.vlyt_datos_paciente.addWidget(self.lbl_penalizado)
        self.vlyt_paciente.addLayout(self.vlyt_datos_paciente)
        self.btn_buscar = QtGui.QLineEdit(dlg_reserva)
        self.btn_buscar.setText("")
        #self.btn_buscar.setClearButtonEnabled(True)
        self.btn_buscar.setObjectName("btn_buscar")
        self.vlyt_paciente.addWidget(self.btn_buscar)
        self.tblview_pacientes = QtGui.QTableView(dlg_reserva)
        self.tblview_pacientes.setObjectName("tblview_pacientes")
        self.vlyt_paciente.addWidget(self.tblview_pacientes)
        self.hlyt_btn_nuevo_paciente = QtGui.QHBoxLayout()
        self.hlyt_btn_nuevo_paciente.setObjectName("hlyt_btn_nuevo_paciente")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlyt_btn_nuevo_paciente.addItem(spacerItem)
        self.btn_nuevo_paciente = QtGui.QPushButton(dlg_reserva)
        self.btn_nuevo_paciente.setObjectName("btn_nuevo_paciente")
        self.hlyt_btn_nuevo_paciente.addWidget(self.btn_nuevo_paciente)
        self.vlyt_paciente.addLayout(self.hlyt_btn_nuevo_paciente)
        self.hlyt_columnas_formulario.addLayout(self.vlyt_paciente)
        self.vlyt_fecha = QtGui.QVBoxLayout()
        self.vlyt_fecha.setObjectName("vlyt_fecha")
        self.vlyt_calendario = QtGui.QVBoxLayout()
        self.vlyt_calendario.setObjectName("vlyt_calendario")
        self.lbl_fecha_hora_seleccionada = QtGui.QLabel(dlg_reserva)
        self.lbl_fecha_hora_seleccionada.setObjectName("lbl_fecha_hora_seleccionada")
        self.vlyt_calendario.addWidget(self.lbl_fecha_hora_seleccionada)
        self.cal_fecha = QtGui.QCalendarWidget(dlg_reserva)
        self.cal_fecha.setObjectName("cal_fecha")
        self.vlyt_calendario.addWidget(self.cal_fecha)
        self.hlyt_hora = QtGui.QHBoxLayout()
        self.hlyt_hora.setObjectName("hlyt_hora")
        self.lbl_hora = QtGui.QLabel(dlg_reserva)
        self.lbl_hora.setObjectName("lbl_hora")
        self.hlyt_hora.addWidget(self.lbl_hora)
        self.spin_hora = QtGui.QSpinBox(dlg_reserva)
        self.spin_hora.setMinimum(1)
        self.spin_hora.setMaximum(24)
        self.spin_hora.setObjectName("spin_hora")
        self.hlyt_hora.addWidget(self.spin_hora)
        self.spin_minutos = QtGui.QSpinBox(dlg_reserva)
        self.spin_minutos.setMaximum(59)
        self.spin_minutos.setSingleStep(15)
        self.spin_minutos.setObjectName("spin_minutos")
        self.hlyt_hora.addWidget(self.spin_minutos)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlyt_hora.addItem(spacerItem1)
        self.vlyt_calendario.addLayout(self.hlyt_hora)
        self.vlyt_fecha.addLayout(self.vlyt_calendario)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vlyt_fecha.addItem(spacerItem2)
        self.hlyt_columnas_formulario.addLayout(self.vlyt_fecha)
        self.verticalLayout_5.addLayout(self.hlyt_columnas_formulario)
        self.btnbox_ok_cancel = QtGui.QDialogButtonBox(dlg_reserva)
        self.btnbox_ok_cancel.setOrientation(QtCore.Qt.Horizontal)
        self.btnbox_ok_cancel.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.btnbox_ok_cancel.setObjectName("btnbox_ok_cancel")
        self.verticalLayout_5.addWidget(self.btnbox_ok_cancel)

        self.retranslateUi(dlg_reserva)
        QtCore.QObject.connect(self.btnbox_ok_cancel, QtCore.SIGNAL("accepted()"), dlg_reserva.accept)
        QtCore.QObject.connect(self.btnbox_ok_cancel, QtCore.SIGNAL("rejected()"), dlg_reserva.reject)
        QtCore.QMetaObject.connectSlotsByName(dlg_reserva)

    def retranslateUi(self, dlg_reserva):
        dlg_reserva.setWindowTitle(QtGui.QApplication.translate("dlg_reserva", "Reserva de Exámen", None, QtGui.QApplication.UnicodeUTF8))
        self.chkbox_conformado.setText(QtGui.QApplication.translate("dlg_reserva", "Conformado", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_institucion_referente.setText(QtGui.QApplication.translate("dlg_reserva", "Institución Referente", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_examen.setText(QtGui.QApplication.translate("dlg_reserva", "Exámen", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_agregar_institucion.setText(QtGui.QApplication.translate("dlg_reserva", "Agregar Institución", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_activo.setText(QtGui.QApplication.translate("dlg_reserva", "Activo", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_nombre_completo.setText(QtGui.QApplication.translate("dlg_reserva", "Nombre Completo", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_tipo_nro_documento.setText(QtGui.QApplication.translate("dlg_reserva", "Tipo y numero documento", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_penalizado.setText(QtGui.QApplication.translate("dlg_reserva", "Penalizado", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_buscar.setPlaceholderText(QtGui.QApplication.translate("dlg_reserva", "Buscar...", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_nuevo_paciente.setText(QtGui.QApplication.translate("dlg_reserva", "Agregar Nuevo Paciente", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_fecha_hora_seleccionada.setText(QtGui.QApplication.translate("dlg_reserva", "Fecha y hora seleccionada", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_hora.setText(QtGui.QApplication.translate("dlg_reserva", "Hora", None, QtGui.QApplication.UnicodeUTF8))


class FormReservaExamen(QtGui.QDialog, UIReservaExamen):
    def __init__(self, parent=None):
        super(FormReservaExamen, self).__init__(parent)

        # settings del formulario
        self.setupUi(self)
        self.obj_reserva = None
        self.obj_paciente = None
        self.lbl_activo.setText("")
        self.lbl_tipo_nro_documento.setText("")
        self.lbl_nombre_completo.setText("")
        self.lbl_penalizado.setText("")
        # acciones previas del formulario
        self.conectarEventos()
        self.cargarComboBoxExamenes()
        self.cargarComboBoxInstituciones()
        self.cargar_tabla()
        # self._obj_articulo_buscado = None

    ########################################################
    #                     CONECTORES                       #
    ########################################################
    def conectarEventos(self):
        self.tblview_pacientes.doubleClicked.connect(self.handlerCargarLabels)
        self.btn_agregar_institucion.clicked.connect(self.handlerNuevaInstitucion)
        self.btn_nuevo_paciente.clicked.connect(self.handlerNuevoPaciente)

    ########################################################
    #                 MANEJADORES EVENTOS                  #
    ########################################################
    def handlerNuevaInstitucion(self):
        msgBox = QtGui.QMessageBox()
        msgBox.setIcon(QtGui.QMessageBox.Warning)
        msgBox.setWindowTitle(u"No implementado")
        msgBox.setText(u"Lo sentimos. Función no implementada aun.")
        # QtCore.QTimer.singleShot(2000, msgBox, QtCore.SLOT(u"quit()"))
        msgBox.exec_()

    def handlerNuevoPaciente(self):
        frm_paciente = FormPacienteABM()
        frm_paciente.show()
        frm_paciente.exec_()
        self.cargar_tabla()

    def handlerCargarLabels(self):
        print "tabla doble cliqueada"
        index = self.tblview_pacientes.selectedIndexes()[0]
        self.obj_paciente = self.tblview_pacientes.model().get_object(index)
        self.lbl_nombre_completo.setText(u"{} {}".format(self.obj_paciente.nombres,
                                         self.obj_paciente.apellidos))
        self.lbl_tipo_nro_documento.setText(u"{}: {}".format(
            self.obj_paciente.obj_documento.tipo,
            self.obj_paciente.obj_documento.numero))
        if self.obj_paciente.penalizado:
            self.lbl_penalizado.setText("Penalizado")

        if self.obj_paciente.activo:
            self.lbl_activo.setText("Activo")

    def handlerLimpiarClicked(self):
        pass

    def handlerAgregarReserva(self):
        pass

    def handlerFilaSeleccionada(self):
        pass

    ########################################################
    #                     UTILIDADES                       #
    ########################################################
    def cargarComboBoxInstituciones(self):
        for item in Acceder.get_instituciones_medicas().itervalues():
            self.cbox_institucion_referente.addItem(u"{}".format(item.nombre), item)

    def cargarComboBoxExamenes(self):
        examenes = ["Hemograma completo", "Perfil triode: TSH, T3, T4",
                    "Heces por parásito, sangre oculta"]
        for item in examenes:
            self.cbox_examen.addItem(item, item)

    def validarFormulario(self):
        flag_valido = True

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
        self.tblview_pacientes.setModel(Acceder.get_table_model_pacientes(
            parent=self))

    def limpiar_campos(self):
        self.lbl_activo.setText("")
        self.lbl_nombre_completo.setText("")
        self.lbl_tipo_nro_documento.setText("")
        self.lbl_penalizado.setText("")
        self.spin_hora.setValue(1)
        self.spin_minutos.setValue(0)
        # self.cal_fecha.
        self.cbox_institucion_referente.setCurrentIndex(0)
        self.cbox_examen.setCurrentIndex(0)
        self.table_personal.clearSelection()

        self.obj_reserva = None