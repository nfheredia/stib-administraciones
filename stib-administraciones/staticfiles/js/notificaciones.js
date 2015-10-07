$(function() {
     $('#aceptar_notificacion').click(function(){
        $("#estado").val("2");
        $("#estado_name").html("Aceptar");
        $("#modal_envio_cambio_estado").modal("show");
    });

    $('#cancelar_notificacion').click(function(){
        $("#estado").val("4");
        $("#estado_name").html("Cancelar");
        $("#modal_envio_cambio_estado").modal("show");
    });
});