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
  
    const product_type = document.getElementById("type");
    const products = document.getElementById("products");
    const files = document.getElementById("files");
    const region = document.getElementById("region");
    const comuna = document.getElementById("comunas");
    const name = document.getElementById("name");
    const email = document.getElementById("email");
    const phone_number = document.getElementById("phone");


    init_var_for_errors();

    // Errores posibles
    // El cliente no selecciona un tipo de producto.
    handleError(validateRequiredSelects, product_type.value, "Por favor, seleccione el tipo de producto.\n", product_type);

    // El cliente selecciona más de 5 o ningún producto.
    handleError(validateProducts, products, "Por favor, seleccione de 1 a 5 productos.\n", products);

    // El cliente selecciona más de 3 o ningún archivo.
    handleError(validatePictures, files, "Por favor, suba de 1 a 3 archivos.\n", files);

    // El cliente no selecciona una región.
    handleError(validateRequiredSelects, region.value, "Por favor, seleccione la región del producto.\n", region);

    // El cliente no selecciona una comuna.
    handleError(validateRequiredSelects, comuna.value, "Por favor, seleccione la comuna del producto.\n", comuna);

    // El cliente escribe un nombre con menos de 3 caracteres o más de 80.
    handleError(validateName, name.value, "Por favor, escriba un nombre que contenga entre 3 a 80 caracteres.\n", name);

    // El cliente escribe un email sin el formato adecuado.
    handleError(validateEmail, email.value, "Por favor, escriba una dirección de correo válida.\n", email);

    // El cliente escribe un número de celular con más o menos de 8 números.
    handleError(validatePhoneNumber, phone_number.value, "Por favor, escriba un número de teléfono válido.\n", phone_number);


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
 * Cancela la confirmación del formulario.
 */
const cancel = () => {
    modal.style.display = "none";
};


cancelarButton.addEventListener("click", cancel);





// --- Event Listener ---

/**
 * @description Valor del botón agregar-producto.
 * @type {Element}
 */
const add_products = document.getElementById("add_products");
add_products.addEventListener("click", handleForm);