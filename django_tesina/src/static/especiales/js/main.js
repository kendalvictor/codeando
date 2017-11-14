

		/*MENU*/
		$(".icon-menu").click(function(event) {
			event.preventDefault();
			$("#wrapper").toggleClass('wrapper-active');

		});

		/*HEADER*/
		$(".ul-menu-main >li.sub-menu >a").click(function(event) {
			/* Act on the event */
			event.preventDefault();
			$(".ul-menu-main >li.sub-menu").removeClass('active')
			$(this).closest('li').addClass('active');
			$(".menu-secund").stop(false).slideUp();
			$(this).closest('li').find('.menu-secund').stop(false).slideToggle( "300", function() {
			    // Animation complete.
			  });
		});

		$(".container-toggle").click(function(event) {
			/* Act on the event */
			$(this).find(".toggle-card").toggleClass('toggle-card-active');
		});

		function hide_pop_up(){
			$(".pop-up").find('.pop-up-content').removeClass('pop-up-content-active');
			$(".pop-up").removeClass('pop-up-active');
		}
		$('body').on('click', '.open-pop-up', function(event) {

			/* Act on the event */
			event.preventDefault();

			var class_open = $(this).attr('data-pop-up');
			// $(class_open).find(".pop-up-content").css({
			// 	'top': alto
			// })
			if (class_open) {
				var class_open = "." + class_open
				$(class_open).toggleClass('pop-up-active');
				setTimeout(function(){
					console.log("entro")
				 	$(class_open).find('.pop-up-content').toggleClass('pop-up-content-active');
				}, 200);

			}else{
				$(".pop-up").toggleClass('pop-up-active');
				setTimeout(function(){
					console.log("entro")
				 	$('.pop-up .pop-up-content').toggleClass('pop-up-content-active');
				}, 200);
			}

		});
		$('body').on('click', '.pop-up-close', function(event) {

			/* Act on the event */
			event.preventDefault();
		 	$(".pop-up").find('.pop-up-content').removeClass('pop-up-content-active');
			setTimeout(function(){
				$(".pop-up").removeClass('pop-up-active');
			}, 300);
		});
		$('body').on('click', '.close_pop_up', function(event) {

			/* Act on the event */
			event.preventDefault();
		 	$(".pop-up").find('.pop-up-content').removeClass('pop-up-content-active');
			setTimeout(function(){
				$(".pop-up").removeClass('pop-up-active');
			}, 300);
		});
		function show_loader(){

			$("#overlay").show()
		}
		function hide_loader(){
			$("#overlay").hide()
		}


		function hide_notify(){
			$(".notify").removeClass('notify-activate')
		}



		function show_notify(data){
			var data = data
			var li = ""
			$(".notify ul li").remove()
			$(".notify").addClass("notify--danger")
			$(".notify").removeClass("notify--success")
			if (data) {
				$.each(data, function(val, index) {
					 /* iterate through array or object */
					 li += "<li>"+index+"</li>"
				});
				$(".notify ul").append(li)
				$(".notify").addClass('notify-activate')
				setTimeout(function(){
					hide_notify()
				}, 4000);
			}
		}


		function show_notify_success(data){
			var data = data
			var li = ""
			$(".notify ul li").remove()
			$(".notify").removeClass("notify--danger")
			$(".notify").addClass("notify--success")
			if (data) {
				$.each(data, function(val, index) {
					 /* iterate through array or object */
					 li += "<li>"+index+"</li>"
				});
				$(".notify ul").append(li)
				$(".notify").addClass('notify-activate')
				setTimeout(function(){
					hide_notify()
				}, 4000);
			}
		}

		function show_success(titulo, texto){
			$(".message-pop--success").addClass('message-pop-active')
			if (titulo) {
				$(".message-pop--success .message-pop-text h3").text(titulo)

			};
			if (texto) {
				$(".message-pop--success .message-pop-text .text").text(texto)

			};
			setTimeout(function(){
			 	$(".message-pop--success .message-pop-content").addClass('message-pop-content-active');
			}, 200);

		}
		function show_danger(titulo, texto){
			$(".message-pop--danger").addClass('message-pop-active')
			if (titulo) {
				$(".message-pop--danger .message-pop-text h3").text(titulo)

			};
			if (texto) {
				$(".message-pop--danger .message-pop-text .text").text(texto)

			};
			setTimeout(function(){
			 	$(".message-pop--danger .message-pop-content").addClass('message-pop-content-active');
			}, 200);

		}
		function show_warning(titulo, texto){
			$(".message-pop--warning").addClass('message-pop-active')
			if (titulo) {
				$(".message-pop--warning .message-pop-text h3").text(titulo)

			};
			if (texto) {
				$(".message-pop--warning .message-pop-text .text").text(texto)

			};
			setTimeout(function(){
			 	$(".message-pop--warning .message-pop-content").addClass('message-pop-content-active');
			}, 200);

		}
		function hide_message(){
			$('.message-pop .message-pop-content').removeClass('message-pop-content-active');
			setTimeout(function(){
				$('.message-pop').removeClass('message-pop-active')
			}, 400);
		}
		$(".message-pop-close").click(function(event) {
			/* Act on the event */
			event.preventDefault()
		 	$('.message-pop').find(".message-pop-content").removeClass('message-pop-content-active');
			setTimeout(function(){
				$('.message-pop').removeClass('message-pop-active')
			}, 400);
		});