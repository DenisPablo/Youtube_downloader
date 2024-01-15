$(document).ready(function () {

    // Mostrar el div al enviar el formulario
    $("#descarga").submit(function (event) {
        $("#carga").show();
        setTimeout(function() {
            // Ocultar el div después de 10 segundos
            $("#carga").hide();
        }, 5000);
    });
});