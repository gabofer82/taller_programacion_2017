# -*- coding: utf-8 -*-
from .agendadiaria import AgendaDiaria
from .analisis import Analisis
from .cupo import Cupo
from .documento import Documento
from .empleado import Empleado
from .fichapaciente import FichaPaciente
from .institucionmedica import InstitucionMedica
from .laboratorioexterno import LaboratorioExterno
from .paciente import Paciente
from .reserva_analisis import ReservaAnalisis
from .sucursal import Sucursal
from .tipoanalisis import TipoAnalisis
from .ubicacion_geografica import UbicacionGeografica


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
        return Documento()

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
        return Paciente()

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
        return UbicacionGeografica()


class Actualizador(object):
    """
    Clase encargada de actualizar el estado de los objetos de la capa.
    
    Note:
        Suministra los métodos necesarios para actualizar los objetos.
        Debe ser invocada de forma estática.
        
    Args:
        Ninguno
        
    Attributes:
        Ninguno
    """
    pass


class Elminador(object):
    """
    Clase encargada de dar baja al estado de los objetos de la capa y eliminar-
    los.

    Note:
        Suministra los métodos necesarios para dar baja a los objetos.
        Debe ser invocada de forma estática.

    Args:
        Ninguno

    Attributes:
        Ninguno
    """
    pass


class Servicio(object):
    """
    Clase encargada de brindar todos los servicios de la capa.

    Note:
        Suministra todos los métodos necesarios.
        Debe ser invocada de forma estática.

    Args:
        Ninguno

    Attributes:
        Ninguno
    """
    pass
