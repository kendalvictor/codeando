/* Codigo de validacion v3.2 Desarrollado por mi :3  */
function validar(id, paceholder, tipo, error) {
				
				var valido=true;
				var value = $(id).val();
				if(value=='' || value==$(id).attr('placeholder') || value==null){
					valido=false; $(id).addClass(error);
					$(id+"_error").css('display','block');
				}
				else
				{
					$(id+"_error").css('display','none');
					$(id).removeClass(error);
					if(tipo=="mail") {
							var emailReg = /^([\w-\.]+@([\w-]+\.)+[\w-]{2,8})?$/;
							if(!emailReg.test(value)){ valido=false; $(id).addClass(error); $(id+"_error").css('display','block');}
							else { $(id).removeClass(error); $(id+"_error").css('display','none');}
					}
					if(tipo=="file") {
							myfile= $(id).val();
							$('#conten_file_name').html(myfile.split('\\').pop());
							var ext = myfile.split('.').pop();
							if(ext=="pdf" || ext=="docx" || ext=="doc"){valido=true; $(id).removeClass(error); $(id+"_error").css('display','none');}
							else{valido=false; $(id).addClass(error); $(id+"_error").css('display','block'); alert("Solo se acepta .pdf .doc .docx");}
					}
				}
				$(id).attr("onkeyup","wcc_verify(this.id);");
				return valido;
			}

function validarSelectLi(id, paceholder, tipo, error) {
				console.log(id);
				var valido=true;
				var value = $(id).val();
				if(value=='' || value==$(id).attr('placeholder') || value==null) {
					valido=false; $(id).parent("li").addClass(error);
					$(id+"_error").css('display','block');
				}
				else
				{
					$(id+"_error").css('display','none');
					$(id).parent("li").removeClass(error);
				}
				$(id).attr("onchange",'validarSelectLi("'+id+'","","text","error");');
				return valido;
			}

function wcc_verify(id){
	id = "#"+id
	error = "error"
	tipo = $(id).attr('type')
	var value = $(id).val();
	if(value=='' || value==$(id).attr('placeholder') || value==null) {
		valido=false; $(id).addClass(error);
		$(id+"_error").css('display','block');
	}
	else
	{
		$(id+"_error").css('display','none');
		$(id).removeClass(error);
		if(tipo =="email") {
				var emailReg = /^([\w-\.]+@([\w-]+\.)+[\w-]{2,4})?$/;
				if(!emailReg.test(value)){ valido=false; $(id).addClass(error); $(id+"_error").css('display','block');}
				else { $(id).removeClass(error); $(id+"_error").css('display','none');}
		}
		if(tipo=="file") {
				myfile= $(id).val();
				$('#conten_file_name').html(myfile.split('\\').pop());
				var ext = myfile.split('.').pop();
				if(ext=="pdf" || ext=="docx" || ext=="doc"){valido=true; $(id).removeClass(error); $(id+"_error").css('display','none');}
				else{valido=false; $(id).addClass(error); $(id+"_error").css('display','block'); alert("Solo se acepta .pdf .doc .docx");}
		}
	}
	$(id).attr("onkeyup","wcc_verify(this.id);");
}

$( "#wSuscriptForm" ).submit(function( event ) {


	var valido=true;
	valido4 = validar('#wcc_email_suscript', 'Email*', 'mail', 'error');
		if(valido4) {
			valido = true;
			 $('.w-boton').css('display','none');
			 $('#mensaje-form').css('display','block');
			 $('#mensaje-form').html("Su mensaje esta siendo enviado ...");
		}
		else{
				valido = false;
		}
	return valido;
});

$( "#idcontactotra" ).submit(function( event ) {
	var valido=true;
	valido1 = validar('#wNombreJob', '', 'text', 'error');
	valido4 = validar('#archivo', '', 'file', 'error');
		if( valido1 && valido4 ) {
			valido = true;
			 $('.w-boton').css('display','none');
			 $('#mensaje-form').css('display','block');
			 $('#mensaje-form').html("Su mensaje esta siendo enviado ...");
		}
		else{
				valido = false;
		}
	return valido;
});

$( "#wBusquedaHomeForm" ).submit(function( event ) {


	var valido=true;
	valido1 = validarSelectLi('#wmarca_hf', 'Email*', 'text', 'error');
	valido2 = validarSelectLi('#wmodelo_hf', 'Email*', 'text', 'error');
	valido3 = validarSelectLi('#wuso_hf', 'Email*', 'text', 'error');
		if(valido1 && valido2 && valido3) {
			valido = true;
			 $('.w-boton').css('display','none');
			 $('#mensaje-form').css('display','block');
			 $('#mensaje-form').html("Su mensaje esta siendo enviado ...");
		}
		else{
				valido = false;
		}
	return valido;
});

$( "#wTopFormBattery" ).submit(function( event ) {


	var valido=true;
	valido1 = validarSelectLi('#wMarcaSelectTopForm', 'Email*', 'text', 'error');
	valido2 = validarSelectLi('#wModelSelectTopForm', 'Email*', 'text', 'error');
	valido3 = validarSelectLi('#wUsoSelectTopForm', 'Email*', 'text', 'error');
		if(valido1 && valido2 && valido3) {
			valido = true;
			 $('.w-boton').css('display','none');
			 $('#mensaje-form').css('display','block');
			 $('#mensaje-form').html("Su mensaje esta siendo enviado ...");
		}
		else{
				valido = false;
		}
	return valido;
});

$( "#wTopFormBattery2" ).submit(function( event ) {
	var valido=true;
	valido1 = validarSelectLi('#wMarcaSelectTopForm', 'Email*', 'text', 'error');
	valido2 = validarSelectLi('#wModelSelectTopForm', 'Email*', 'text', 'error');
	
		if(valido1 && valido2) {
			valido = true;
			 $('.w-boton').css('display','none');
			 $('#mensaje-form').css('display','block');
			 $('#mensaje-form').html("Su mensaje esta siendo enviado ...");
		}
		else{
				valido = false;
		}
	return valido;
});

$('.wMarcaSelect').change(function(){
	var formData = {};
	if($(this).val() == ""){
		$('.wModelSelect').empty();
		$('.wModelSelect').html('<option value="">-------------</option>');
		$('.wModelSelect').change();
	}
	else{
	formData.marca = $(this).val();
	$.ajax({
			url: "/es/mpm/",
			data: formData,
			type: "POST",
			dataType: "json",
		}).done(function( data ) {
			$('.wModelSelect').empty();
			$.each(data,function (index, modelo){
				$('<option data-have="'+modelo["have"]+'" value="'+modelo["nombre"]+'">'+modelo["nombre"]+'</option>').appendTo('.wModelSelect');
			});
			$('.wModelSelect').change();
		});
	}
});
$('.wMarcaSelectLM').change(function(){
	var formData = {};
	if($(this).val() == ""){
		$('.wModelSelectLM').empty();
		$('.wModelSelectLM').html('<option value="">-------------</option>');
		$('.wModelSelectLM').change();
	}
	else{
	formData.marca = $(this).val();
	$.ajax({
			url: "/es/mpm_lm/",
			data: formData,
			type: "POST",
			dataType: "json",
		}).done(function( data ) {
			$('.wModelSelectLM').empty();
			$.each(data,function (index, modelo){
				$('<option value="'+modelo+'">'+modelo+'</option>').appendTo('.wModelSelectLM');
			});
			$('.wModelSelectLM').change();
		});
	}
});
$('.wMarcaSelectBM').change(function(){
	var formData = {};
	if($(this).val() == ""){
		$('.wModelSelectBM').empty();
		$('.wModelSelectBM').html('<option value="">-------------</option>');
		$('.wModelSelectBM').change();
	}
	else{
	formData.marca = $(this).val();
	$.ajax({
			url: "/es/mpm_bm/",
			data: formData,
			type: "POST",
			dataType: "json",
		}).done(function( data ) {
			$('.wModelSelectBM').empty();
			$.each(data,function (index, modelo){
				$('<option value="'+modelo+'">'+modelo+'</option>').appendTo('.wModelSelectBM');
			});
			$('.wModelSelectBM').change();
		});
	}
});

// $( document ).ready(function(){
// 	$(".b21-descripcion .item-tab").each(function(){
// 		$(this).css("height",$(this).height()+"px");
// 	});
// });
