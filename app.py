from flask import Flask, request, render_template, redirect, url_for
from database import db

app = Flask(__name__)

limit_left = 0
limit_right = 5


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
        

@app.route("/agregar-producto", methods=["GET", "POST"])
def agregarProducto():
    if request.method == "GET":
        return render_template("agregar-producto.html")
    
@app.route("/ver-productos", methods=["GET", "POST"])
def verProductos():
    data_products = []
    for product in db.get_producto(limit_left, limit_right):
        product_id, tipo, _, comuna_id, _, _, _ = product
        name = db.get_name_by_id_product(product_id)
        region = db.get_region_by_id_comuna(comuna_id)
        comuna = db.get_comuna_by_id(comuna_id)
        fotos = db.get_foto_by_id_product(product_id)

        data_products.append({
            "tipo": tipo,
            "name": name,
            "region": region,
            "comuna": comuna,
            "fotos": fotos
        })
    
    return render_template("ver-productos.html", data=data_products)
    
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