/**
 * @description Elemento asociado a la imagen de informacion-producto.
 * @type {Element}
 */
const image = document.getElementById("imagen_info");


/**
 * Agranda la imagen de informacion-producto.
 */
const clickImage = () => {
    if(image.style.width == "640px"){
        image.style.width = "1280px";
        image.style.height = "1024px";
    }
    else {
        image.style.width = "640px";
        image.style.height = "480px";
    }
};


image.addEventListener("click", clickImage);