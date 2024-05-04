// --- Aux functions ---

/**
 * Determina si un valor se encuentra en un intervalo.
 * 
 * @param {Number} len - Cantidad de elementos en un objeto (cantidad de archivos, cantidad de caracteres en un string). 
 * @param {Number} i - Inicio del intervalo.
 * @param {Number} j - Final del intervalo.
 * 
 * @return {Boolean} - True si el valor esta en el rango y false en caso contrario.
 */
const validateRange = (len, i, j) => {
    return len >= i && len <= j;
};


/**
 * Separa un email en 5 partes. Por ejemplo, juan@gmail.com lo separa en juan, @, gmail, . y com.
 * @ y . siempre deben estar, lo demás cambia.
 * 
 * @param {String} email - Email del usuario. 
 * 
 * @return {Array} - Retorna un arreglo con todas las partes si es que se cumple que @ y . se estan en el input 
 *                   y en ese orden de aparición. En caso contrario devuelve null.
 */
const splitEmail = email => {
    const parts = email.match(/([^@]+)@([^\.]+)\.([^\.]+)/);

    if (parts && parts.length === 4) {
        const emailArray = [parts[1], '@', parts[2], '.', parts[3]];
        return emailArray;
    } else {
        return null;
    }
};




// --- Validation Functions ---

/**
 * Valida los menu selects obligatorios de la página web.
 * 
 * @param {String} select_value - Valor del elemento seleccionado.
 * 
 * @return {Boolean} - True si seleccionó un elemento, false en caso contrario.
 */
const validateRequiredSelects = select_value => select_value != "" && select_value != "Seleccione una opción";


/**
 * Valida que los productos seleccionados hayan sido entre 1 a 5.
 * 
 * @param {Element} products_element - Elemento con los productos seleccionados.  
 * 
 * @return {Boolean} - True si el cliente seleccionó de 1 a 5 productos, false en caso contrario. 
 */
const validateProducts = products_element => {
    let count = 0;
    const checkboxes = products_element.querySelectorAll('input[type="checkbox"]');
    checkboxes.forEach(checkbox => {
        if (checkbox.checked) {
            count++;
        }
    });
    return count >= 1 && count <= 5;
};


/**
 * Valida la cantidad de fotos subidas a la página web y que sean imágenes.
 * 
 * @param {Element} Files - Elemento que contiene los archivos subidos.
 * 
 * @return {Boolean} - True si el cliente subió de 1 a 3 archivos, false en caso contrario. 
 */
const validatePictures = Files => {
    let count = 0;
    const upload_files = Files.querySelectorAll('input[type="file"]');
    upload_files.forEach(file => {
        if (file.files.length > 0 && file.files[0].type.startsWith('image/')) {
            count++;
        }
    });
    return count >= 1 && count <= 3;
};


/**
 * Valida el largo de un nombre de un productor.
 * 
 * @param {String} name_value - Nombre del productor. 
 * 
 * @return {Boolean} - True si el nombre de un productor posee entre 3 a 80 caracteres, false en caso contrario.
 */
const validateName = name_value => {
    if (validateRange(name_value.length, 3, 80)) {
        const sinEspacios = name_value.replace(/\s/g, '');
        return /^[a-zA-Z]+$/.test(sinEspacios);
    }
    return false;
};


/**
 * Valida el email del productor.
 * 
 * @param {String} email_value - Email del productor. 
 * 
 * @return {Boolean} - True si el email cumple con el formato, false en caso contrario.
 */
const validateEmail = email_value => {
    const domains = ["gmail", "outlook", "yahoo"];
    const dots = ["com", "cl"];
    const emailParts = splitEmail(email_value);
    if (emailParts != null && dots.includes(emailParts[4]) && domains.includes(emailParts[2])) {
        return /^[a-zA-Z0-9]+$/.test(emailParts[0]);
    }
    return false;
};


/**
 * Valida el número celular del productor solo si es que este lo agregó.
 * 
 * @param {String} phone_number_value - Número celular del productor.
 * 
 * @return {Boolean} - True si el número cumple con el formato, es decir, contiene 8 números, false en caso contrario. 
 */
const validatePhoneNumber = phone_number_value => {
    if(phone_number_value != "") {
        return /^\d+$/.test(phone_number_value) && phone_number_value.length == 8;
    }
    return true;
};




// --- Errors Handling ---

/**
 * @description Variable que define si el formulario esta correcto.
 * @type {Boolean}
 */
let isValid = true;

/**
 * @description Variable que guarda los mensajes de errores dados por las validaciones.
 * @type {String}
 */
let errorMessage = "";


/**
 * Inicializa las variables isValid y errorMessage puesto que se completó o corrigió el formulario.
 * 
 */
const init_var_for_errors = () => {
    isValid = true;
    errorMessage = "";
};


/**
 * Guarda todos los errores que hubieron al completar el formulario.
 * 
 * @param {Function} func - Función usada para validar un input del usuario en la página.
 * @param {any} arg - Argumento de la función dada anteriormente.
 * @param {String} message - String con los mensajes para que el usuario se de cuenta del error.
 * @param {Element} element - Elemento de donde se obtuvo arg.
 */
const handleError = (func, arg, message, element) => {
    if (!func(arg)) {
        isValid = false;
        errorMessage += message;
        element.style.borderColor = "red";
    } else {
        element.style.borderColor = "";
    }
};