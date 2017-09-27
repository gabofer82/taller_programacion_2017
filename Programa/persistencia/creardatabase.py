from basededatos import BaseDeDatos


class CreadorDataBase:
    """
    Encargada de crear la base de datos para el sistema.
    """
    def __init__(self):
        self._ruta_sql_inicio = 'schema.sql'
        self._data_base = BaseDeDatos()
        try:
            archivo = open(self._ruta_sql_inicio, 'r')
            script_sql = archivo.read()  # retorna un objeto string
            archivo.close()

            print 'Creando base de datos...'
            self._data_base.ejecutar_script_inicio(script_sql)
            print 'Base de datos creada.'
        except Exception as e:
            print e.message


if __name__ == '__main__':
    CreadorDataBase()
