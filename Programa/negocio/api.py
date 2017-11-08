# -*- coding: utf-8 -*-
from .manejadoras import ManejadoraPrincipal, ManejadoraPacientes, \
    ManejadoraSucursales, ManejadoraPersonal


class Acceder(object):
    """
    Clase encargada de nuclear el acceso a cada uno de los objetos de la capa 
    de negocio.
    
    Note:
        Suministra los métodos necesarios para trabajar con la capa como 
        fachada pública de ella.
        Dichos métodos deben ser invocados de forma estática.
        
    Args:
        Ninguno
        
    Attributes:
        Ninguno
    """

    # Personal
    @staticmethod
    def nuevo_personal(**kwargs):
        return ManejadoraPersonal().nuevo_empleado(**kwargs)

    @staticmethod
    def actualizar_personal(**kwargs):
        return ManejadoraPersonal().actualizar_empleado(**kwargs)

    @staticmethod
    def baja_personal(**kwargs):
        return ManejadoraPersonal().baja_empleado(**kwargs)

    @staticmethod
    def get_table_model_personal(**kwargs):
        return ManejadoraPersonal().get_modelo_tabla(kwargs["parent"])

    # Pacientes
    @staticmethod
    def nuevo_paciente(**kwargs):
        return ManejadoraPacientes().nuevo_paciente(**kwargs)

    @staticmethod
    def actualizar_paciente(**kwargs):
        return ManejadoraPacientes().actualizar_paciente(**kwargs)

    @staticmethod
    def baja_paciente(**kwargs):
        return ManejadoraPacientes().baja_paciente(**kwargs)

    @staticmethod
    def get_table_model_pacientes(**kwargs):
        return ManejadoraPacientes().get_modelo_tabla(kwargs["parent"])

    # Sucursales
    @staticmethod
    def nueva_sucursal(**kwargs):
        return ManejadoraSucursales().nueva_sucursal(**kwargs)

    @staticmethod
    def actualizar_sucursal(**kwargs):
        return ManejadoraSucursales().actualizar_sucursal(**kwargs)

    @staticmethod
    def baja_sucursal(**kwargs):
        return ManejadoraSucursales().baja_sucursal(**kwargs)

    @staticmethod
    def get_table_model_sucursales(**kwargs):
        return ManejadoraSucursales().get_modelo_tabla(kwargs["parent"])

    @staticmethod
    def get_sucursales(**kwargs):
        return ManejadoraSucursales().get_sucursales(**kwargs)

    # Ubicaciones geograficas
    @staticmethod
    def get_ubicaciones_geograficas(**kwargs):
        return ManejadoraPrincipal().get_ubicaciones_geograficas(**kwargs)

    # Instituciones medicas
    @staticmethod
    def get_instituciones_medicas(**kwargs):
        return ManejadoraPrincipal().get_instituciones_medicas(**kwargs)



class Actualizador(object): # son responsabilidad de cada clase
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


class Elminador(object):  # son responsabilidad de cada clase
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
