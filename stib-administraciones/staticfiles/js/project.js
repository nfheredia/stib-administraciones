$(function() {

    $('#side-menu').metisMenu();

    $(".fancybox").fancybox({
		openEffect	: 'none',
		closeEffect	: 'none'
	});

	$("#todas-las-fotos").click(function(){
        $("a.no-display")[0].click();
	});

});
