document.addEventListener("DOMContentLoaded", function () {

    fetch("latest.json")
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {

            var updateElement = document.getElementById("last-update");

            if (updateElement) {
                updateElement.textContent =
                    "Última actualización: " +
                    new Date(data.updated).toLocaleString("es-ES");
            }

            renderProducts(
                "monster-high",
                data.monsterHigh
            );

            renderProducts(
                "funko",
                data.funko
            );

        })
        .catch(function (error) {

            console.error(
                "Error cargando datos:",
                error
            );

        });

});


function renderProducts(containerId, products) {

    var container =
        document.getElementById(containerId);

    if (!container) {
        return;
    }

    if (!products || products.length === 0) {

        container.innerHTML =
            "<p>No hay productos.</p>";

        return;

    }

    var html = "";

    products.forEach(function (product) {

        html += "<div class='item'>";

        html += "<h3>" +
            product.name +
            "</h3>";

        if (product.store) {

            html += "<p><strong>Tienda:</strong> " +
                product.store +
                "</p>";

        }

        if (product.price) {

            html += "<p><strong>Precio:</strong> " +
                product.price +
                "</p>";

        }

        if (product.url) {

            html +=
                "<p><a href='" +
                product.url +
                "' target='_blank'>Ver producto</a></p>";

        }

        html += "</div>";

    });

    container.innerHTML = html;

}
