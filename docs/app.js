fetch("latest.json")
    .then(function(response) {
        return response.json();
    })
    .then(function(data) {

        var updateElement = document.getElementById("last-update");

        if (updateElement) {
            updateElement.textContent =
                "Última actualización: " + data.updated;
        }

        console.log("Datos cargados:", data);

    })
    .catch(function(error) {

        console.error("Error cargando datos:", error);

    });
