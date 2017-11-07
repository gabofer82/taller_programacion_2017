# -*- coding: utf-8 -*-
from fabrica import Creador
from paciente import Paciente, ModeloTablaPacientes
from documento import Documento
from persistencia.perubicaciongeografica import PerUbicacion
from persistencia.perpaciente import PerPaciente
from persistencia.perpersona import PerPersona
from persistencia.perdocumento import PerDocumento
from persistencia.pertelefono import PerTelefono


class ManejadoraPrincipal(object):
    def __init__(self):
        pass

    def get_ubicaciones_geograficas(self):
        dataset = PerUbicacion().obtener_listado()
        col_ubicaciones = {}
        for fila in dataset:
            obj = Creador.ubicacion_geografica(pk=fila[0], ciudad=fila[1],
                                             departamento=fila[2], baja=[3])
            col_ubicaciones[obj.pk] = obj

        return col_ubicaciones

    def get_ubicacion_geografica(self, pk):
        fila = PerUbicacion.obtener_uno(pk)
        obj_ubicacion = None
        if fila:
            obj_ubicacion = Creador.ubicacion_geografica(pk=fila[0],
                                                         ciudad=fila[1],
                                                         departamento=fila[2],
                                                         baja=[3])
        return obj_ubicacion


class ManejadoraPacientes(object):
    def nuevo_paciente(self, **kwargs):
        if kwargs["accion"] == "alta":
            col_telefonos = []
            for tel in kwargs["col_telefonos"]:
                col_telefonos.append((None, tel))
            # obj_p = Creador.paciente(**kwargs)
            obj_p = Creador.paciente(pk=None, pk_persona=None,
                         activo=kwargs["activo"],
                         penalizado=kwargs["penalizado"],
                         ficha_paciente_id=None, baja=kwargs["baja"],
                         nombres=kwargs["nombres"],
                         apellidos=kwargs["apellidos"],
                         domicilio=kwargs["domicilio"],
                         documento=(None, kwargs["tipo_documento"],
                                    kwargs["numero_documento"]),
                         ubicacion_geo=(kwargs["obj_ubicacion_geo"].pk,
                                        kwargs["obj_ubicacion_geo"].ciudad,
                                        kwargs["obj_ubicacion_geo"].departamento,
                                        kwargs["obj_ubicacion_geo"].baja),
                         col_telefonos=col_telefonos)
            obj_p.salvar()
            return obj_p

    def actualizar_paciente(self, **kwargs):
        obj_p = kwargs["obj_paciente"]
        obj_p.actualizar()
        return obj_p

    def baja_paciente(self, **kwargs):
        obj_p = kwargs["obj_paciente"]
        obj_p.dar_baja()
        return obj_p

    def get_paciente(self, pk):
        data_pac = PerPaciente().obtener_uno(pk)
        data_per = PerPersona().obtener_uno(data_pac[1])
        data_ubigeo = PerUbicacion().obtener_uno(data_per[5])
        data_doc = PerDocumento().obtener_uno(data_per[4])
        data_tels = PerTelefono().obtener_relacionados(data_per[0], "persona")
        return Creador.paciente(pk=data_pac[0], pk_persona=data_pac[1],
                         activo=data_pac[2], penalizado=data_pac[3],
                         ficha_paciente_id=data_pac[4], baja=data_pac[5],
                         nombres=data_per[1], apellidos=data_per[2],
                         domicilio=data_per[3],
                         documento=data_doc,
                         ubicacion_geo=data_ubigeo,
                         col_telefonos=data_tels)

    def get_pacientes(self, **kwargs):
        dataset = PerPaciente().obtener_listado(**kwargs)
        col_pacientes = {}
        if not dataset:
            return col_pacientes
        for data_pac in dataset:
            data_per = PerPersona().obtener_uno(data_pac[1])
            data_ubigeo = PerUbicacion().obtener_uno(data_per[5])
            data_doc = PerDocumento().obtener_uno(data_per[4])
            data_tels = PerTelefono().obtener_relacionados(data_per[0],
                                                         "persona")
            obj = Creador.paciente(pk=data_pac[0], pk_persona=data_pac[1],
                                   activo=data_pac[2], penalizado=data_pac[3],
                                   ficha_paciente_id=data_pac[4],
                                   baja=data_pac[5],
                                   nombres=data_per[1], apellidos=data_per[2],
                                   domicilio=data_per[3],
                                   documento=data_doc,
                                   ubicacion_geo=data_ubigeo,
                                   col_telefonos=data_tels)
            col_pacientes[obj.pk] = obj
        return col_pacientes

    def get_modelo_tabla(self, parent):
        dataset = self.get_pacientes(pagina=1)
        if dataset:
            return ModeloTablaPacientes(parent, dataset)
        else:
            return None
