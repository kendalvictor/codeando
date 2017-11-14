$(function() {
	/* modelo clases generales */

		$('.block-general').wrap('<div class="general-wrapper"></div>');
		$('<div class="inner-general"></div>').appendTo('body');
		$('<h2 class="name-dev"></h2>').appendTo('.inner-general');
		$('.general-wrapper').appendTo('.inner-general');
		$('<span class="btn-copy">Copiar código</span>').prependTo('.general-wrapper');

	    var copy_sel = $('.btn-copy');
	    // Disables other default handlers on click (avoid issues)
	    copy_sel.on('click', function(e) {
	        e.preventDefault();
	    });

	    // Apply clipboard click event
	    copy_sel.clipboard({
	        path: '/static/js/mg/jquery.clipboard.swf',
	        copy: function() {
	            var this_sel = $(this);
	            return this_sel.closest('.general-wrapper').find('.block-general').html();
	        }
	    });

			$( window ).on( "load", function() {
			$('.wrapp-iframe-general').each(function(index, el) {
				var alto = $(el).contents().height();
				$(el).contents().find('body').css('overflow', 'hidden');			
				var name = $(el).attr('src');
				// console.log(name);
				var nameDev = name.replace('.html',':');		
				$(el).css('height', alto);
				$(el).contents().find('.name-dev').text(nameDev);

			});
    });

});
