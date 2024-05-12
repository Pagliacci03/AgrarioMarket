import filetype
from database import db
import re



def validate_amount(n, i, j):
    return n >= i and n <= j


def validate_type(ptype):
    return ptype == "fruta" or ptype == "verdura"


def validate_product(products):
    for product in products:
        if not db.is_product(product):
            False
    return validate_amount(len(products), 1, 5)


def validate_description(description):
    return True


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


def validate_region(region):
    if db.is_region(region):
        return True
    return False


def validate_comuna(comuna):
    if db.is_comuna(comuna):
        return True
    return False


def validate_name(name):
    new_name = name.replace(" ", "")
    if validate_amount(len(new_name), 1, 80):
        return bool(re.match('^[a-zA-Z]+$', new_name))
    return False
    

def validate_email(email):
    ALLOWED_DOMAINS = {"gmail", "outlook", "yahoo"}
    ALLOWED_DOTS = {"com", "cl"}

    new_email = re.split(r'[@.]', email)
    if validate_amount(len(new_email), 3, 3):
        if new_email[1] in ALLOWED_DOMAINS and new_email[2] in ALLOWED_DOTS:
            return True
    return False


def validate_phone_number(phone_number):
    if phone_number:
        return phone_number.isdigit() and validate_amount(len(phone_number), 8, 8)
    return True


def validate_agregar_producto(ptype, products, description, images, region, comuna, name, email, phone_number):
    return validate_type(ptype) and validate_product(products) and validate_description(description) and validate_img(images) and validate_region(region) and validate_comuna(comuna) and validate_name(name) and validate_email(email) and validate_phone_number(phone_number)
