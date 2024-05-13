/**
 * Agranda la imagen de informacion-producto.
 */
const resize = (id, width, height) => {
    console.log(width == '640')
    console.log(height == '480')
    if (width == '640' && height == '480') {
        width = '1280';
        height = '1024';
    } else {
        width = '640';
        height = '480';
    }

    fetch(`/informacion-producto/${id}/${width}/${height}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ id: id })
    })
    .then(response => {
        if (response.ok) {
            window.location.href = `/informacion-producto/${id}/${width}/${height}`;
        } else {
            throw new Error('La solicitud no fue exitosa');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        // Manejar el error, si es necesario
    });
};