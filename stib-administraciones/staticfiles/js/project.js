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

});
