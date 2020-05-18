from psycopg2 import connect, Error
from errores import escribir_errores

############## CONEXION Y CIERRE CON BD ##############
class Conexion:

    bd: None
    cursor = None

    def __init__(self, **parametros):
        try:
            self.db = connect(
                host=parametros['direccion_servidor'],
                user=parametros['usuario'],
                password=parametros['contrasena'],
                database=parametros['base_datos'] 
            )
            self.cursor = self.db.cursor()
        except Error as e:
            escribir_errores(e, "Ocurrio un Error al conectar con la Base de Datos")

############## EJECUTAR SENTENCIAS SQL ##############
    def _ejecutar_sql(
        self, sentencia_sql, parametros=None, 
        escribir_en_db=True
    ):
        try:
            self.cursor.execute(sentencia_sql, parametros) # execute corre las sentencias sql
            if escribir_en_db:
                self.db.commit()
        except Exception as e:
             escribir_errores(e, f"Ocurrio un error al ejecutar la sentencia SQL:\n\n{sentencia_sql}\n")
        if escribir_en_db:
                self.db.rollback()

############## LECTOR DE CODIGO SQL ##############
    def _leer_desde_sql(self):
        try:
            registros = self.cursor.fetchall()
            for x in registros:
                print(x)
        except Exception as e:
            escribir_errores(e, f'Un error ocurrió al momento de leer desde la BD')
        return registros

############## CREAR TABLAS  ##############
    def crear_tabla(self):
        self._ejecutar_sql(
            """
            CREATE TABLE frutas_verduras (
                codigo_articulo SERIAL,
                nombre_articulo VARCHAR(50) NOT NULL,
                fecha TIMESTAMP,
                cantidad INT,
                precio DECIMAL,
                PRIMARY KEY (codigo_articulo)
            )
            """
        )

        self._ejecutar_sql(
            """
            CREATE TABLE carnes (
                codigo_articulo SERIAL,
                nombre_articulo VARCHAR(50) NOT NULL,
                fecha TIMESTAMP,
                cantidad INT,
                precio DECIMAL,
                PRIMARY KEY (codigo_articulo)
            )
            """
        )

        self._ejecutar_sql(
            """
            CREATE TABLE congelados (
                codigo_articulo SERIAL,
                nombre_articulo VARCHAR(50) NOT NULL,
                fecha TIMESTAMP,
                cantidad INT,
                precio DECIMAL,
                PRIMARY KEY (codigo_articulo)
            )
            """
        )

        self._ejecutar_sql(
            """
            CREATE TABLE lacteos (
                codigo_articulo SERIAL,
                nombre_articulo VARCHAR(50) NOT NULL,
                fecha TIMESTAMP,
                cantidad INT,
                precio DECIMAL,
                PRIMARY KEY (codigo_articulo)
            )
            """
        )
        
        self._ejecutar_sql(
            """
            CREATE TABLE quesos (
                codigo_articulo SERIAL,
                nombre_articulo VARCHAR(50) NOT NULL,
                fecha TIMESTAMP,
                cantidad INT,
                precio DECIMAL,
                PRIMARY KEY (codigo_articulo)
            )
            """
        )

        self._ejecutar_sql(
            """
            CREATE TABLE abarrotes (
                codigo_articulo SERIAL,
                nombre_articulo VARCHAR(50) NOT NULL,
                fecha TIMESTAMP,
                cantidad INT,
                precio DECIMAL,
                PRIMARY KEY (codigo_articulo)
            )
            """
        )

        self._ejecutar_sql(
            """
            CREATE TABLE bebidas (
                codigo_articulo SERIAL,
                nombre_articulo VARCHAR(50) NOT NULL,
                fecha TIMESTAMP,
                cantidad INT,
                precio DECIMAL,
                PRIMARY KEY (codigo_articulo)
            )
            """
        )

        self._ejecutar_sql(
            """
            CREATE TABLE panaderia (
                codigo_articulo SERIAL,
                nombre_articulo VARCHAR(50) NOT NULL,
                fecha TIMESTAMP,
                cantidad INT,
                precio DECIMAL,
                PRIMARY KEY (codigo_articulo)
            )
            """
        )

        self._ejecutar_sql(
            """
            CREATE TABLE cuidado_personal (
                codigo_articulo SERIAL,
                nombre_articulo VARCHAR(50) NOT NULL,
                fecha TIMESTAMP,
                cantidad INT,
                precio DECIMAL,
                PRIMARY KEY (codigo_articulo)
            )
            """
        )

        self._ejecutar_sql(
            """
            CREATE TABLE limpieza (
                codigo_articulo SERIAL,
                nombre_articulo VARCHAR(50) NOT NULL,
                fecha TIMESTAMP,
                cantidad INT,
                precio DECIMAL,
                PRIMARY KEY (codigo_articulo)
            )
            """
        )

        self._ejecutar_sql(
            """
            CREATE TABLE mascotas (
                codigo_articulo SERIAL,
                nombre_articulo VARCHAR(50) NOT NULL,
                fecha TIMESTAMP,
                cantidad INT,
                precio DECIMAL,
                PRIMARY KEY (codigo_articulo)
            )
            """
        )

        self._ejecutar_sql(
            """
            CREATE TABLE productos (
                codigo_articulo SERIAL,
                nombre_articulo VARCHAR(50) NOT NULL,
                fecha TIMESTAMP,
                cantidad INT,
                precio DECIMAL,
                PRIMARY KEY (codigo_articulo)
            )
            """
        )

###################### INSERTAR ARTICULOS EN BD ADMINISTRADOR #######################
    def insertar_verduras(self, nombre_articulo, cantidad, precio):
        self._ejecutar_sql(
            """INSERT INTO frutas_verduras (nombre_articulo, fecha, cantidad, precio) 
            VALUES (%s, CURRENT_DATE, %s, %s)""",
            (nombre_articulo, cantidad, precio)
    )

    def insertar_carnes(self, nombre_articulo, cantidad, precio):
        self._ejecutar_sql(
            """INSERT INTO carnes (nombre_articulo, fecha, cantidad, precio) 
            VALUES (%s, CURRENT_DATE, %s, %s)""",
            (nombre_articulo, cantidad, precio)
    )

    def insertar_congelados(self, nombre_articulo, cantidad, precio):
        self._ejecutar_sql(
            """INSERT INTO congelados (nombre_articulo, fecha, cantidad, precio) 
            VALUES (%s, CURRENT_DATE, %s, %s)""",
            (nombre_articulo, cantidad, precio)
    )

    def insertar_lacteos(self, nombre_articulo, cantidad, precio):
        self._ejecutar_sql(
            """INSERT INTO lacteos (nombre_articulo, fecha, cantidad, precio) 
            VALUES (%s, CURRENT_DATE, %s, %s)""",
            (nombre_articulo, cantidad, precio)
    )

    def insertar_quesos(self, nombre_articulo, cantidad, precio):
        self._ejecutar_sql(
            """INSERT INTO quesos (nombre_articulo, fecha, cantidad, precio) 
            VALUES (%s, CURRENT_DATE, %s, %s)""",
            (nombre_articulo, cantidad, precio)
    )

    def insertar_abarrotes(self, nombre_articulo, cantidad, precio):
        self._ejecutar_sql(
            """INSERT INTO abarrotes (nombre_articulo, fecha, cantidad, precio) 
            VALUES (%s, CURRENT_DATE, %s, %s)""",
            (nombre_articulo, cantidad, precio)
    )

    def insertar_bebidas(self, nombre_articulo, cantidad, precio):
        self._ejecutar_sql(
            """INSERT INTO bebidas (nombre_articulo, fecha, cantidad, precio) 
            VALUES (%s, CURRENT_DATE, %s, %s)""",
            (nombre_articulo, cantidad, precio)
    )

    def insertar_panaderia(self, nombre_articulo, cantidad, precio):
        self._ejecutar_sql(
            """INSERT INTO panaderia (nombre_articulo, fecha, cantidad, precio) 
            VALUES (%s, CURRENT_DATE, %s, %s)""",
            (nombre_articulo, cantidad, precio)
    )

    def insertar_cuidado(self, nombre_articulo, cantidad, precio):
        self._ejecutar_sql(
            """INSERT INTO cuidado_personal (nombre_articulo, fecha, cantidad, precio) 
            VALUES (%s, CURRENT_DATE, %s, %s)""",
            (nombre_articulo, cantidad, precio)
    )

    def insertar_limpieza(self, nombre_articulo, cantidad, precio):
        self._ejecutar_sql(
            """INSERT INTO limpieza (nombre_articulo, fecha, cantidad, precio) 
            VALUES (%s, CURRENT_DATE, %s, %s)""",
            (nombre_articulo, cantidad, precio)
    )

    def insertar_mascotas(self, nombre_articulo, cantidad, precio):
        self._ejecutar_sql(
            """INSERT INTO mascotas (nombre_articulo, fecha, cantidad, precio) 
            VALUES (%s, CURRENT_DATE, %s, %s)""",
            (nombre_articulo, cantidad, precio)
    )

###################### VER LOS ARTICULOS EN BD ADMINISTRADOR #######################
    def ver_articulos(self):
        self._ejecutar_sql(
            """
            SELECT codigo_articulo, nombre_articulo, fecha, cantidad, precio
            FROM frutas_verduras

            UNION

            SELECT codigo_articulo, nombre_articulo, fecha, cantidad, precio
            FROM carnes

            UNION

            SELECT codigo_articulo, nombre_articulo, fecha, cantidad, precio
            FROM congelados

            UNION

            SELECT codigo_articulo, nombre_articulo, fecha, cantidad, precio
            FROM lacteos

            UNION

            SELECT codigo_articulo, nombre_articulo, fecha, cantidad, precio
            FROM quesos

            UNION

            SELECT codigo_articulo, nombre_articulo, fecha, cantidad, precio
            FROM abarrotes

            UNION

            SELECT codigo_articulo, nombre_articulo, fecha, cantidad, precio
            FROM bebidas

            UNION

            SELECT codigo_articulo, nombre_articulo, fecha, cantidad, precio
            FROM panaderia

            UNION

            SELECT codigo_articulo, nombre_articulo, fecha, cantidad, precio
            FROM cuidado_personal

            UNION

            SELECT codigo_articulo, nombre_articulo, fecha, cantidad, precio
            FROM limpieza

            UNION

            SELECT codigo_articulo, nombre_articulo, fecha, cantidad, precio
            FROM mascotas

            ORDER BY fecha DESC;
            """,
            escribir_en_db=False
        )
        self._leer_desde_sql()

    def ver_vegetales(self):
            self._ejecutar_sql(
                "SELECT * FROM fruta_verduras",
                escribir_en_db=False
            )
            self._leer_desde_sql()

    def ver_carnes(self):
            self._ejecutar_sql(
                "SELECT * FROM carnes",
                escribir_en_db=False
            )
            self._leer_desde_sql()

    def ver_congelados(self):
            self._ejecutar_sql(
                "SELECT * FROM congelados",
                escribir_en_db=False
            )
            self._leer_desde_sql()

    def ver_lacteos(self):
            self._ejecutar_sql(
                "SELECT * FROM lacteos",
                escribir_en_db=False
            )
            self._leer_desde_sql()

    def ver_quesos(self):
            self._ejecutar_sql(
                "SELECT * FROM quesos",
                escribir_en_db=False
            )
            self._leer_desde_sql()

    def ver_abarrotes(self):
            self._ejecutar_sql(
                "SELECT * FROM abarrotes",
                escribir_en_db=False
            )
            self._leer_desde_sql()

    def ver_bebidas(self):
            self._ejecutar_sql(
                "SELECT * FROM bebidas",
                escribir_en_db=False
            )
            self._leer_desde_sql()

    def ver_panaderia(self):
            self._ejecutar_sql(
                "SELECT * FROM panaderia",
                escribir_en_db=False
            )
            self._leer_desde_sql()

    def ver_cuidado(self):
            self._ejecutar_sql(
                "SELECT * FROM cuidado_personal",
                escribir_en_db=False
            )
            self._leer_desde_sql()

    def ver_limpieza(self):
            self._ejecutar_sql(
                "SELECT * FROM limpieza",
                escribir_en_db=False
            )
            self._leer_desde_sql()

    def ver_mascotas(self):
            self._ejecutar_sql(
                "SELECT * FROM mascotas",
                escribir_en_db=False
            )
            self._leer_desde_sql()

###################### MODIFICAR LOS ARTICULOS EN BD ADMINISTRADOR #######################
def modificar_verduras(self, nombre_articulo, cantidad, precio, codigo_articulo):
        self._ejecutar_sql(
            """UPDATE frutas_verduras 
            SET nombre_articulo=%s,
                cantidad=%s,
                precio=%s
            WHERE
                codigo_articulo = %s""",
            (nombre_articulo, cantidad, precio, codigo_articulo)
        )

def modificar_carnes(self, nombre_articulo, cantidad, precio, codigo_articulo):
        self._ejecutar_sql(
            """UPDATE carnes 
            SET nombre_articulo=%s,
                cantidad=%s,
                precio=%s
            WHERE
                codigo_articulo = %s""",
            (nombre_articulo, cantidad, precio, codigo_articulo)
        )

def modificar_congelados(self, nombre_articulo, cantidad, precio, codigo_articulo):
        self._ejecutar_sql(
            """UPDATE congelados 
            SET nombre_articulo=%s,
                cantidad=%s,
                precio=%s
            WHERE
                codigo_articulo = %s""",
            (nombre_articulo, cantidad, precio, codigo_articulo)
        )

def modificar_lacteos(self, nombre_articulo, cantidad, precio, codigo_articulo):
        self._ejecutar_sql(
            """UPDATE lacteos 
            SET nombre_articulo=%s,
                cantidad=%s,
                precio=%s
            WHERE
                codigo_articulo = %s""",
            (nombre_articulo, cantidad, precio, codigo_articulo)
        )

def modificar_quesos(self, nombre_articulo, cantidad, precio, codigo_articulo):
        self._ejecutar_sql(
            """UPDATE quesos 
            SET nombre_articulo=%s,
                cantidad=%s,
                precio=%s
            WHERE
                codigo_articulo = %s""",
            (nombre_articulo, cantidad, precio, codigo_articulo)
        )

def modificar_abarrotes(self, nombre_articulo, cantidad, precio, codigo_articulo):
        self._ejecutar_sql(
            """UPDATE abarrotes 
            SET nombre_articulo=%s,
                cantidad=%s,
                precio=%s
            WHERE
                codigo_articulo = %s""",
            (nombre_articulo, cantidad, precio, codigo_articulo)
        )

def modificar_bebidas(self, nombre_articulo, cantidad, precio, codigo_articulo):
        self._ejecutar_sql(
            """UPDATE bebidas 
            SET nombre_articulo=%s,
                cantidad=%s,
                precio=%s
            WHERE
                codigo_articulo = %s""",
            (nombre_articulo, cantidad, precio, codigo_articulo)
        )

def modificar_panaderia(self, nombre_articulo, cantidad, precio, codigo_articulo):
        self._ejecutar_sql(
            """UPDATE panaderia 
            SET nombre_articulo=%s,
                cantidad=%s,
                precio=%s
            WHERE
                codigo_articulo = %s""",
            (nombre_articulo, cantidad, precio, codigo_articulo)
        )

def modificar_cuidado_personal(self, nombre_articulo, cantidad, precio, codigo_articulo):
        self._ejecutar_sql(
            """UPDATE cuidado_pesonal 
            SET nombre_articulo=%s,
                cantidad=%s,
                precio=%s
            WHERE
                codigo_articulo = %s""",
            (nombre_articulo, cantidad, precio, codigo_articulo)
        )

def modificar_limpieza(self, nombre_articulo, cantidad, precio, codigo_articulo):
        self._ejecutar_sql(
            """UPDATE limpieza 
            SET nombre_articulo=%s,
                cantidad=%s,
                precio=%s
            WHERE
                codigo_articulo = %s""",
            (nombre_articulo, cantidad, precio, codigo_articulo)
        )

def modificar_mascotas(self, nombre_articulo, cantidad, precio, codigo_articulo):
        self._ejecutar_sql(
            """UPDATE mascotas 
            SET nombre_articulo=%s,
                cantidad=%s,
                precio=%s
            WHERE
                codigo_articulo = %s""",
            (nombre_articulo, cantidad, precio, codigo_articulo)
        )
