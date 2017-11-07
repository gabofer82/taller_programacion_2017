# -*- coding: utf-8 -*-
from .agendadiaria import AgendaDiaria
from .analisis import Analisis
from .cupo import Cupo
from .documento import Documento
from .empleado import Empleado
from .telefono import Telefono
from .fichapaciente import FichaPaciente
from .institucionmedica import InstitucionMedica
from .laboratorioexterno import LaboratorioExterno
from .reserva_analisis import ReservaAnalisis
from .sucursal import Sucursal
from .tipoanalisis import TipoAnalisis
from .ubicacion_geografica import UbicacionGeografica
from .paciente import Paciente


class Creador(object):
    """
    Clase encargada de crear cada uno de los objetos de la capa de negocio.

    Note:
        Suministra los métodos necesarios para crear.
        Debe ser invocada de forma estática.

    Args:
        Ninguno

    Attributes:
        Ninguno
    """

    @staticmethod
    def agendadiaria(**kwargs):
        return AgendaDiaria()

    @staticmethod
    def analisis(**kwargs):
        return Analisis()

    @staticmethod
    def cupo(**kwargs):
        return Cupo()

    @staticmethod
    def documento(**kwargs):
        return Documento(pk=None, numero=kwargs["numero_documento"],
                         tipo=kwargs["tipo_documento"])

    @staticmethod
    def telefono(**kwargs):
        return Telefono(pk=kwargs["pk"], numero=kwargs["numero"], baja=0)

    @staticmethod
    def empleado(**kwargs):
        return Empleado()

    @staticmethod
    def fichapaciente(**kwargs):
        return FichaPaciente()

    @staticmethod
    def institucionmedica(**kwargs):
        return InstitucionMedica()

    @staticmethod
    def laboratorioexterno(**kwargs):
        return LaboratorioExterno()

    @staticmethod
    def paciente(**kwargs):
        obj_documento = Creador.documento(pk=kwargs["documento"][0],
                                          numero_documento=kwargs["documento"]
                                          [2], tipo_documento=kwargs
                                          ["documento"][1])
        col_telefonos = []
        for tel in kwargs["col_telefonos"]:
            obj_telefono = Creador.telefono(pk=tel[0], numero=tel[1])
            col_telefonos.append(obj_telefono)
        obj_ubicacion_geo = Creador.ubicacion_geografica(
            pk=kwargs["ubicacion_geo"][0], ciudad=kwargs
            ["ubicacion_geo"][1], departamento=kwargs["ubicacion_geo"]
            [2], baja=kwargs["ubicacion_geo"][3])
        # kwargs["obj_ubicacion_geo"] trae un objeto
        return Paciente(pk=kwargs["pk"],
                        pk_persona=kwargs["pk_persona"],
                        activo=True, penalizado=False,
                        nombres=kwargs["nombres"],
                        apellidos=kwargs["apellidos"],
                        col_telefonos=col_telefonos,
                        domicilio=kwargs["domicilio"],
                        obj_documento=obj_documento,
                        obj_ubicacion_geo=obj_ubicacion_geo,
                        obj_ficha_paciente=None, baja=False)

    @staticmethod
    def reserva_analisis(**kwargs):
        return ReservaAnalisis()

    @staticmethod
    def sucursal(**kwargs):
        return Sucursal()

    @staticmethod
    def tipoanalisis(**kwargs):
        return TipoAnalisis()

    @staticmethod
    def ubicacion_geografica(**kwargs):
        return UbicacionGeografica(kwargs['pk'], kwargs['ciudad'],
                                   kwargs['departamento'], kwargs['baja'])