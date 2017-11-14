(function($) {
	$(document).ready(function() {
		$(".url_seo .grp-readonly").each(function(){
			$(this).html();
			console.log($(this).html());
			$(this).parent().append('<a class="wSEOLink" href="'+$(this).html()+'" target="_blank" style="margin-left: 5px;">Abrir Enlace </a>');
		});
	});
})(grp.jQuery);

(function($) {
	$(document).ready(function() {
		$(".cv .grp-readonly").each(function(){
			$(this).html();
			console.log($(this).html());
			$(this).parent().append('<a class="wSEOLink" href="'+MEDIA_URL+$(this).html()+'" target="_blank" style="margin-left: 5px;">Abrir Archivo</a>');
		});
	});
})(grp.jQuery);