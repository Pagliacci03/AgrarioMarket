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
 * Función que genera nuevas opciones para el menu de selección de los productos según el tipo de producto escogido.
 */
const change_product_select = () => {
    let product_type = type_selected.options[type_selected.selectedIndex].value;

    if (product_type) {
        fetch('/productos?tipo=' + product_type)
            .then(response => response.json())
            .then( data => {
                products.innerHTML = ""; // Limpiar el contenido anterior

                data.forEach(product => {
                    let checkbox = document.createElement("input");
                    checkbox.type = "checkbox";
                    checkbox.name = "product_checkbox";
                    checkbox.class = "checkboxes";
                    checkbox.value = product;
            
                    let label = document.createElement("label");
                    label.textContent = product;
            
                    const br = document.createElement("br");
            
                    products.appendChild(checkbox);
                    products.appendChild(label);
                    products.appendChild(br);
                });
            });
    }
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
                    option.value = comuna;
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
        new_input_file.name = "image";
        new_input_file.accept = "image/*";
        input_files.appendChild(new_input_file);

        const br = document.createElement("br");
        input_files.appendChild(br);
    }
};





// --- Event Listener ---

type_selected.addEventListener("change", change_product_select);
input_files.addEventListener("change", files_selection);
region_selected.addEventListener("change", change_comuna_select);