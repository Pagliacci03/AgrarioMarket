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

                let label = document.createElement("label");
                label.textContent = "Seleccione de 1 a 5 productos";
                products.appendChild(label);
                const br = document.createElement("br");
                products.appendChild(br)

                data.forEach(product => {
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
 * @description Diccionario que contiene la region del producto seguido de una lista con las comunas de esa región.
 * @type {Map}
 */
let dicc_regiones = new Map([
    ["arica", [
        "Arica",
        "Camarones",
        "General Lagos",
        "Putre"
    ]],
    ["tarapaca", [
        "Iquique",
        "Alto Hospicio",
        "Camiña",
        "Colchane",
        "Huara",
        "Pica",
        "Pozo Almonte"
    ]],
    ["antofagasta", [
        "Antofagasta",
        "Mejillones",
        "Sierra Gorda",
        "Taltal",
        "Calama",
        "Ollague",
        "San Pedro de Atacama",
        "Tocopilla",
        "María Elena"
    ]],
    ["atacama", [
        "Copiapó",
        "Caldera",
        "Tierra Amarilla",
        "Chañaral",
        "Diego de Almagro",
        "Vallenar",
        "Alto del Carmen",
        "Freirina",
        "Huasco"
    ]],
    ["coquimbo", [
        "La Serena",
        "Coquimbo",
        "Andacollo",
        "La Higuera",
        "Paihuano",
        "Vicuña",
        "Illapel",
        "Canela",
        "Los Vilos",
        "Salamanca",
        "Ovalle",
        "Combarbalá",
        "Monte Patria",
        "Punitaqui",
        "Río Hurtado"
    ]],
    ["valparaiso", [
        "Valparaíso",
        "Casablanca",
        "Concón",
        "Juan Fernández",
        "Puchuncaví",
        "Quintero",
        "Viña del Mar",
        "Isla de Pascua",
        "Los Andes",
        "Calle Larga",
        "Rinconada",
        "San Esteban",
        "La Ligua",
        "Cabildo",
        "Papudo",
        "Petorca",
        "Zapallar",
        "Quillota",
        "Calera",
        "Hijuelas",
        "La Cruz",
        "Nogales",
        "San Antonio",
        "Algarrobo",
        "Cartagena",
        "El Quisco",
        "El Tabo",
        "Santo Domingo",
        "San Felipe",
        "Catemu",
        "Llaillay",
        "Panquehue",
        "Putaendo",
        "Santa María",
        "Quilpué",
        "Limache",
        "Olmué",
        "Villa Alemana"
    ]],
    ["metropolitana", [
        "Santiago",
        "Cerrillos",
        "Cerro Navia",
        "Conchalí",
        "El Bosque",
        "Estación Central",
        "Huechuraba",
        "Independencia",
        "La Cisterna",
        "La Florida",
        "La Granja",
        "La Pintana",
        "La Reina",
        "Las Condes",
        "Lo Barnechea",
        "Lo Espejo",
        "Lo Prado",
        "Macul",
        "Maipú",
        "Ñuñoa",
        "Pedro Aguirre Cerda",
        "Peñalolén",
        "Providencia",
        "Pudahuel",
        "Quilicura",
        "Quinta Normal",
        "Recoleta",
        "Renca",
        "San Joaquín",
        "San Miguel",
        "San Ramón",
        "Vitacura",
        "Puente Alto",
        "Pirque",
        "San José de Maipo",
        "Colina",
        "Lampa",
        "Til Til",
        "San Bernardo",
        "Buin",
        "Calera de Tango",
        "Paine",
        "Melipilla",
        "Alhué",
        "Curacaví",
        "María Pinto",
        "San Pedro",
        "Talagante",
        "El Monte",
        "Isla de Maipo",
        "Padre Hurtado",
        "Peñaflor"
    ]],
    ["ohiggins", [
        "Rancagua",
        "Codegua",
        "Coinco",
        "Coltauco",
        "Doñihue",
        "Graneros",
        "Las Cabras",
        "Machalí",
        "Malloa",
        "Mostazal",
        "Olivar",
        "Peumo",
        "Pichidegua",
        "Quinta de Tilcoco",
        "Rengo",
        "Requínoa",
        "San Vicente de Tagua Tagua",
        "La Estrella",
        "Litueche",
        "Marchihue",
        "Navidad",
        "Peredones",
        "Pichilemu",
        "Chépica",
        "Chimbarongo",
        "Lolol",
        "Nancagua",
        "Palmilla",
        "Peralillo",
        "Placilla",
        "Pumanque",
        "Santa Cruz"
    ]],
    ["maule", [
        "Talca",
        "Consitución",
        "Curepto",
        "Empedrado",
        "Maule",
        "Pelarco",
        "Pencahue",
        "Río Claro",
        "San Clemente",
        "San Rafael",
        "Cauquenes",
        "Chanco",
        "Pelluhue",
        "Curicó",
        "Hualañé",
        "Licantén",
        "Molina",
        "Rauco",
        "Romeral",
        "Sagrada Familia",
        "Teno",
        "Vichuquén",
        "Linares",
        "Colbún",
        "Longaví",
        "Parral",
        "Retiro",
        "San Javier",
        "Villa Alegre",
        "Yerbas Buenas"
    ]],
    ["nuble", [
        "Chillán",
        "Bulnes",
        "Cobquecura",
        "Coelemu",
        "Coihueco",
        "Chillán Viejo",
        "El Carmen",
        "Ninhue",
        "Ñiquén",
        "Pemuco",
        "Pinto",
        "Portezuelo",
        "Quillón",
        "Quirihue",
        "Ránquil",
        "San Carlos",
        "San Fabián",
        "San Ignacio",
        "San Nicolás",
        "Treguaco",
        "Yungay"
    ]],
    ["biobio", [
        "Concepción",
        "Coronel",
        "Chiguayante",
        "Florida",
        "Hualqui",
        "Lota",
        "Penco",
        "San Pedro de la Paz",
        "Santa Juana",
        "Talcahuano",
        "Tomé",
        "Hualpén",
        "Lebu",
        "Arauco",
        "Cañete",
        "Contulmo",
        "Curanilahue",
        "Los Álamos",
        "Tirúa",
        "Los Ángeles",
        "Antuco",
        "Cabrero",
        "Laja",
        "Mulchén",
        "Nacimiento",
        "Negrete",
        "Quilaco",
        "Quilleco",
        "San Rosendo",
        "Santa Bárbara",
        "Tucapel",
        "Yumbel",
        "Alto Biobío"
    ]],
    ["araucania", [
        "Temuco",
        "Carahue",
        "Cunco",
        "Curarrehue",
        "Freire",
        "Galvarino",
        "Gorbea",
        "Lautaro",
        "Loncoche",
        "Melipeuco",
        "Nueva Imperial",
        "Padre las Casas",
        "Perquenco",
        "Pitrufquén",
        "Pucón",
        "Saavedra",
        "Teodoro Schmidt",
        "Toltén",
        "Vilcún",
        "Villarrica",
        "Cholchol",
        "Angol",
        "Collipulli",
        "Curacautín",
        "Ercilla",
        "Lonquimay",
        "Los Sauces",
        "Lumaco",
        "Purén",
        "Renaico",
        "Traiguén",
        "Victoria"
    ]],
    ["rios", [
        "Valdivia",
        "Corral",
        "Lanco",
        "Los Lagos",
        "Máfil",
        "Mariquina",
        "Paillaco",
        "Panguipulli",
        "La Unión",
        "Futrono",
        "Lago Ranco",
        "Río Bueno"
    ]],
    ["lagos", [
        "Puerto Montt",
        "Calbuco",
        "Cochamó",
        "Fresia",
        "Frutillar",
        "Los Muermos",
        "Llanquihue",
        "Maullín",
        "Puerto Varas",
        "Castro",
        "Ancud",
        "Chonchi",
        "Curaco de Vélez",
        "Dalcahue",
        "Puqueldón",
        "Queilén",
        "Quellón",
        "Quemchi",
        "Quinchao",
        "Osorno",
        "Puerto Octay",
        "Purranque",
        "Puyehue",
        "Río Negro",
        "San Juan de la Costa",
        "San Pablo",
        "Chaitén",
        "Futaleufú",
        "Hualaihué",
        "Palena"
    ]],
    ["aysen", [
        "Coyhaique",
        "Lago Verde",
        "Aysén",
        "Cisnes",
        "Guaitecas",
        "Cochrane",
        "O'Higgins",
        "Tortel",
        "Chile Chico",
        "Río Ibáñez"
    ]],
    ["magallanes", [
        "Punta Arenas",
        "Laguna Blanca",
        "Río Verde",
        "San Gregorio",
        "Cabo de Hornos (Ex Navarino)",
        "Antártica",
        "Porvenir",
        "Primavera",
        "Timaukel",
        "Natales",
        "Torres del Paine"
    ]]
]);


// ordena las comunas por orden alfabético
for (const [region, valores] of dicc_regiones) {
    // Ordenar la lista de valores alfabéticamente
    dicc_regiones.set(region, valores.sort());
}


/**
 * Función que genera nuevas opciones para el menu de selección de las comunas según la región escogida.
 */
const change_comuna_select = () => {
    comunas.innerHTML = "";

    let defaultOption = document.createElement("option");
    defaultOption.text = "Seleccione una opción";
    defaultOption.disabled = true;
    defaultOption.selected = true;
    comunas.add(defaultOption);

    let options = dicc_regiones.get(region_selected.value);

    options.forEach(optionText => {
        let option = document.createElement("option");
        option.text = optionText;
        comunas.add(option);
    });
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
        new_input_file.className = "menu_selection";
        input_files.appendChild(new_input_file);
    }
};





// --- Event Listener ---

type_selected.addEventListener("change", change_product_select);
input_files.addEventListener("change", files_selection);
region_selected.addEventListener("change", change_comuna_select);