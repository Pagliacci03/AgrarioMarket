from flask import Flask, request, render_template, redirect, url_for
from database import db

app = Flask(__name__)


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