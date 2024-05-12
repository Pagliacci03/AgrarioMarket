from flask import Flask, request, render_template, redirect, url_for, jsonify
from database import db
from utils import validations as vald
from werkzeug.utils import secure_filename
import hashlib
import filetype
import os
import uuid

UPLOAD_FOLDER = 'static/uploads'

app = Flask(__name__)
app.secret_key = "secret_key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")

    elif request.method == "POST":
        button = request.form.get("index_button")
        if button == "Agregar Producto":
            return redirect(url_for("agregarProducto"))
        
        elif button == "Agregar Pedido":
            return redirect(url_for("agregarPedido"))
        
        elif button == "Ver Productos":
            return redirect(url_for("verProductos"))
        
        elif button == "Ver Pedidos":
            return redirect(url_for("verPedidos"))
        
        else:
            return render_template("index.html")
        

@app.route("/comunas")
def comunas():
    region = request.args.get('region')
    comunas = db.get_comunas_by_region(region)
    return jsonify(comunas)


@app.route("/agregar-producto", methods=["GET", "POST"])
def agregarProducto():
    if request.method == "POST":
        ptype = request.form.get("type")
        products = request.form.getlist("product_checkbox")
        description = request.form.get("description")
        files = request.files.getlist("image")
        region = request.form.get("region")
        comuna = request.form.get("comuna")
        pname = request.form.get("name")
        email = request.form.get("email")
        phone_number = request.form.get("phone")

        if len(files) >= 2 and len(files) <= 3 and not filetype.guess(files[-1]):
            files = files[:-1] 

        if vald.validate_agregar_producto(ptype, products, description, files, region, comuna, pname, email, phone_number):
            comuna_id = db.get_id_comuna_by_nombre(comuna)
            product_id = db.create_producto(ptype, description, comuna_id, pname, email, phone_number)
            for product in products:
                name_product_id = db.get_id_tvf_by_nombre(product)
                db.create_pvf(product_id, name_product_id)
            for img in files:
                # 1. generate random name for img
                _filename = hashlib.sha256(
                    secure_filename(img.filename).encode("utf-8")
                    ).hexdigest()
                _extension = filetype.guess(img).extension
                img_filename = f"{_filename}_{str(uuid.uuid4())}.{_extension}"

                # 2. save img as a file
                img_path = os.path.join(app.config["UPLOAD_FOLDER"], img_filename)
                img.save(img_path)

                db.create_image(img_path, img_filename, product_id)

            return redirect(url_for("index"))
        
    regiones = []
    for name in db.get_regiones():
        regiones.append(name[0])
    return render_template("agregar-producto.html", regiones=regiones)
    
@app.route("/ver-productos", methods=["GET", "POST"])
def verProductos():
    if request.method == "GET":
        return render_template("ver-productos.html")
    
@app.route("/agregar-pedido", methods=["GET", "POST"])
def agregarPedido():
    if request.method == "GET":
        return render_template("agregar-pedido.html")
    
@app.route("/ver-pedidos", methods=["GET", "POST"])
def verPedidos():
    if request.method == "GET":
        return render_template("ver-pedidos.html")
    
if __name__ == '__main__':
   app.run(debug = True)