/**
 * Redirige hacia la informacicion-producto.
 */
const redirectProduct = () => {
    window.location.href = "../html/informacion-producto.html";
};

const clickTable_1 = document.getElementById("producto_1");
const clickTable_2 = document.getElementById("producto_2");
const clickTable_3 = document.getElementById("producto_3");
const clickTable_4 = document.getElementById("producto_4");
const clickTable_5 = document.getElementById("producto_5");
clickTable_1.addEventListener("click", redirectProduct);
clickTable_2.addEventListener("click", redirectProduct);
clickTable_3.addEventListener("click", redirectProduct);
clickTable_4.addEventListener("click", redirectProduct);
clickTable_5.addEventListener("click", redirectProduct);