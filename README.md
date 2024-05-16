# AgrarioMarket
### Sobre el proyecto

El siguiente proyecto es una solución de la tarea 2 del curso CC5002: Desarrollo de Aplicaciones Webs de la Universidad de Chile. Esta tarea consiste en la creación de páginas webs donde los productores de frutas y verduras del país pueden agregar sus productos para que estos sean comprados directamente sin la necesidad de intermediarios que elevan el precio final.

### Uso

La primera página vista por el usuario es index.html, esta posee 4 botones que llevan a distintas páginas donde el usuario puede interactuar para agregar producto(s), ver los productos agregados, agregar un producto a comprar, es decir, un pedido o ver los pedidos agregados. 

La página de agregar-producto.html permite rellenar un formulario a los productores para agregar sus productos a la base de datos que se conecta la página. En esta página, los siguientes datos a rellenar son obligatorios y algunos deben cumplir con ciertas condiciones (validaciones del front-end):
* Tipo de Producto
* Producto: solo se puede seleccionar un producto si es que se escoge el tipo de producto antes.
* Fotos del producto: se deben colocar de 1 a 3 fotos del producto. A medida que el usuario coloque un archivo, aparecerá otro input abajo del ya usado para poder subir otro archivo. Solo aparecerán 3 inputs de archivo, pues es el máximo de fotos deseadas.
* Región
* Comuna: solo se podrá elegir una comuna si es que se escogió una región antes.
* Nombre del productor: Debe ser un nombre (o nombre completo) que tenga entre 3 a 80 caracteres, o más bien letras (el input solo debe contener letras y/o espacios).
* Email: Debe cumplir con el formato de string de letras y números, seguido de @, seguido de un dominio de correo válido como gmail, yahoo o outlook, seguido de un . y finalizado con com o cl.

Los datos como descripción del producto y número celular del productor son opcionales, pero si el cliente decide llenar el input de número celular deberá cumplir con el formato para este dato, el cual corresponde a un string de 8 números.

Todos los datos no completados o que no cumplen con el formato deseado serán notificados por una alerta y no dejarán 'agregar' el producto.

Además de las validaciones en el front-end, una vez los datos sean enviados al servidor se valida que todos estos esten en la base de datos contenida y que efectivamente cumplan con las validaciones anteriores. Los archivos deben cumplir con las extensiones validas que son "png", "jpg", "jpeg", "gif". Si uno de estas validaciones en el back-end no se cumple, entonces el servidor envía un mensaje que se mostrará al principio del formulario diciendo en cual de los datos pedidos se encontró el error.

La página de agregar-pedido.html permite rellenar un formulario a los compradores para pedir los productos que desean. Es por esto que los datos pedidos son los mismos a los de agregar-producto.html y con las mismas condiciones, con la diferencia de que en esta página no se pedirán fotos del producto.

La página ver-productos muestra una tabla de productos con la siguiente información: tipo, nombre, región, comuna, y foto(s) del o los productos. Estos datos son los que se encuentran en la base de datos del servidor. Además, en cada línea de la tabla que contiene información de un producto se puede hacer clic y esto llevará a la página informacion-producto.html donde saldrá toda la información colocada en el formulario de agregar-producto para el producto clickeado.

De forma similar, ver-pedidos mostrará una tabla de pedidos inventados con la información: tipo, nombre, región, comuna de los productos pedidos y nombre del comprador del pedido. En cada línea, se podrá cliquear para dirigirse a infoprmacion-pedido.html donde saldrán todos los datos pedidos en agregar-pedido.html para un pedido inventado.

Cabe mencionar que desde todas las páginas se podrá dirigir al índice gracias a un botón en el incio de cada una que al apretarlo redirecciona a index.html.

### Contacto
Rodrigo Díaz Maturana - rodrigo.diaz.m@ug.uchile.cl

### Agradecimientos
Todas las imágenes del proyecto fueron obtenidas en https://www.pexels.com/es-es/buscar/cultivos/?size=large&orientation=landscape, una página web dedicada a subir fotos gratuitas y sin licencia.