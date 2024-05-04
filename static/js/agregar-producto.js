// --- Files Selection ---

/**
 * @description Valor del contenedor para subir archivos.
 * @type {Element}
 */
const files_input = document.getElementById("files");


/**
 * Hace que aparezca un nuevo input para subir archivos al subir uno.
 */
const files_selection = () => {
    const upload_files = files_input.querySelectorAll('input[type="file"]');
    if (upload_files.length < 3) {
        let input_file = document.createElement("input");
        input_file.type = "file";
        input_file.className = "menu_selection";
        files_input.appendChild(input_file);
    }
};


files_input.addEventListener("change", files_selection);




// --- Form Handling ---

/**
 * @description Valor del modal de confirmación.
 * @type {Element}
 */
const modal = document.getElementById("modal_product");

/**
 * Función que maneja el formulario notificando los errores que ha cometido el usuario 
 * al llenar este y llevándolo al cuadro de confimación si es que los datos estan correctos.
 */
const handleForm = () => {
    console.log("Validating form...");
  
    const productType_select = document.getElementById("product_type");
    const products_select = document.getElementById("products");
    const files_input = document.getElementById("files");
    const region_select = document.getElementById("region");
    const comuna_select = document.getElementById("comunas");
    const name_input = document.getElementById("name");
    const email_input = document.getElementById("email");
    const phone_number_input = document.getElementById("phone");


    init_var_for_errors();

    // Errores posibles
    // El cliente no selecciona un tipo de producto.
    handleError(validateRequiredSelects, productType_select.value, "Por favor, seleccione el tipo de producto.\n", productType_select);

    // El cliente selecciona más de 5 o ningún producto.
    handleError(validateProducts, products_select, "Por favor, seleccione de 1 a 5 productos.\n", products_select);

    // El cliente selecciona más de 3 o ningún archivo.
    handleError(validatePictures, files_input, "Por favor, suba de 1 a 3 archivos.\n", files_input);

    // El cliente no selecciona una región.
    handleError(validateRequiredSelects, region_select.value, "Por favor, seleccione la región del producto.\n", region_select);

    // El cliente no selecciona una comuna.
    handleError(validateRequiredSelects, comuna_select.value, "Por favor, seleccione la comuna del producto.\n", comuna_select);

    // El cliente escribe un nombre con menos de 3 caracteres o más de 80.
    handleError(validateName, name_input.value, "Por favor, escriba un nombre que contenga entre 3 a 80 caracteres.\n", name_input);

    // El cliente escribe un email sin el formato adecuado.
    handleError(validateEmail, email_input.value, "Por favor, escriba una dirección de correo válida.\n", email_input);

    // El cliente escribe un número de celular con más o menos de 8 números.
    handleError(validatePhoneNumber, phone_number_input.value, "Por favor, escriba un número de teléfono válido.\n", phone_number_input);


    // Alertar al usuario de sus errores o llevarlo al cuadro de confirmación.
    if (!isValid) {
        alert(errorMessage);
    } else {
        modal.style.display = "block";
    }
};




// --- Confirmation ---

/**
 * @description Valor del botón confirmar.
 * @type {Element}
 */
const confirmarButton = document.getElementById("confirmar");


/**
 * @description Valor del botón cancelar.
 * @type {Element}
 */
const cancelarButton = document.getElementById("cancelar");


/**
 * Redirige a la página index.
 */
const redirectToIndex = () => {
    modal.style.display = "none";
    const modal_success = document.getElementById("modal_success");
    modal_success.style.display = "block";
};


/**
 * Cancela la confirmación del formulario.
 */
const cancel = () => {
    modal.style.display = "none";
};

/**
 * @description Valor del botón aceptar del modal que redirige al indice.
 * @type {Element}
 */
const aceptarButton = document.getElementById("aceptar");

confirmarButton.addEventListener("click", redirectToIndex);
cancelarButton.addEventListener("click", cancel);
aceptarButton.addEventListener("click", ToIndex);




// --- Event Listener ---

/**
 * @description Valor del botón agregar-producto.
 * @type {Element}
 */
const add_products_button = document.getElementById("add_products");
add_products_button.addEventListener("click", handleForm);