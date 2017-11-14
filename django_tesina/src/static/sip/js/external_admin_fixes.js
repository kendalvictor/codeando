(function($) {
	console.log("Rawr :3");
	var arrayLang = ["es","en"]
	var Lang_STATUS = "ALL"
	$(document).ready(function() {
		$(".url_seo .grp-readonly").each(function(){
			$(this).html();
			console.log($(this).html());
			$(this).parent().append('<a class="wSEOLink" href="'+$(this).html()+'" target="_blank" style="margin-left: 5px;">Abrir Enlace </a>');
		});
		// $('div[class*=_en]').css("display", "none");
		$('#grp-content-title').append('<ul class="grp-object-tools wLangList"><li>\
											<a class="wChangeLang wEs" data-wlang="es">ES</a>\
											<a class="wChangeLang wEn" data-wlang="en">EN</a>\
											<a class="wChangeLang wAll wLangActive" data-wlang="all">ALL</a>\
											</li></ul>');
		$('.wChangeLang').click(function(){
			$('.wChangeLang').removeClass('wLangActive');
			$(this).addClass('wLangActive');
			wChangeLang($(this).attr('data-wlang'));
		});
		function wChangeLang(LangToShow){
			if (LangToShow != "all") {
				for (i = 0; i < arrayLang.length; i++) { 
					if(arrayLang[i]==LangToShow){
						$('div[class*=_'+arrayLang[i]+']').removeClass('wLangRowItem');
						$('div[class*=-'+arrayLang[i]+']').removeClass('wLangRowItem');
					}else{
						$('div[class*=_'+arrayLang[i]+']').addClass('wLangRowItem');
						$('div[class*=-'+arrayLang[i]+']').addClass('wLangRowItem');
					}
				}
			}else{
				for (i = 0; i < arrayLang.length; i++) { 
					$('div[class*=_'+arrayLang[i]+']').removeClass('wLangRowItem');
					$('div[class*=-'+arrayLang[i]+']').removeClass('wLangRowItem');
				}				
			}
			
		}
	});

})(grp.jQuery);
