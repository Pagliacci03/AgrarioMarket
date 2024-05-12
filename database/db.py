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

def get_regiones():
    sql = "SELECT nombre FROM region"
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    regiones = cursor.fetchall()
    return regiones

def get_comunas_by_region(region):
    sql = "SELECT C.nombre FROM region R, comuna C WHERE R.id=C.region_id AND R.nombre=%s"
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(sql, (region,))
    conn.commit()
    comunas = cursor.fetchall()
    return comunas