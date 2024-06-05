from flask import Flask, request, render_template, redirect, url_for, jsonify, session
from flask_cors import cross_origin
from database import db
from utils.validations import validate_agregar_producto, error_inputs_productos, validate_agregar_pedido, error_inputs_pedidos
from werkzeug.utils import secure_filename
from PIL import Image
import hashlib
import filetype
import os
import uuid

UPLOAD_FOLDER = 'static/uploads'

app = Flask(__name__)
app.secret_key = "secret_key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# --- API's ---

# Retorna los productos en formato json segun el tipo especificado en la url
@app.route("/productos")
def productos():
    tipo = request.args.get('tipo')
    productos = db.get_productos_by_tipo(tipo)

    return jsonify(productos)


# Retorna las comunas en formato json segun la region especificada en la url
@app.route("/comunas")
def comunas():
    region = request.args.get('region')
    comunas = db.get_comunas_by_region(region) 

    return jsonify(comunas)


# Retorna el total de productos por tipo de fruta y verdura en formato json
@app.route("/get-stats-data-productos", methods=["GET"])
@cross_origin(origin="localhost", supports_credentials=True)
def get_stats_data_productos():

    data = []
    for producto in db.get_count_productos():
        nombre, cantidad = producto
        data.append({
            "name": nombre,
            "count": cantidad
        })

    return jsonify(data)


# Retorna el total de pedidos por comuna en formato json
@app.route("/get-stats-data-pedidos", methods=["GET"])
@cross_origin(origin="localhost", supports_credentials=True)
def get_stats_data_pedidos():

    data = []
    for comuna in db.get_count_pedidos():
        nombre, cantidad = comuna
        data.append({
            "name": nombre,
            "count": cantidad
        })

    return jsonify(data)





# --- Indice ---

@app.route("/", methods=["GET", "POST"])
def index():
    # No esta permitido acceder a la pagina success desde este punto
    session['allow_success'] = False

    if request.method == "GET":
        return render_template("index.html")

    elif request.method == "POST":
        button = request.form.get("index_button")
        if button == "Agregar Producto":
            return redirect(url_for("agregarProducto"))
        
        elif button == "Agregar Pedido":
            return redirect(url_for("agregarPedido"))
        
        elif button == "Ver Productos":
            return redirect(url_for("verProductos", pagina=0))
        
        elif button == "Ver Pedidos":
            return redirect(url_for("verPedidos", pagina=0))
        
        elif button == "Estadisticas":
            return redirect(url_for("stats"))
        
        else:
            return render_template("index.html")
        



# --- Agregar producto ---

@app.route("/agregar-producto", methods=["GET", "POST"])
def agregarProducto():
    # No esta permitido acceder a la pagina success desde este punto
    session['allow_success'] = False

    regiones = []
    for name in db.get_regiones():
        regiones.append(name[0])

    if request.method == "POST":
        index = request.form.get("back_to_index")

        if not index: # usuario hizo submit del formulario
            # datos del usuario registrados en el formulario
            product_type = request.form.get("type")
            products = request.form.getlist("product_checkbox")
            description = request.form.get("description")
            files = request.files.getlist("image")
            region = request.form.get("region")
            comuna = request.form.get("comuna")
            productor_name = request.form.get("name")
            productor_email = request.form.get("email")
            phone_number = request.form.get("phone")

            # no tomar en cuenta al input de tipo file que se agrega después de agregar un archivo al input anterior y esta vacío
            if len(files) >= 2 and len(files) <= 3 and not filetype.guess(files[-1]):
                if not filetype.guess(files[-2]):
                    files = files[:-2]
                else:
                    files = files[:-1] 

            # validacion backend
            if validate_agregar_producto(product_type, products, description, files, region, comuna, productor_name, productor_email, phone_number):
                comuna_id = db.get_id_comuna_by_nombre(comuna)
                product_id = db.create_producto(product_type, description, comuna_id, productor_name, productor_email, phone_number)

                # cada producto se asocia a un tipo de verdura o fruta
                for product in products:
                    name_product_id = db.get_id_tvf_by_nombre(product)
                    db.create_productovf(product_id, name_product_id)

                # se suben las imagenes a la carpeta uploads y a la base de datos en el servidor
                for img in files:
                    # generación de un nombre aleatorio para el archivo
                    _filename = hashlib.sha256(
                        secure_filename(img.filename).encode("utf-8")
                        ).hexdigest()
                    _extension = filetype.guess(img).extension
                    img_filename = f"{_filename}_{str(uuid.uuid4())}.{_extension}"

                    # guardar la imagen y sus distintas resoluciones en uploads
                    img_path = os.path.join(app.config["UPLOAD_FOLDER"], img_filename)
                    img.save(img_path)
                    sizes = [(120, 120), (640, 480), (1280, 1024)]
                    for size in sizes:
                        with Image.open(img_path) as temp_img:
                            resized_img = temp_img.resize(size)
                            resized_path = os.path.join(app.config["UPLOAD_FOLDER"], img_filename + f"_size_{size[0]}_{size[1]}.{_extension}")
                            resized_img.save(resized_path)

                    # guardar los datos del archivo en la base de datos
                    db.create_image(img_path, img_filename, product_id)

                # las validaciones son correctas por lo que se permite el acceso a la pagina de success
                session['allow_success'] = True
                return redirect(url_for("success"))
            
            else: # validaciones erroneas
                error = error_inputs_productos(product_type, products, files, region, comuna, productor_name, productor_email, phone_number)
                return render_template("agregar-producto.html", regiones=regiones, error=error)
        
        else: # se presiono el boton de regreso al indice
            return redirect(url_for("index"))

    return render_template("agregar-producto.html", regiones=regiones)
    



# --- Ver Productos ---

@app.route("/ver-productos/<pagina>", methods=["GET", "POST"])
def verProductos(pagina):
    # No esta permitido acceder a la pagina success desde este punto
    session['allow_success'] = False

    page = int(pagina)
    limit_left = page * 5
    show = 5
    notfirst = False
    notlast = False

    if page != 0: # no estamos en la primera pagina
        notfirst = True

    elementos = len(db.get_all_productos())
    last = elementos // 5 if elementos % 5 != 0 else (elementos // 5) - 1
    if (page != last): # no estamos en la ultima pagina
        notlast = True

    if request.method == "POST":
        index = request.form.get("back_to_index")
        anterior = request.form.get("back")
        siguiente = request.form.get("next")

        if index: # usuario quiere volver al indice
            return redirect(url_for("index"))
        
        if anterior: # usuario retrocedio de pagina
            page -= 1
            return redirect(url_for("verProductos", pagina=page))

        if siguiente: # usuario avanzo de pagina
            page += 1
            return redirect(url_for("verProductos", pagina=page))

    elif request.method == "GET":
        productos = []
        for product in db.get_producto(limit_left, show):
            product_id, tipo, _, comuna_id, _, _, _ = product

            # nombres del o los productos
            names = ""
            product_names = [row[0] for row in db.get_name_by_id_product(product_id)]
            for name in product_names:
                names += name + ", "
            names = names[:-2]

            # region
            region = db.get_region_by_id_comuna(comuna_id)[0]
            
            # comuna
            comuna = db.get_comuna_by_id(comuna_id)[0]
            
            # fotos
            urls = []
            fotos = [row[0] for row in db.get_foto_by_id_product(product_id)]
            for foto in fotos:
                p_img = f"uploads/{foto}_size_120_120"
                _extension = os.path.splitext(foto)[1].lower()
                p_img += f"{_extension}"
                urls.append(p_img)

            productos.append({
                "id": product_id,
                "tipo": tipo,
                "name": names,
                "region": region,
                "comuna": comuna,
                "fotos": urls
            })

        return render_template("ver-productos.html", productos=productos, notfirst=notfirst, notlast=notlast, page=(page+1))




# --- Información Producto ---

@app.route("/informacion-producto/<producto_id>/<width>/<height>", methods=["GET", "POST"])
def informacionProducto(producto_id, width, height):
    # No esta permitido acceder a la pagina success desde este punto
    session['allow_success'] = False

    if request.method == "POST":
        index = request.form.get("index")
        if index: # usuario desea volver al indice
            return redirect(url_for("index"))
        
    elif request.method == "GET":
        _, product_type, description, comuna_id, productor, email, phone_number = db.get_producto_by_id(producto_id)[0]
        
        # nombres del o los productos
        names = ""
        product_names = [row[0] for row in db.get_name_by_id_product(producto_id)]
        for name in product_names:
            names += name + ", "
        names = names[:-2]

        # fotos
        urls = []
        fotos = [row[0] for row in db.get_foto_by_id_product(producto_id)]
        for foto in fotos:
            p_img = f"uploads/{foto}_size_{width}_{height}"
            _extension = os.path.splitext(foto)[1].lower()
            p_img += f"{_extension}"
            urls.append(p_img)

        # comuna
        comuna = db.get_comuna_by_id(comuna_id)[0]

        # region
        region = db.get_region_by_id_comuna(comuna_id)[0]

        # descripcion
        if not description:
            description = ""

        # numero celular
        if not phone_number:
            phone_number = ""
        
            
        info = {
            "id": producto_id,
            "tipo": product_type,
            "productos": names,
            "descripcion": description,
            "fotos": urls,
            "region": region,
            "comuna": comuna,
            "productor": productor,
            "email": email,
            "celular": phone_number,
            "width": width,
            "height": height
        }

        return render_template("informacion-producto.html", info=info)




# --- Agregar Pedido ---

@app.route("/agregar-pedido", methods=["GET", "POST"])
def agregarPedido():
    # No esta permitido acceder a la pagina success desde este punto
    session['allow_success'] = False
    
    regiones = []
    for name in db.get_regiones():
        regiones.append(name[0])

    if request.method == "POST":
        index = request.form.get("back_to_index")

        if not index: # usuario hizo submit del formulario
            # datos del usuario registrados en el formulario
            product_type = request.form.get("type")
            products = request.form.getlist("product_checkbox")
            description = request.form.get("description")
            region = request.form.get("region")
            comuna = request.form.get("comuna")
            productor_name = request.form.get("name")
            productor_email = request.form.get("email")
            phone_number = request.form.get("phone")

            # validacion backend
            if validate_agregar_pedido(product_type, products, description, region, comuna, productor_name, productor_email, phone_number):
                comuna_id = db.get_id_comuna_by_nombre(comuna)
                pedido_id = db.create_pedido(product_type, description, comuna_id, productor_name, productor_email, phone_number)

                # cada producto se asocia a un tipo de verdura o fruta
                for product in products:
                    name_product_id = db.get_id_tvf_by_nombre(product)
                    db.create_pedidovf(name_product_id, pedido_id)

                # las validaciones son correctas por lo que se permite el acceso a la pagina de success
                session['allow_success'] = True
                return redirect(url_for("success"))
            
            else: # error en la validacion
                error = error_inputs_pedidos(product_type, products, region, comuna, productor_name, productor_email, phone_number)
                return render_template("agregar-pedido.html", regiones=regiones, error=error)
        
        else: # se presiono el boton de regreso al indice
            return redirect(url_for("index"))

    return render_template("agregar-pedido.html", regiones=regiones)




# --- Ver Pedidos ---

@app.route("/ver-pedidos/<pagina>", methods=["GET", "POST"])
def verPedidos(pagina):
    # No esta permitido acceder a la pagina success desde este punto
    session['allow_success'] = False

    page = int(pagina)
    limit_left = page * 5
    show = 5
    notfirst = False
    notlast = False

    if page != 0: # no estamos en la primera pagina
        notfirst = True

    elementos = len(db.get_all_pedidos())
    last = elementos // 5 if elementos % 5 != 0 else (elementos // 5) - 1
    if (page != last): # no estamos en la ultima pagina
        notlast = True

    if request.method == "POST":
        index = request.form.get("back_to_index")
        anterior = request.form.get("back")
        siguiente = request.form.get("next")

        if index: # usuario quiere volver al indice
            return redirect(url_for("index"))
        
        if anterior: # usuario retrocedio de pagina
            page -= 1
            return redirect(url_for("verPedidos", pagina=page))

        if siguiente: # usuario avanzo de pagina
            page += 1
            return redirect(url_for("verPedidos", pagina=page))

    elif request.method == "GET":
        pedidos = []
        for pedido in db.get_pedido(limit_left, show):
            pedido_id, tipo, _, comuna_id, _, _, _ = pedido

            # nombre del o los prodcutos
            names = ""
            product_names = [row[0] for row in db.get_name_by_id_pedido(pedido_id)]
            for name in product_names:
                names += name + ", "
            names = names[:-2]

            # region
            region = db.get_region_by_id_comuna(comuna_id)[0]

            # comuna
            comuna = db.get_comuna_by_id(comuna_id)[0]

            # nombre del comprador
            comprador = db.get_comprador_by_id_pedido(pedido_id)[0]

            pedidos.append({
                "id": pedido_id,
                "tipo": tipo,
                "name": names,
                "region": region,
                "comuna": comuna,
                "comprador": comprador
            })

        return render_template("ver-pedidos.html", pedidos=pedidos, notfirst=notfirst, notlast=notlast, page=(page+1))




# --- Información Pedido ---

@app.route("/informacion-pedido/<pedido_id>", methods=["GET", "POST"])
def informacionPedido(pedido_id):
    # No esta permitido acceder a la pagina success desde este punto
    session['allow_success'] = False

    if request.method == "POST":
        index = request.form.get("index")
        if index: # usuario desea volver al indice
            return redirect(url_for("index"))
        
    elif request.method == "GET":
        _, product_type, description, comuna_id, comprador, email, phone_number = db.get_pedido_by_id(pedido_id)
        
        # nombre del o los productos
        names = ""
        product_names = [row[0] for row in db.get_name_by_id_pedido(pedido_id)]
        for name in product_names:
            names += name + ", "
        names = names[:-2]

        # comuna
        comuna = db.get_comuna_by_id(comuna_id)[0]

        # region
        region = db.get_region_by_id_comuna(comuna_id)[0]

        # descripcion
        if not description:
            description = ""

        # numero celular
        if not phone_number:
            phone_number = ""
        
            
        info = {
            "id": pedido_id,
            "tipo": product_type,
            "productos": names,
            "descripcion": description,
            "region": region,
            "comuna": comuna,
            "comprador": comprador,
            "email": email,
            "celular": phone_number,
        }

        return render_template("informacion-pedido.html", info=info)





# --- Stats ---

@app.route("/stats", methods=["GET"])
def stats():
    # No esta permitido acceder a la pagina success desde este punto
    session['allow_success'] = False
    return render_template("stats.html")





# --- Agregados con exito ---

@app.route("/success", methods=["GET", "POST"])
def success():
    if not session.get('allow_success'):
        # Si la sesión no permite el acceso, redirige a la página de inicio
        return redirect(url_for('index'))

    if request.method == "POST":
        return redirect(url_for("index"))
    
    elif request.method == "GET":
        return render_template("success.html")





if __name__ == '__main__':
   app.run(debug = True)