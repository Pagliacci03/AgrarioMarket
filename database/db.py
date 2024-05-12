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

def get_product_by_type(type):
    sql = "SELECT TVF.nombre FROM tipo_verdura_fruta TVF, producto_verdura_fruta PVF, producto P WHERE P.id=PVF.product_id AND PVF.tipo_verdura_fruta_id=TVF.id AND P.tipo=%s"
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(sql, (type,))
    conn.commit()
    productos = cursor.fetchall()
    return productos