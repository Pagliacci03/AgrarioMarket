// --- Select menu for the product ---

/**
 * @description Valor del menu independiente (los tipos de producto).
 * @type {Element}
 */
const type_selected = document.getElementById("type");


/**
 * @description Valor del menu dependiente (los productos).
 * @type {Element}
 */
let products = document.getElementById("products");


/**
 * @description Diccionario que contiene el tipo de producto seguido de una lista de los productos disponibles para ese tipo.
 * @type {Map}
 */
const dicc_products = new Map([["fruta", [
    "Arándano", 
    "Frambuesa", 
    "Frutilla", 
    "Grosella", 
    "Mora", 
    "Limón", 
    "Mandarina", 
    "Naranja", 
    "Pomelo", 
    "Melón", 
    "Sandía", 
    "Palta", 
    "Chirimoya", 
    "Coco", 
    "Dátil", 
    "Kiwi", 
    "Mango", 
    "Papaya", 
    "Piña", 
    "Plátano", 
    "Damasco", 
    "Cereza", 
    "Ciruela", 
    "Higo", 
    "Kaki", 
    "Manzana", 
    "Durazno", 
    "Nectarin", 
    "Níspero", 
    "Pera", 
    "Uva", 
    "Almendra", 
    "Avellana", 
    "Maní", 
    "Castaña", 
    "Nuez", 
    "Pistacho"
]], ["verdura", [
    "Brócoli", 
    "Repollo", 
    "Coliflor", 
    "Rábano", 
    "Alcachofa", 
    "Lechuga", 
    "Zapallo", 
    "Pepino", 
    "Haba", 
    "Maíz", 
    "Champiñon", 
    "Acelga", 
    "Apio", 
    "Espinaca", 
    "Perejil", 
    "Ajo", 
    "Cebolla", 
    "Espárrago", 
    "Puerro", 
    "Remolacha", 
    "Berenjena", 
    "Papa", 
    "Pimiento", 
    "Tomate", 
    "Zanahoria"
]]]);


/**
 * Función que genera nuevas opciones para el menu de selección de los productos según el tipo de producto escogido.
 */
const change_product_select = () => {
    let product_type = type_selected.value;
    let list_of_products = dicc_products.get(product_type);

    products.innerHTML = ""; // Limpiar el contenido anterior

    list_of_products.forEach(product => {
        let checkbox = document.createElement("input");
        checkbox.type = "checkbox";
        checkbox.name = "product_checkbox";
        checkbox.value = product;

        let label = document.createElement("label");
        label.textContent = product;

        const br = document.createElement("br");

        products.appendChild(checkbox);
        products.appendChild(label);
        products.appendChild(br);
    });
};





// --- Select menu for comunas ---

/**
 * @description Valor del menu independiente (las regiones).
 * @type {Element}
 */
const region_selected = document.getElementById("region");


/**
 * @description Valor del menu dependiente (las comunas).
 * @type {Element}
 */
let comunas = document.getElementById("comunas");


/**
 * Función que genera nuevas opciones para el menu de selección de las comunas según la región escogida.
 */
const change_comuna_select = () => {
    let region = region_selected.options[region_selected.selectedIndex].value;

    if (region) {
        fetch('/comunas?region=' + region)
            .then(response => response.json())
            .then( data => {
                comunas.innerHTML = ""; // Limpiar el contenido anterior

                let defaultOption = document.createElement("option");
                defaultOption.text = "Seleccione una opción";
                defaultOption.disabled = true;
                defaultOption.selected = true;
                comunas.add(defaultOption);

                data.forEach(comuna => {
                    let option = document.createElement("option");
                    option.text = comuna;
                    comunas.add(option);
                });
            });
    }
};





// --- Files Selection ---

/**
 * @description Valor del contenedor para subir archivos.
 * @type {Element}
 */
const input_files = document.getElementById("files");


/**
 * Hace que aparezca un nuevo input para subir archivos al subir uno.
 */
const files_selection = () => {
    const upload_files = input_files.querySelectorAll('input[type="file"]');
    if (upload_files.length < 3) {
        let new_input_file = document.createElement("input");
        new_input_file.type = "file";
        new_input_file.className = "selection";
        input_files.appendChild(new_input_file);

        const br = document.createElement("br");
        input_files.appendChild(br);
    }
};





// --- Event Listener ---

type_selected.addEventListener("change", change_product_select);
input_files.addEventListener("change", files_selection);
region_selected.addEventListener("change", change_comuna_select);