/**
 * Redirige hacia la información-pedido.
 */
const redirect_to_info = (id) => {
    fetch(`/informacion-pedido/${id}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ id: id })
    })
    .then(response => {
        if (response.ok) {
            window.location.href = `/informacion-pedido/${id}`;
        } else {
            throw new Error('La solicitud no fue exitosa');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        // Manejar el error, si es necesario
    });
};