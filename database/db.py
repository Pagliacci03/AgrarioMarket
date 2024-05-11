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