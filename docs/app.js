fetch("latest.json")
    .then(function(response) {
        return response.json();
    })
    .then(function(data) {

        document.getElementById("last-update").textContent =
            "Última actualización: " + data.updated;

        console.log(data);

    })
    .catch(function(error) {

        console.error("Error cargando latest.json:", error);

    });
