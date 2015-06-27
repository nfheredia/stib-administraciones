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
        Configuracion Tinymce editor
    --------------------------------------------- */
    tinymce.init({
        selector: "textarea",
        plugins: [
            "advlist autolink lists link image charmap print preview anchor",
            "searchreplace visualblocks code fullscreen",
            "insertdatetime media table contextmenu paste"
        ],
        toolbar: "insertfile undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image"
    });

});
