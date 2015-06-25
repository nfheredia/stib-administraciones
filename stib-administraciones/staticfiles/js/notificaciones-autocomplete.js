$(document).ready(function(){

    /* **************************************************
        Autocomplete de productos
        - utilizamos jquery autocomplete
    *************************************************** */
    $( "#id_producto_nombre" ).autocomplete({
        source: "/notificaciones/search_productos_autocomplete",
        selectFirst:true,
        minLength:3,
        select: function(event,ui) {
            $("#id_producto").val(ui.item.id)
        }
    });

});