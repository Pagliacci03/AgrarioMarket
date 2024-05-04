/**
 * Redirige las paginas que contengan un boton indice hacia indice cuando este es clickeado.
 */
const ToIndex = () => {
    window.location.href = "../html/index.html";
};


/**
 * @description Elemento asociado al boton indice.
 * @type {Element}
 */
const index_element = document.getElementById("index");


index_element.addEventListener("click", ToIndex);