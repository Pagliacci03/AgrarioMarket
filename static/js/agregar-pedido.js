// --- Form Handling ---

/**
 * @description Valor del modal de confirmación.
 * @type {Element}
 */
const modal = document.getElementById("modal_order");

/**
 * Función que maneja el formulario notificando los errores que ha cometido el usuario 
 * al llenar este y llevándolo al cuadro de confimación si es que los datos estan correctos.
 */
const handleForm = () => {
    console.log("Validating form...");
  
    const productType_select = document.getElementById("product_type");
    const products_select = document.getElementById("products");
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
    handleError(validateProducts, products_select, "Por favor, seleccione de entre 1 a 5 productos.\n", products_select);

    // El cliente no selecciona una región.
    handleError(validateRequiredSelects, region_select.value, "Por favor, seleccione la región del pedido.\n", region_select);

    // El cliente no selecciona una comuna.
    handleError(validateRequiredSelects, comuna_select.value, "Por favor, seleccione la comuna del pedido.\n", comuna_select);

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
 * Cancela la confirmación del formulario.
 */
const cancel = () => {
    modal.style.display = "none";
};


cancelarButton.addEventListener("click", cancel);





// --- Event Listener ---

/**
 * @description Valor del botón agregar-pedido.
 * @type {Element}
 */
const add_order_button = document.getElementById("add_order");
add_order_button.addEventListener("click", handleForm);