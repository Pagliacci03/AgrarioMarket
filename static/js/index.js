// --- Form Handling ---

/**
 * Redirige a la página agregar-producto.
 */
const handleAddProduct = () => {
    window.location.href = "../html/agregar-producto.html";
};


/**
 * Redirige a la página ver-productos.
 */
const handleSeeProduct = () => {
    window.location.href = "../html/ver-productos.html";
};


/**
 * Redirige a la página agregar-pedido.
 */
const handleAddOrder = () => {
    window.location.href = "../html/agregar-pedido.html";
};


/**
 * Redirige a la página ver-pedidos.
 */
const handleSeeOrder = () => {
    window.location.href = "../html/ver-pedidos.html";
};


// --- Event Listener ---

/**
 * @description Valor del botón agregar-producto.
 * @type {Element}
 */
const addProductButton = document.getElementById("AgregarProducto");

/**
 * @description Valor del botón ver-productos.
 * @type {Element}
 */
const seeProductButton = document.getElementById("VerProductos");

/**
 * @description Valor del botón agregar-pedido.
 * @type {Element}
 */
const addOrderButton = document.getElementById("AgregarPedido");

/**
 * @description Valor del botón ver-pedidos.
 * @type {Element}
 */
const seeOrderButton = document.getElementById("VerPedidos");

addProductButton.addEventListener("click", handleAddProduct);
seeProductButton.addEventListener("click", handleSeeProduct);
addOrderButton.addEventListener("click", handleAddOrder);
seeOrderButton.addEventListener("click", handleSeeOrder);