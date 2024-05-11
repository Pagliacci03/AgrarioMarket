import pymysql

DB_NAME = "tarea2"
DB_USERNAME = "cc5002"
DB_PASSWORD = "programacionweb"
DB_HOST = "localhost"
DB_PORT = 3306
DB_CHARSET = "utf8"


# --- Connection ---

def get_conn():
    conn = pymysql.connect(
        db=DB_NAME,
        user=DB_USERNAME,
        passwd=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        charset=DB_CHARSET
    )
    return conn

def get_producto():
    sql = "SELECT id, tipo, descripcion, comuna_id, nombre_productor, email_productor, celular_productor FROM producto ORDER BY id DESC"
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    productos = cursor.fetchall()
    return productos

def get_name_by_id_product(id):
    sql = "SELECT TVF.nombre FROM tipo_verdura_fruta TVF, producto_verdura_fruta PVF WHERE TVF.id=PVF.tipo_verdura_fruta_id AND PVF.producto_id=%s"
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(sql, (id,))
    conn.commit()
    product_names = cursor.fetchall()
    return product_names

def get_region_by_id_comuna(id):
    sql = "SELECT REG.nombre FROM region REG, comuna COM WHERE REG.id = COM.region_id AND COM.id=%s"
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(sql, (id,))
    conn.commit()
    region = cursor.fetchall()
    return region

def get_comuna_by_id(id):
    sql = "SELECT nombre FROM comuna WHERE COM.id=%s"
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(sql, (id,))
    conn.commit()
    comuna = cursor.fetchall()
    return comuna

def get_foto_by_id_product(id):
    sql = "SELECT ruta_archivo, nombre_archivo FROM foto WHERE producto_id=%s"
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(sql, (id,))
    conn.commit()
    fotos = cursor.fetchall()
    return fotos