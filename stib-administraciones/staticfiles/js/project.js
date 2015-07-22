$(function() {

    $('#side-menu').metisMenu();

    $(".fancybox").fancybox({
		openEffect	: 'none',
		closeEffect	: 'none'
	});

	$("#todas-las-fotos").click(function(){
        $("a.no-display")[0].click();
	});

	/* --------------------------------------------
        Lanzar modal de recursos de edificios
    --------------------------------------------- */
    $('#open_recursos_modal').click(function(){
        $("#recursos_modal").modal("show");
    });

    /* --------------------------------------------
        Open bootstrap pop-over
    --------------------------------------------- */
    $('.open_popover').popover({
        animation: true,
        html: true
    });

	$('#open_notificaciones_modal').click(function(){
        $("#notificaciones_modal").modal("show");
    });

     /* ---------------------
     -- common datepicker --
     ----------------------- */
    $('.dateinput').datepicker({
        format: 'dd/mm/yyyy'
    }).on('changeDate', function(ev){
        // -- hide dropdown when change dates
        $('.dropdown-menu').hide();
    });

    /* --------------------------------------------
        Autocomplete de edificios que pertencen
        a la administracion logueada
        - utilizamos jquery autocomplete
    ----------------------------------------------- */
    $("#id_edificio_nombre").autocomplete({
        source: "/edificios/search/autocomplete/edificios/administracion",
        selectFirst:true,
        minLength:3,
        open: function() { $('#ui-id-1').width(250) },
        select: function(event,ui) {
            $("#id_edificio").val(ui.item.id)
        }
    });

    /* **************************************************
        Autocomplete de adminsitraciones
        - utilizamos jquery autocomplete
    *************************************************** */
    $( "#id_administracion_nombre_comercial" ).autocomplete({
        source: "/perfiles/autocomplete/nombre/comercial",
        selectFirst:true,
        minLength:3,
        select: function(event,ui) {
            $("#id_usuario").val(ui.item.user_id)
        }
    });
});
