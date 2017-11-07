from negocio.api import Creador
from .basededatos import BaseDeDatos


class PerInstitucionMedica(BaseDeDatos):

    def obtener_uno(self, id_):
        """
        Obtiene y retorna un objeto según el id dado.
        :param id_: int >= 0
        :return: object
        """
        if id_ >= 0:
            id_ = (id_,)
            sql = 'SELECT * FROM instituciones_medicas WHERE id=?'
            fila = self.obtener(sql, id_)
            return Creador.sucursal(id_=fila[0], nombre=fila[1], baja=fila[2])
        else:
            print 'El parámetro debe ser mayor o igual a 0.'
            return None

    def obtener_listado(self, **kwargs):
        """
        Obtiene y retorna un listado de objetos según los filtros pasados.
        :param kwargs: dict 
        :return: dict
        """
        if 'pagina' in kwargs:
            total_filas = self.contar_filas('instituciones_medicas')
            offset = kwargs['pagina'] * 10  #resultados por pagina
            if offset < total_filas:  # TODO: ver aca el asunto de paginacion
                sql = 'SELECT * FROM instituciones_medicas LIMIT(10) OFFSET(?)'
                data = (offset,)
                lista_de_filas = self.obtener(sql, data, True)
                return lista_de_filas
            return None
        else:
            return None

    def agregar_objeto(self, obj):
        """
        Prepara los datos de un objeto para ser insertado en la base de datos.
        :param obj: object
        :return: object
        """
        sql = 'INSERT INTO instituciones_medicas VALUES (null, ?, ?)'
        id_ = self.salvar(sql, (obj.nombre, obj.baja,))
        obj.id_ = id_
        return obj

    def actualizar_objeto(self, obj):
        """
        Prepara los datos de un objeto para actualizar su registro correlativo 
        en la base de datos.
        :param obj: object
        :return: bool
        """
        sql = 'UPDATE instituciones_medicas SET nombre = ?, baja = ? WHERE \
              id = ?'
        return self.actualizar(sql, (obj.nombre, obj.baja))

    def baja_objeto(self, obj):
        """
        Obtiene el id del objeto para dar una baja lógica en el registro co-
        rrespondiente en la base de datos.
        :param obj: object 
        :return: bool
        """
        sql = 'UPDATE instituciones_medicas SET baja = ? WHERE id = ?'
        return self.actualizar(sql, (1, obj.id_))
