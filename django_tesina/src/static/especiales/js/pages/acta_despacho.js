/**
 * Created by vvillacorta on 22/05/2017 06:08:21
 */
var notificaciones_error = [];

function show_success_2(titulo, texto){
    $(".message-pop--success-2").addClass('message-pop-active')
    if (titulo) {
        $(".message-pop--success-2 .message-pop-text h3").text(titulo)

    };
    if (texto) {
        $(".message-pop--success-2 .message-pop-text .text").text(texto)

    };
    setTimeout(function(){
        $(".message-pop--success-2 .message-pop-content").addClass('message-pop-content-active');
    }, 200);

}

function show_danger_2(titulo, texto){
    $(".message-pop--danger_2").addClass('message-pop-active')
    if (titulo) {
        $(".message-pop--danger_2 .message-pop-text h3").text(titulo)

    };
    if (texto) {
        $(".message-pop--danger_2 .message-pop-text .text").text(texto)

    };
    setTimeout(function(){
        $(".message-pop--danger_2 .message-pop-content").addClass('message-pop-content-active');
    }, 200);

}

function clear_fom_acta(){
  $("#id_observaciones").val("");
  $("#id_recepciono").val("");
  $("#id_entrego").val("");
  $("#id_direccion").val("");
  $("#id_estacion").val("");
  $("#id_contratista").val("");
  $("#id_fechaacta").val("");
  $("#id_proyecto").select2("destroy");
  $("#id_proyecto").val("489");
  $("#id_proyecto").select2();
}

function deshabilitar_form_acta(){
  $("#id_observaciones").attr('disabled', 'disabled');
  $("#id_recepciono").attr('disabled', 'disabled');
  $("#id_entrego").attr('disabled', 'disabled');
  $("#id_direccion").attr('disabled', 'disabled');
  $("#id_estacion").attr('disabled', 'disabled');
  $("#id_contratista").attr('disabled', 'disabled');
  $("#id_fechaacta").attr('disabled', 'disabled');
  $("#id_proyecto").attr('disabled', 'disabled');
  $.each($('#id_panel_materiales input[type="checkbox"]'), function() {
      var $row = $(this);
      $row.attr('disabled', 'disabled');
  });
}
function habilitar_form_acta(){
  $("#id_observaciones").removeAttr('disabled');
  $("#id_recepciono").removeAttr('disabled');
  $("#id_entrego").removeAttr('disabled');
  $("#id_direccion").removeAttr('disabled');
  $("#id_estacion").removeAttr('disabled');
  $("#id_contratista").removeAttr('disabled');
  $("#id_fechaacta").removeAttr('disabled');
  $("#id_proyecto").removeAttr('disabled');
  $.each($('#id_panel_materiales input[type="checkbox"]'), function() {
      var $row = $(this);
      $row.removeAttr('disabled');
      $row.prop("checked", false);
  });
}

function remove_errordata_form_acta(){
  $("#id_recepciono").removeClass('error-data');
  $("#id_entrego").removeClass('error-data');
  $("#id_direccion").removeClass('error-data');
  $("#id_estacion").removeClass('error-data');
  $("#id_contratista").removeClass('error-data');
  $("#id_proyecto").removeClass('error-data');
  $("#id_fechaacta").removeClass('error-data');
}

function clean_form_all_despacho() {
    remove_errordata_form_acta();
    clear_fom_acta();
    habilitar_form_acta();
    $("#section_carga_acta").hide();
    $("#id_anular_acta").hide();
    $("#id_xport_pdf_acta").hide();
    $("#id_guardar_acta").show();
    $("#name_acta_despacho").html("");
    $("#id_load_acta_despacho").removeData("iddacta");
    $("#id_load_acta_despacho").data("iddacta", "");
    $("#id_pdfseguimiento").val("");
}

function soloNumeros(e){
    var key = window.Event ? e.which : e.keyCode;
    return (key >= 48 && key <= 57 || key==8)
}

function validate_pdf_despacho(){
  var extensiones = ["pdf"];
  var mandar_submit = true;
  if($("#id_pdfseguimiento").val()){
      var extension_image_tmi = String($("#id_pdfseguimiento").val()).toLowerCase().split(".")[1];
      if(extensiones.indexOf(extension_image_tmi) == -1){
          mandar_submit = false
      }
      notificaciones_error.push("Formato 'pdf' no detectado")
  }else{
      mandar_submit = false;
      notificaciones_error.push("Seleccione el acta a cargar")
  }
  return mandar_submit;
}

function load_data_material(iddespacho, nroacta){
    var enabled_view = null;
    $.ajax({
        url: URLS_GET_INFO_MATERIAL,
        type: 'POST',
        dataType: 'json',
        data: {
            'iddespacho': iddespacho,
            'nroacta': nroacta
        },
        success: function(data){
            if(data.error){
                show_notify([data.error])
            }else{
                var list_element = data.result;
                console.log("## ", list_element);
                console.log("## ", list_element.length);
                if(list_element.length > 0){
                    enabled_view = true;
                    $("#tbody_info_material").empty();
                    $.each(list_element, function (index, value){
                        var chekor = '';
                        if(value[0]){
                            chekor = 'checked'
                        }
                        var deshabilitado = '';
                        if(nroacta != ''){
                            deshabilitado = 'disabled="disabled"'
                        }
                        var html_tbody = '<tr data-iddtipomaterial="'+ value[1] +'" data-namematerial="'+ value[2] +'">' +
                            '<td><center><input type="checkbox" class="material_elegido" ' + chekor + ' ' + deshabilitado + '/></center></td>' +
                            '<td><center>' + value[2] + '</center></td></tr>';
                        $("#tbody_info_material").append(html_tbody)
                    });
                }
            }
        }
    });
    return enabled_view
}

function view_acta_existente() {
    $("#section_carga_acta").show();
    $("#id_anular_acta").show();
    $("#id_xport_pdf_acta").show();
    $("#id_guardar_acta").hide();
}

function validate_filtros(){
      var correct = true;
      var error_html = '(*)';
      $('.col-movil-100').find('.error').html("");
      $('.col-movil-100').find('.select2-selection').removeClass('error-data');
      $("#id_panel_datos_generales").find('input').removeClass('error-data');
      if (parseInt($('#id_proyecto').val()) == 0){
          correct = false;
          $('#id_proyecto').closest('.col-movil-100').find('.error').html(error_html);
          $('#id_proyecto').closest('.form-group').find('.select2-selection').addClass('error-data');
      }
      if ($('#id_contratista').val() == ''){
          correct = false;
          $('#id_contratista').closest('.col-movil-100').find('.error').html(error_html);
          $('#id_contratista').addClass('error-data');
      }
      if ($('#id_estacion').val() == ''){
          correct = false;
          $('#id_estacion').closest('.col-movil-100').find('.error').html(error_html);
          $('#id_estacion').addClass('error-data');
      }
      if ($('#id_direccion').val() == ''){
          correct = false;
          $('#id_direccion').closest('.col-movil-100').find('.error').html(error_html);
          $('#id_direccion').addClass('error-data');
      }
      if ($('#id_entrego').val() == ''){
          correct = false;
          $('#id_entrego').closest('.col-movil-100').find('.error').html(error_html);
          $('#id_entrego').addClass('error-data');
      }
      if ($('#id_direccion').val() == ''){
          correct = false;
          $('#id_recepciono').closest('.col-movil-100').find('.error').html(error_html);
          $('#id_recepciono').addClass('error-data');
      }
      if ($('#id_fechaacta').val() == ''){
          correct = false;
          $('#id_fechaacta').closest('.col-movil-100').find('.error').html(error_html);
          $('#id_fechaacta').addClass('error-data');
      }
      if(!correct){
          notificaciones_error.push("Complete los campos requeridos")
      }
      return correct;
  }

function validate_material(){
  var material_valido = true;
  var cantidad_checkeados = $("#id_panel_materiales").find('input[type="checkbox"]:checked').length;
  if(cantidad_checkeados < 1){
      material_valido = false;
      notificaciones_error.push("Debe llenar al menos en un tipo de material")
  }
  return material_valido
}

function get_material_chekeado(){
    var materiales_chekeados = $("#id_panel_materiales").find('input[type="checkbox"]:checked');
    var serie = '';
    $.each(materiales_chekeados, function() {
        var idd = $(this).closest("tr").data("iddtipomaterial");
         if(serie){
              serie += "," + idd
          }else{
              serie += idd
          }
    });
    return serie
}

$("#id_guardar").on('click', function(e){
  e.preventDefault();
  var iddespacho = $(this).data("iddespacho");
  var bit_datos_generales = validate_filtros();
  var bit_material = validate_material();

  if (bit_datos_generales && bit_material){
      $.ajax({
         url: URL_SAVE_ACTA,
         type: 'post',
         data: {
             "observaciones" : $('#id_observaciones').val(),
             "recepciono" : $('#id_recepciono').val(),
             "entrego" : $('#id_entrego').val(),
             "direccion" : $('#id_direccion').val(),
             "estacion" : $('#id_estacion').val(),
             "contratista" : $('#id_contratista').val(),
             "fechaacta" : $('#id_fechaacta').val(),
             "proyecto" : $('#id_proyecto').val(),
             "nroacta" : nroacta_captado,
             "serie": get_material_chekeado(),
             "iddespacho": iddespacho
         },
         success : function(data){
             var notificaciones_error_save = [];
             if(data.error){
                 show_notify([data.error])
             }else{
                 if(data.list_error.length == 0){
                     view_acta_existente();
                     deshabilitar_form_acta();
                     $("#name_acta_despacho").html(String(data.stracta));
                     str_acta_mostrar = String(data.stracta);
                     $("#id_load_acta_despacho").removeData("iddacta");
                     $("#id_load_acta_despacho").data("iddacta", data.intacta);
                     actaidd = data.intacta;
                     actastr = data.stracta;
                     show_success_2('Acta creada satisfactoriamente  ' + String(data.stracta));
                 }else{
                     $.each(data.list_error, function(index, msje){
                         notificaciones_error_save.push(msje)
                     });
                     show_notify(notificaciones_error_save)
                 }
             }
         }
      });
  }else{
      show_notify(notificaciones_error);
      notificaciones_error = []
  }
});


$("#id_load_acta_despacho").on('click', function(e){
  e.preventDefault();
  var bit_pdf = validate_pdf_despacho();
  if(bit_pdf){
      var iddacta = $(this).data("iddacta");
      var form = $('#id_form_seguimiento')[0];
      var data = new FormData(form);
      data.append("iddacta", iddacta);
        $.ajax({
            type: "POST",
            enctype: 'multipart/form-data',
            url: URLS_LOAD_ACTA,
            data: data,
            processData: false,
            contentType: false,
            cache: false,
            success: function (dat) {
                if(dat.error){
                     show_notify([dat.error])
                 }else{
                    show_success("Acta cargada correctamente")
                 }
            }
        });
  }else{
      show_notify(notificaciones_error);
      notificaciones_error = []
  }
});


$('#grilla_actual_2 tbody').on('click', 'tr', function () {
    if($(this).hasClass("skyblue")){
        $(this).removeClass("skyblue")
    }else{
        $("tr").removeClass("skyblue");
        $(this).addClass("skyblue")
    }
});


$('#id_nuevo_acta_despacho').on('click', function(e){
    e.preventDefault();
    var actatipo = $(this).data("actatipo");
    $("#id_regresar_listado").show();

    var list_acta_tipo = actatipo.split("/");
    if(parseInt(list_acta_tipo[0]) >= parseInt(list_acta_tipo[1])){
        show_notify(["Actas completas"])
    }else{
        var contador_no_anulados = 0;
        $.each($('#id_modal_list_actas_despacho_2 tr'), function() {
            var estado = $(this).find('td').eq(2).text();
            if(estado != "ANULADO"){
                contador_no_anulados += 1
            }
        });
        var enabled_view;
        if(contador_no_anulados >= 2){
            show_notify(["Actas completas"])
        }else{
            clean_form_all_despacho();
            var iddespacho = $("#id_guardar").data("iddespacho");
            //enabled_view = load_data_material(iddespacho, '');
            ///////////////
            $.ajax({
                url: URLS_GET_INFO_MATERIAL,
                type: 'POST',
                dataType: 'json',
                data: {
                    'iddespacho': iddespacho,
                    'nroacta': ''
                },
                success: function(data){
                    if(data.error){
                        show_notify([data.error])
                    }else{
                        var list_element = data.result;
                        console.log("## ", list_element);
                        console.log("## ", list_element.length);
                        if(list_element.length > 0){
                            $("#tbody_info_material").empty();
                            $.each(list_element, function (index, value){
                                var chekor = '';
                                if(value[0]){
                                    chekor = 'checked'
                                }
                                var deshabilitado = '';
                                var html_tbody = '<tr data-iddtipomaterial="'+ value[1] +'" data-namematerial="'+ value[2] +'">' +
                                    '<td><center><input type="checkbox" class="material_elegido" ' + chekor + ' ' + deshabilitado + '/></center></td>' +
                                    '<td><center>' + value[2] + '</center></td></tr>';
                                $("#tbody_info_material").append(html_tbody)
                            });
                            nroacta_captado = '';
                            $("#id_fechaacta").val(currentDate);
                            $(".modal_bg_info").trigger("click");
                            $("#id_new_acta").addClass("pop-up-active");
                        }else{
                            show_notify(["Actas completas"])
                        }
                    }
                }
            });
            ///////////////
        }
    }
});


$('#id_editar_acta_despacho').on('click', function(e){
    e.preventDefault();
    if($(".skyblue").length < 1){
        show_notify(["De click sobre el acta a modificar"])
    }else{
        if($(".skyblue").length == 1){
            var stracta = $(".skyblue").find('td').eq(0).text();
            var estado = $(".skyblue").find('td').eq(2).text();
            if(estado != "ANULADO"){
                show_loader();
                var actacliente = $("#id_nuevo_acta_despacho").data("actacliente");
                if(actacliente){
                    $("#id_anular_acta").hide();
                    $("#id_anular").attr("disabled", "disabled");
                }else{
                    $("#id_anular_acta").show();
                    $("#id_anular").removeAttr("disabled");
                }
                tr_editar = $(".skyblue");
                $("#id_regresar_listado").show();
                var nroacta = $(".skyblue").data("iddacta");
                var fechacta = $(".skyblue").data("fechacta");
                var iddespacho = $("#id_guardar").data("iddespacho");
                $(".modal_bg_info").trigger("click");
                view_acta_existente();
                $("#name_acta_despacho").html(String(stracta));
                $("#id_load_acta_despacho").removeData("iddacta");
                $("#id_load_acta_despacho").data("iddacta", nroacta);
                $("#id_fechaacta").val(String(fechacta));

                $.ajax({
                     url: URL_GET_DATA_ACTA_EXISTENTE,
                     type: 'get',
                     data: {
                         "iddacta" : nroacta
                     },
                     success : function(data){
                         if(data.error){
                             show_notify([data.error])
                         }else{
                             $("#id_proyecto").select2("destroy");
                             $("#id_proyecto").val(data.result["intIdProye"]);
                             $("#id_proyecto").select2();
                             $("#id_contratista").val(data.result["strNoContra"]);
                             $("#id_estacion").val(data.result["strNoEstacion"]);
                             $("#id_direccion").val(data.result["strDeDirec"]);
                             $("#id_entrego").val(data.result["strNoEntrega"]);
                             $("#id_recepciono").val(data.result["strDeRecep"]);
                             $("#id_observaciones").val(data.result["strDeObser"]);
                             var enabled_view = load_data_material(iddespacho, nroacta);
                             console.log("@@", enabled_view);
                             deshabilitar_form_acta();
                             $("#nombre_acta_existente").html(" :  " + String(data.result["strDeRutaImagenTMI"]).split("/")[1]);
                             actaidd = nroacta;
                             $("#id_new_acta").addClass("pop-up-active");

                         }
                         hide_loader()
                     }
                });
            }else{
                show_notify(["Elija un acta no anulada"])
            }
        }else{
            show_notify(["Solo seleccione una fila para editar"])
        }
    }
});


$("#id_anular").on('click', function(e){
  e.preventDefault();
  show_danger_2("¿Esta seguro de anular?", "");
});

$("#id_null_acta").on('click', function(e){
    e.preventDefault();
    var iddespacho = $("#id_guardar").data("iddespacho");
    $.ajax({
         url: URL_ANULAR_ACTA,
         type: 'get',
         data: {
             "iddespacho": iddespacho,
             "nroacta" : actaidd,
             'proyecto':$('#id_proyecto>option:selected').val()
         },
         success : function(data){
             if(data.error){
                 show_notify([data.error])
             }else{
                 $("#close_msje_null").trigger("click");
                 $("#cerrar-pop-up").trigger("click");
                 $('#cargar_despacho').trigger("click");
                 $("#modal_list_actas").modal({backdrop: 'static', keyboard: true});
                 tr_editar.find('td').eq(2).html("ANULADO")
             }
         }
    });
});


$('#grilla_actual_2>tbody').on('click', '.lance_popup_tmi', function(e){
  e.preventDefault();
  var rutatmi = $(this).data("rutatmi");
  if(rutatmi){
      $.ajax({
         url: GET_URL_PDF,
         type: 'get',
         data: {"stracta" : rutatmi},
         success : function(data){
             if(data.error){
                 show_notify([data.error])
             }else{
                 var pdf_link;
                 if(data.url){
                     pdf_link = data.url;
                 }else{
                     pdf_link = PDF_NULL;
                 }
                 const iframe = '<iframe src="' + pdf_link + '" width="100%" height="500"></iframe>';
                 $.EditcreateModal({
                    title: 'ACTA: ' + String(rutatmi).split("/")[1],
                    message: iframe,
                    closeButton: true,
                    scrollable: false
                });
             }
         }
      });
  }else{
      show_notify(["Acta no cuenta con imagen TMI"])
  }
});


$("#regreso_listado").on('click', function(e){
  e.preventDefault();
  $(".pop-up-close").trigger("click");
  $("#modal_list_actas").modal({backdrop: 'static', keyboard: true});
});

$("#tabla_main tbody").on('click', '.nothing_acta', function(e){
    e.preventDefault();
    show_notify(["Acta de Inspeccion Firmada Faltante"])
});

