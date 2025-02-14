// Función para actualizar la lista de pedidos
function actualizarPedidos() {
    // Hacer una solicitud AJAX al servidor
    fetch('/admin/menu/pedido/')  // Ruta de la página de pedidos en el admin
        .then(response => response.text())  // Obtener el contenido de la respuesta
        .then(data => {
            // Extraer la tabla de pedidos del HTML recibido
            const parser = new DOMParser();
            const doc = parser.parseFromString(data, 'text/html');
            const nuevaTabla = doc.querySelector('#result_list');  // ID de la tabla de pedidos

            // Reemplazar la tabla actual con la nueva tabla
            if (nuevaTabla) {
                const tablaActual = document.querySelector('#result_list');
                tablaActual.innerHTML = nuevaTabla.innerHTML;
            }
        })
        .catch(error => console.error('Error al actualizar pedidos:', error));
}

// Actualizar la lista de pedidos cada 5 segundos (5000 milisegundos)
setInterval(actualizarPedidos, 5000);