$(document).ready(function(){

    /* **************************************************
        Autocomplete de productos
        - utilizamos jquery autocomplete
    *************************************************** */
    $( "#id_producto_nombre" ).autocomplete({
        source: "/notificaciones/search-autocomplete?obj=Productos",
        selectFirst:true,
        minLength:3,
        select: function(event,ui) {
            $("#id_producto").val(ui.item.id)
        }
    });

    /* **************************************************
        Autocomplete de servicios
        - utilizamos jquery autocomplete
    *************************************************** */
    $( "#id_servicio_nombre" ).autocomplete({
        source: "/notificaciones/search-autocomplete?obj=Servicios",
        selectFirst:true,
        minLength:3,
        select: function(event,ui) {
            $("#id_servicio").val(ui.item.id)
        }
    });

	/* **************************************************
        Autocomplete de edificios
        - utilizamos jquery autocomplete
    *************************************************** */
    $( "#id_edificio_nombre" ).autocomplete({
        source: "/notificaciones/search-autocomplete-edificios",
        selectFirst:true,
        minLength:3,
        select: function(event,ui) {
            $("#id_edificio").val(ui.item.id)
        }
    });

});
