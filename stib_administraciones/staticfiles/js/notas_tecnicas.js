$(function() {
     $('#aceptar_nota_tecnica').click(function(){
        $("#estado").val("2");
        $("#estado_name").html("Aceptar");
        $("#modal_nota_tecnica_estado").modal("show");
    });

    $('#cancelar_nota_tecnica').click(function(){
        $("#estado").val("4");
        $("#estado_name").html("Cancelar");
        $("#modal_nota_tecnica_estado").modal("show");
    });

    $('#pendiente_nota_tecnica').click(function(){
        $("#estado").val("3");
        $("#estado_name").html("Mantener Pendiente");
        $("#modal_nota_tecnica_estado").modal("show");
    });
});