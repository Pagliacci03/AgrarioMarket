import pymysql

DB_NAME = "tarea2"
DB_USERNAME = "cc5002"
DB_PASSWORD = "programacionweb"
DB_HOST = "localhost"
DB_PORT = 3306
DB_CHARSET = "utf8"


# --- Connexión con la base de datos ---

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


# --- Obtener elementos en la base de datos ---

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

def get_id_comuna_by_nombre(name):
    sql = "SELECT id FROM comuna WHERE nombre=%s"
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(sql, (name,))
    conn.commit()
    id = cursor.fetchall()
    return id

def get_id_tvf_by_nombre(name):
    sql = "SELECT id FROM tipo_verdura_fruta WHERE nombre=%s"
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(sql, (name,))
    conn.commit()
    id = cursor.fetchall()
    return id

def get_all_productos():
    sql = "SELECT * FROM producto"
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    productos = cursor.fetchall()
    return productos

def get_producto(x, y):
    sql = "SELECT id, tipo, descripcion, comuna_id, nombre_productor, email_productor, celular_productor FROM producto ORDER BY id DESC LIMIT %s, %s"
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(sql, (x, y))
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
    region = cursor.fetchone()
    return region

def get_comuna_by_id(id):
    sql = "SELECT nombre FROM comuna WHERE id=%s"
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(sql, (id,))
    conn.commit()
    comuna = cursor.fetchone()
    return comuna

def get_foto_by_id_product(id):
    sql = "SELECT nombre_archivo FROM foto WHERE producto_id=%s"
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(sql, (id,))
    conn.commit()
    fotos = cursor.fetchall()
    return fotos

def get_producto_by_id(id):
    sql = "SELECT * FROM producto WHERE id=%s"
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(sql, (id,))
    conn.commit()
    info = cursor.fetchall()
    return info

def get_productos_by_tipo(tipo):
    sql = ""
    if tipo == 'fruta':
        sql = "SELECT nombre FROM tipo_verdura_fruta WHERE id BETWEEN 1 AND 37;"
    if tipo == 'verdura':
        sql = "SELECT nombre FROM tipo_verdura_fruta WHERE id BETWEEN 38 AND 64;"
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    info = cursor.fetchall()
    return info

def get_all_pedidos():
    sql = "SELECT * FROM pedido"
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    productos = cursor.fetchall()
    return productos

def get_pedido(x, y):
    sql = "SELECT id, tipo, descripcion, comuna_id, nombre_comprador, email_comprador, celular_comprador FROM pedido ORDER BY id DESC LIMIT %s, %s"
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(sql, (x, y))
    conn.commit()
    productos = cursor.fetchall()
    return productos

def get_name_by_id_pedido(id):
    sql = "SELECT TVF.nombre FROM tipo_verdura_fruta TVF, pedido_verdura_fruta PVF WHERE TVF.id=PVF.tipo_verdura_fruta_id AND PVF.pedido_id=%s"
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(sql, (id,))
    conn.commit()
    product_names = cursor.fetchall()
    return product_names

def get_comprador_by_id_pedido(id):
    sql = "SELECT nombre_comprador FROM pedido WHERE id=%s"
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(sql, (id,))
    conn.commit()
    comprador = cursor.fetchone()
    return comprador

def get_pedido_by_id(id):
    sql = "SELECT * FROM pedido WHERE id=%s"
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(sql, (id,))
    conn.commit()
    info = cursor.fetchone()
    return info

def get_count_productos():
    sql = "SELECT TVF.nombre, count(*) FROM producto_verdura_fruta PVF, tipo_verdura_fruta TVF WHERE PVF.tipo_verdura_fruta_id = TVF.id GROUP BY TVF.nombre;"
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    info = cursor.fetchall()
    return info

# --- Ver si existe un elemento en la base de datos ---

def is_product(product):
    sql = "SELECT nombre FROM tipo_verdura_fruta WHERE nombre=%s"
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(sql, (product,))
    conn.commit()
    if cursor.fetchall():
        return True
    return False

def is_region(region):
    sql = "SELECT * FROM region WHERE nombre=%s"
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(sql, (region,))
    conn.commit()
    if cursor.fetchall():
        return True
    return False

def is_comuna(comuna):
    sql = "SELECT * FROM comuna WHERE nombre=%s"
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(sql, (comuna,))
    conn.commit()
    if cursor.fetchall():
        return True
    return False


# --- Agregar elementos a la base de datos ---

def create_producto(product_type, description, comuna_id, productor_name, productor_email, productor_phone):
    sql = "INSERT INTO producto (tipo, descripcion, comuna_id, nombre_productor, email_productor, celular_productor) VALUES (%s,%s,%s,%s,%s,%s)"
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(sql, (product_type, description, comuna_id, productor_name, productor_email, productor_phone))
    conn.commit()

    sql_id = "SELECT LAST_INSERT_ID()"
    cursor.execute(sql_id)
    conn.commit()
    id = cursor.fetchone()
    return id

def create_pedido(product_type, description, comuna_id, comprador_name, comprador_email, comprador_phone):
    sql = "INSERT INTO pedido (tipo, descripcion, comuna_id, nombre_comprador, email_comprador, celular_comprador) VALUES (%s,%s,%s,%s,%s,%s)"
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(sql, (product_type, description, comuna_id, comprador_name, comprador_email, comprador_phone))
    conn.commit()

    sql_id = "SELECT LAST_INSERT_ID()"
    cursor.execute(sql_id)
    conn.commit()
    id = cursor.fetchone()
    return id

def create_productovf(product_id, tvf_id):
    sql = "INSERT INTO producto_verdura_fruta (producto_id, tipo_verdura_fruta_id) VALUES (%s,%s)"
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(sql, (product_id, tvf_id))
    conn.commit()

def create_pedidovf(tvf_id, pedido_id):
    sql = "INSERT INTO pedido_verdura_fruta (tipo_verdura_fruta_id, pedido_id) VALUES (%s,%s)"
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(sql, (tvf_id, pedido_id))
    conn.commit()

def create_image(path, name, product_id):
    sql = "INSERT INTO foto (ruta_archivo, nombre_archivo, producto_id) VALUES (%s,%s,%s)"
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(sql, (path, name, product_id))
    conn.commit()