/**
 * Redirige hacia la informacicion-pedido.
 */
const redirectOrder = () => {
    window.location.href = "../html/informacion-pedido.html";
};

const clickTable_1 = document.getElementById("pedido_1");
const clickTable_2 = document.getElementById("pedido_2");
const clickTable_3 = document.getElementById("pedido_3");
const clickTable_4 = document.getElementById("pedido_4");
const clickTable_5 = document.getElementById("pedido_5");
clickTable_1.addEventListener("click", redirectOrder);
clickTable_2.addEventListener("click", redirectOrder);
clickTable_3.addEventListener("click", redirectOrder);
clickTable_4.addEventListener("click", redirectOrder);
clickTable_5.addEventListener("click", redirectOrder);