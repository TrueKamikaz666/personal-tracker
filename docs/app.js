document.addEventListener("DOMContentLoaded", function () {

    fetch("latest.json")
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {

            document.getElementById("updated").textContent =
                "Última actualización: " + data.updated;

            renderSection("monster-high", data.monsterHigh);
            renderSection("funko", data.funko);

        })
        .catch(function (error) {
            console.error("Error cargando datos:", error);
        });

});


function renderSection(id, items) {

    var container = document.getElementById(id);

    if (!items || items.length === 0) {
        container.innerHTML = "<p>No hay datos disponibles</p>";
        return;
    }

    var html = "";

    items.forEach(function (item) {

        html += "<div class='item'>";
        html += "<h3>" + item.name + "</h3>";

        if (item.price) {
            html += "<p>Precio: " + item.price + "</p>";
        }

        if (item.url) {
            html += "<a href='" + item.url + "' target='_blank'>Ver producto</a>";
        }

        html += "</div>";

    });

    container.innerHTML = html;
}
