import filetype
from database import db
import re




# --- Validaciones ---

# Valida que n este en el rango de [i,j]
def validate_amount(n, i, j):
    return n >= i and n <= j

# Valida que un tipo de fruta o verdura
def validate_type(ptype):
    return ptype == "fruta" or ptype == "verdura"

# Valida que una lista de productos (nombres) estan en la base de datos
def validate_product(products):
    for product in products:
        if not db.is_product(product):
            False
    return validate_amount(len(products), 1, 5)

# Valida la description
def validate_description(description):
    return True

# Valida que la cantidad de imagenes es entre 1 a 3 y que sus extensiones son las permitidas
def validate_img(images):
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
    ALLOWED_MIMETYPES = {"image/jpeg", "image/png", "image/gif"}

    for img in images:
        ftype_guess = filetype.guess(img)
        if img is None:
               return False
        if img.filename == "":
            return False
            
        ftype_guess = filetype.guess(img)
        if ftype_guess.extension not in ALLOWED_EXTENSIONS:
            return False
        if ftype_guess.mime not in ALLOWED_MIMETYPES:
            return False
    return validate_amount(len(images), 1, 3)

# Valida que la region escogida este en la base de datos
def validate_region(region):
    if db.is_region(region):
        return True
    return False

# Valida que la comuna este en la base de datos
def validate_comuna(comuna):
    if db.is_comuna(comuna):
        return True
    return False

# Valida que un nombre cuente entre 1 a 80 caracteres y solo este formado por letras
def validate_name(name):
    new_name = name.replace(" ", "")
    if validate_amount(len(new_name), 1, 80):
        return bool(re.match('^[a-zA-Z]+$', new_name))
    return False
    
# Valida que un correo tenga el formato correcto ((nombre)@dominio.dot) con dominio y dot pudiendo ser solo los permitidos por el servidor
def validate_email(email):
    ALLOWED_DOMAINS = {"gmail", "outlook", "yahoo"}
    ALLOWED_DOTS = {"com", "cl"}

    new_email = re.split(r'[@.]', email)
    if validate_amount(len(new_email), 3, 3):
        if new_email[1] in ALLOWED_DOMAINS and new_email[2] in ALLOWED_DOTS:
            return True
    return False

# Valida que el numero celular esta formado por 8 digitos 
def validate_phone_number(phone_number):
    if phone_number:
        return phone_number.isdigit() and validate_amount(len(phone_number), 8, 8)
    return True

# Valida que la instancia de un producto que quiere ser agregado a la base de datos cumpla con el formato y restricciones para cada uno de sus atributos
def validate_agregar_producto(ptype, products, description, images, region, comuna, name, email, phone_number):
    return validate_type(ptype) and validate_product(products) and validate_description(description) and validate_img(images) and validate_region(region) and validate_comuna(comuna) and validate_name(name) and validate_email(email) and validate_phone_number(phone_number)

# Valida que la instancia de un pedido que quiere ser agregado a la base de datos cumpla con el formato y restricciones para cada uno de sus atributos
def validate_agregar_pedido(ptype, products, description, region, comuna, name, email, phone_number):
    return validate_type(ptype) and validate_product(products) and validate_description(description) and validate_region(region) and validate_comuna(comuna) and validate_name(name) and validate_email(email) and validate_phone_number(phone_number)





# --- Mensajes de Errores ---
# Retorna un mensaje de error solo si la validación es False

def error_type(ptype):
    if validate_type(ptype):
        return ""
    return "Error en el tipo elegido. "


def error_products(products):
    if validate_product(products):
        return ""
    return "Error en los productos elegidos. "


def error_images(images):
    if validate_img(images):
        return ""
    return "Error en los archivos subidos. "


def error_region(region):
    if validate_region(region):
        return ""
    return "Error en la region escogida. "


def error_comuna(comuna):
    if validate_comuna(comuna):
        return ""
    return "Error en la comuna escogida. "


def error_name(name):
    if validate_name(name):
        return ""
    return "Error en el nombre entregado. "


def error_email(email):
    if validate_email(email):
        return ""
    return "Error en el email entregado. "


def error_phone(phone):
    if validate_phone_number(phone):
        return ""
    return "Error en el número celular entregado. "


def error_inputs_productos(ptype, products, images, region, comuna, name, email, phone_number):
    error = error_type(ptype) + error_products(products) + error_images(images) + error_region(region) + error_comuna(comuna) + error_name(name) + error_email(email) + error_phone(phone_number)
    return error


def error_inputs_pedidos(ptype, products, region, comuna, name, email, phone_number):
    error = error_type(ptype) + error_products(products) + error_region(region) + error_comuna(comuna) + error_name(name) + error_email(email) + error_phone(phone_number)
    return error