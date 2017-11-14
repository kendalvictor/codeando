jQuery(document).ready(function($) {
    $('select').select2();
     $('.date-picker').datepicker({});

   var tabla_packing = $("#datatable_packing").DataTable({
            responsive: true,
            dom: 'Bfrtip',
            "language":lengauge_table,
            "scrollY": 400,
            'scrollCollapse': true,
            "paginate": false,
            "bInfo": false,
          });


    var tabla_asignar = $("#tabla-asignar").DataTable({
            responsive: true,
            dom: 'Bfrtip',
            "language":lengauge_table,
            "paging": false,
            "bInfo": false,

        });


var tabla_eliminar = $("#tabla-eliminar").DataTable({
            responsive: true,
            dom: 'Bfrtip',
            "language":lengauge_table,
            "paging": false,
            "bInfo": false,


        });

   search_header_table([tabla_packing, tabla_asignar, tabla_eliminar])

     // $("#pop-asignar-guia").addClass('pop-up-active');

    $(".cancelar_elementos").click(function(event) {
        /* Act on the event */
        event.preventDefault()
        $("#tabla-asignar_wrapper input").val("").trigger("keyup")
        $("#pop-asignar-guia").removeClass('pop-up-active')
      });

    $("tbody").on('click', '.show-asignar', (function(event) {
            /* Act on the event */
            event.preventDefault();
            $('#numero_guia_interna').val('')
            numero_packing_list = $(this).data('packing');
            id_packing_list = $(this).data('packingid');
            tabla_asignar.clear().draw()
            show_loader()
            $.ajax({
                url: url_get_packing_list_detail,
                type: 'GET',
                dataType: 'json',
                data: { 'id_packing_list':id_packing_list},
                success: function(data){
                   if (data.status == 200) {
                        total_peso = 0
                        total_elementos = 0
                        console.log('data', data)
                         var results = data.results.map(function(val, index) {
                                result = []
                                result.push(val['strCoEleme'])
                                result.push(val['strNoEleme'])
                                result.push(val['strDePaque'])
                                result.push(val['numNuLongi'])
                                result.push(val['numNuPesosNetos'])
                                result.push(val['numNuAreas'])
                                result.push(val['strDePerfi'])
                                result.push(val['Cantidad'])

                                total_peso += parseFloat(val['Cantidad']) * parseFloat(val['numNuPesosNetos'])
                                total_elementos += parseFloat(val['Cantidad'])
                                return result

                        })
                         tabla_asignar.rows.add(results).draw()
                         $('#id_packing_list').val(id_packing_list);
                         $('#id_numero_packing_list').val(numero_packing_list);
                         $('#pop-asignar-guia .total-elementos').text(parseFloat(total_elementos).toFixed(2))
                         $('#pop-asignar-guia .total-peso').text(parseFloat(total_peso).toFixed(2))

                         $("#pop-asignar-guia").toggleClass('pop-up-active')
                    }else{
                        show_notify(["No se puede mostrar la data."]);
                    }
                }
            })
            let id_etapa = $(this).data('etapa');
            let id_proyecto = $('#id_intIdProye').val();
            let id_tipo_elemento = $("#id_tipo_elemento").val();
            $.ajax({
                url: url_get_contratistas,
                type: 'GET',
                dataType: 'json',
                data: { 'id_etapa':id_etapa, 'id_proyecto': id_proyecto, 'id_tipo_elemento': id_tipo_elemento},
                success: function(data){
                        console.log(' data', data)
                    if (data.status == 200){
                        console.log(' todo ok', data)
                        $("#id_contratista").find('option').remove()
                        $("#id_contratista").append($('<option>', {value: -1, text: '--------------'}));
                        $.each(data.result, function(index, val) {
                              $("#id_contratista").append($('<option>', {value: val['intIdContr'], text: val['strNoEmpre']}));
                               /* iterate through array or object */
                          });
                    }else{
                        show_notify(["No se pudo mostrar los contratistas"])
                    }
                }
            });
                hide_loader()
        }));



    $(".cancelar_eliminar").click(function(event) {
            /* Act on the event */
            event.preventDefault()
            $("#pop-eliminar-elementos").removeClass('pop-up-active')
          });

    $("tbody").on('click', '.show-eliminar', (function(event) {
            /* Act on the event */
            event.preventDefault();
            tabla_eliminar.clear().draw()
            numero_packing_list = $(this).data('packing');
            id_packing_list = $(this).data('packingid');
            show_loader()
            $.ajax({
                url: url_get_packing_list_detail,
                type: 'GET',
                dataType: 'json',
                data: { 'id_packing_list':id_packing_list},
                success: function(data){
                    hide_loader()
                   if (data.status == 200) {
                        total_peso = 0
                        total_elementos = 0
                         var results = data.results.map(function(val, index) {
                                result = []
                                result.push('<input type="checkbox" class="check-eliminar" data-elemento ="'+ val['strCoEleme'] + '">')
                                result.push(val['strCoEleme'])
                                result.push(val['strNoEleme'])
                                result.push(val['strDePaque'])
                                result.push(val['numNuLongi'])
                                result.push(val['numNuPesosNetos'])
                                result.push(val['numNuAreas'])
                                result.push(val['strDePerfi'])
                                result.push(val['Cantidad'])
                                result.push('<input type="number" disabled="disabled" class="cantidad-eliminar">')
                                total_peso += parseFloat(val['Cantidad']) * parseFloat(val['numNuPesosNetos'])
                                total_elementos += parseFloat(val['Cantidad'])
                                return result

                        })
                         tabla_eliminar.rows.add(results).draw()
                         $('#id_numero_packing_list_eliminar').val(numero_packing_list);
                         $('#id_packing_list_eliminar').val(id_packing_list);
                         $('#pop-eliminar-elementos .total-elementos').text(parseFloat(total_elementos).toFixed(2))
                         $('#pop-eliminar-elementos .total-peso').text(parseFloat(total_peso).toFixed(2))
                        $("#pop-eliminar-elementos").toggleClass('pop-up-active')
                    }else{
                        show_notify(["No se puede mostrar la data."]);
                    }
                }
            })

        }));


    $('.grabar_guia_interna').on('click', function(e){
        e.preventDefault();
         numero_guia_interna = $('#numero_guia_interna').val();
         id_packing_list = $('#id_packing_list').val();
         id_contratista = $('#id_contratista').val();
         var data_validar = [
            {
                id: "#numero_guia_interna",
                tipo: "select"
            },
            {
                id: "#id_contratista",
                tipo: "select"
            },
        ]
        console.log(validate_data(data_validar))
        if (validate_data(data_validar)) {
            show_loader()
                     $.ajax({
                         url: url_grabar_guia_interna,
                         type: 'POST',
                         dataType: 'json',
                         data: {'numero_guia_interna': numero_guia_interna, 'id_packing_list': id_packing_list, 'id_contratista': id_contratista},
                         success: function(data){
                                    hide_loader()
                                    if (data.status == '200'){
                                            $("#numero_guia_interna").val("")
                                            show_success("Se grabó correctamente.");
                                    }else{
                                        show_notify([data.error]);
                                    }

                                }
                     })
         }
    });

   $('tbody').on('click', '.check-eliminar', function(e){

            $row = $(this).closest('tr')
            let cantidad
            let input_cantidad
            input_cantidad = $row .find('.cantidad-eliminar')
            if (input_cantidad.is(':disabled')){
                input_cantidad.prop("disabled", false);
                input_cantidad.removeClass('error-data');
                cantidad = $row.find(':nth-last-child(2)').text()
                input_cantidad.val(cantidad)

            }else{
                input_cantidad.prop("disabled", "disabled");
                input_cantidad.val('')
                input_cantidad.removeClass('error-data');
            }
   });


   $('tbody').on('change', '.cantidad-eliminar', function(e){
        cantidad_eliminar = $(this).val();
        tr = $(this).closest('tr')
        cantidad =tr.find(':nth-last-child(2)').text();
        if ((parseInt(cantidad_eliminar)) > parseInt(cantidad)){
            $(this).addClass('error-data');
        }else{
            $(this).removeClass('error-data');
        }

   });


   function is_valid_cantidades_eliminar(){
    // VALIDARA QUE NINGUN INPUT TENGA LA CLASE ERROR-DATA Y ADEMAS QUE AL MENOS UNO TENGA VALOR, RETORNARA UN BOOLEANO
    inputs_cantidades_eliminar = $('.cantidad-eliminar');
    flag_algun_valor = false
    inputs_cantidades_eliminar.each(function(index, el) {
        if ($(this).hasClass('error-data')){
            show_notify(['Las cantidades a eliminar no pueden superar a las existentes']);
            return false
        }
        if ($(this).val() != '' ){
            flag_algun_valor =  true
        }
    });
    if (flag_algun_valor == false){
            show_notify(['Ingrese alguna cantidad a eliminar'])
            return false
    }

    return true
   }


   var data_packing = {
        ot: '',
        tipo_elemento: '',
        tarea: '',
        zona: '',
        planta:'',
        etapa:'',
        elementos: {

        },
        update_filtro: function(data){
            this.ot = data.id_proyecto;
            this.tipo_elemento = data.id_tipo_elemento;
            this.tarea = data.id_tarea;
            this.planta = data.id_planta;
            this.zona = data.id_zona;
            this.etapa = data.id_etapa
        },
        add: function(codigo, cantidad){
            var self = this;
            if(parseInt(cantidad)){
                self.elementos[codigo] = cantidad
            }else{
                delete self.elementos[codigo]
           }
        },
        remove: function(codigo){
            var self = this;
            delete self.elementos[codigo]
        },
        add_remove: function(codigo, cantidad){
            var self = this;

            if(parseInt(cantidad)){
                self.elementos[''+codigo+''] = cantidad
            }else{
                delete self.elementos[''+codigo+'']
           }
        },
        clean_data: function(){
            this.elementos = {}
            $("#example-select-all").prop('checked', false)
        },
        get_data: function(){
            var self = this;
            var data_json = {
                ot: self.ot,
                tipo_elemento:  self.tipo_elemento,
                tarea: self.tarea,
                zona: self.zona,
                planta: self.planta,
                etapa: self.etapa,
                elementos: self.elementos
            }
            return JSON.stringify(data_json)
        }
   }

    $("#id_intIdProye").change(function(event) {
        /* Act on the event */
        var id_proyecto = $(this).val()


        if (id_proyecto) {
                show_loader()
                $.ajax({
                    url: url_get_tarea_x_ot,
                    type: 'GET',
                    dataType: 'json',
                    data: {id_proyecto: id_proyecto},
                    success: function(data){

                        if (data.status == 200) {
                             $("#id_intIdTarea").find('option').remove()
                            $("#id_intIdTarea").append($('<option>', {value: -1, text: 'TODOS'}));
                            $.each(data.list_tarea, function(index, val) {
                                $("#id_intIdTarea").append($('<option>', {value: val['intIdTarea'], text: val['strDeTarea']}));
                                 /* iterate through array or object */
                            });
                        }
                        hide_loader()
                    }
                })
        }else{
            $("#id_intIdTarea option").remove()
            $("#id_intIdTarea").append($('<option>', {value: -1, text: 'TODOS'}));
        }
        $.ajax({
            url: url_get_etapa,
            type: 'GET',
            dataType: 'json',
            data: {id_proyecto: id_proyecto},
            success: function(data){
                show_loader()
                if (data.status == 200) {
                    $("#id_etapa").find('option').remove()
                    $("#id_etapa").append($('<option>', {value: -1, text: 'TODOS'}));
                    $.each(data.result, function(index, val) {
                        $("#id_etapa").append($('<option>', {value: val['intIdEtapa'], text: val['strDeEtapa']}));
                         /* iterate through array or object */
                    });
                }
                hide_loader()
            }
        })
        // hide_loader()

    });
    $("body").on('change', "#id_intIdTarea , #id_intIdProye", function(event) {
        event.preventDefault();
        /* Act on the event */
        var id_proyecto = $("#id_intIdProye").val()
        var id_tarea = $("#id_intIdTarea").val()
        /* Act on the event */
        show_loader()
            $.ajax({
                url: url_get_zonas,
                type: 'GET',
                dataType: 'json',
                data: {id_proyecto: id_proyecto, id_tarea:id_tarea},
                success: function(data){

                    if (data.status == 200) {
                            $("#id_zona").find('option').remove()
                            $("#id_zona").append($('<option>', {value: -1, text: 'TODOS'}));
                            $.each(data.list_zonas, function(index, val) {
                                $("#id_zona").append($('<option>', {value: val['strDeZonas'], text: val['strDeZonas']}));
                                 /* iterate through array or object */
                            });
                    }
                    hide_loader()
                }
            })
    });

    $(".cargar_packing").click(function(event) {
        /* Act on the event */
        event.preventDefault();
        var data_enviar = {
            id_fecha_inicio: $('#id_fecha_inicio').val(),
            id_fecha_final: $('#id_fecha_final').val(),
            id_proyecto: $("#id_intIdProye").val(),
            id_tipo_elemento: $("#id_tipo_elemento").val(),
            id_tarea: $("#id_intIdTarea").val(),
            id_planta: $("#id_planta").val(),
            id_zona: $("#id_zona").val(),
            id_etapa: $("#id_etapa").val(),
            id_tipo_guia: $('#id_tipo_packing').val(),

        }
        var data_validar = [
            {
                id: "#id_intIdProye",
                tipo: "select2"
            },
             {
                id: "#id_intIdTarea",
                tipo: "select2"
            },
            {
                id: "#id_fecha_inicio",
                tipo: "select"
            },
            {
                id: "#id_fecha_final",
                tipo: "select"
            },

        ]
        if (validate_data(data_validar)) {
            show_loader()
            data_packing.update_filtro(data_enviar)
            tabla_packing.clear().draw()
            $.ajax({
                url: url_packing_list_by_date,
                type: 'GET',
                dataType: 'json',
                data: data_enviar,
                success: function(data){
                    console.log('data**********', data)
                    var input = ""
                    if (data.status == 200) {
                        total_elementos = 0
                        total_peso = 0
                         var results = data.results.map(function(val, index) {
                                // console.log('data', data)
                                result = []
                                if (val['strNuGuiaInter']) {
                                    input = '<div class="button-group m-t-b-5"> <a class="btn btn--primary generate_reporte" data-packingid="' + val['intIdPacking'] + '"><i class="fa fa-file-excel-o"> </i></a></div>'

                                }else{
                                    input = '<div class="button-group m-t-b-5"><a class="btn btn--info show-asignar " data-etapa ="'+val['intIdEtapa'] +'" data-packing="' + val['strNuPacking'] +'"data-packingid="'+val['intIdPacking']+'"><i class="fa fa-caret-square-o-left"></i></a><a class="btn btn--danger show-eliminar" data-packing="' + val['strNuPacking'] +'"data-packingid="'+val['intIdPacking']+'"><i class="fa fa-minus-square"></i></a> <a class="btn btn--primary generate_reporte" data-packingid="' + val['intIdPacking'] + '"><i class="fa fa-file-excel-o"> </i></a></div>'

                                }


                                result.push(input)
                                result.push(val['dttFeUsuarCreac'])
                                result.push(val['strNuPacking'])
                                result.push(val['strNuGuiaInter'])

                                result.push(val['strOT'])
                                result.push(val['strDePrior'])
                                result.push(val['strDeTarea'])
                                result.push(val['strDePlanta'])
                                result.push(val['Total'])
                                result.push(val['PesoTotal'])
                                result.push(val['strDeZonas'])
                                result.push(val['strDeEtapa'])
                                result.push(val['strNoUsuar'])
                                result.push(val['UsuarGuia'])
                                result.push(val['dttFeGuia'])
                                result.push(val['UsuarModif'])
                                result.push(val['dttFeModif'])

                                total_peso += parseFloat(val['PesoTotal'])

                                total_elementos += parseFloat(val['Total'])


                                return result

                        })
                         tabla_packing.rows.add(results).draw()
                         $('#id_total_elementos').text(parseFloat(total_elementos))
                         $('#id_total_peso').text(parseFloat(total_peso).toFixed(2))
                         hide_loader()
                    }

                }
            })

        }else{
            if($("#id_intIdProye").val() == -1){
              show_notify(['Seleccione OT'])
          }else{
              if($("#id_intIdTarea").val() == -1){
                  show_notify(['Seleccione Tarea'])
              }
          }
        }
    });

    // function calcular_peso_total(){
    //     console.log('calcular peso total');

    // }


    $(".continuar-success").click(function(event) {
        /* Act on the event */
        event.preventDefault();
        $('.pop-up').removeClass('pop-up-active');
        hide_message()
        $("#tabla-asignar_wrapper input").val("").trigger("keyup")
        $('.cargar_packing').trigger('click');
        // window.location = url_guia_interna_list+'?id_proyecto='+$("#id_intIdProye").val()+'&id_tipo_elemento='+$('#id_tipo_elemento')
        //             + '&id_etapa=' + $('#id_etapa').val() + '&id_zona='+ $('#id_zona').val() +'&id_tarea='+ $('#id_intIdTarea').val()+
        //             '&id_planta='+ $('#id_planta').val()+ '&id_tipo_guia='+ $('#id_tipo_packing').val()+
        //             '&id_fecha_inicio=' + $('#id_fecha_inicio').val() +  '&id_fecha_final=' + $('#id_fecha_final').val()

  });

    $("tbody").on('click', '.generate_reporte', function(){
        id_packing = $(this).data('packingid')
        window.open (url_reporte_packing_list+'?id_packing='+parseInt(id_packing), "_blank")
    });



$('#datatable_packing_wrapper tfoot input').on('keyup', function () {
            console.log('change')
              var cant_total = 0;
              var peso_total = 0;
              var obj = $('#datatable_packing_wrapper tbody tr').map(function() {
                  var $row = $(this);
                  console.log('row',   $row)
                  var cantidad = $row.find(':nth-child(9)').text()
                  console.log('cantidad', cantidad)
                  var peso = $row.find(':nth-child(10)').text()
                  console.log('peso', peso)
                  if(cantidad) {
                      cant_total += parseFloat(cantidad);
                      if (peso) {
                            peso_total += parseFloat(peso)
                      }
                  }

              });
              $("#id_total_elementos").text(cant_total.toFixed(2));
              $("#id_total_peso").text(peso_total.toFixed(2));
          });

$('#tabla-asignar tfoot input').on('keyup', function () {
            console.log('change')
              var cant_total = 0;
              var peso_total = 0;
              var obj = $('#tabla-asignar tbody tr').map(function() {
                  var $row = $(this);
                  console.log('row',   $row)
                  var cantidad = $row.find(':nth-last-child(1)').text()
                  console.log('cantidad', cantidad)
                  var peso = $row.find(':nth-child(5)').text()
                  console.log('peso', peso)
                  if(cantidad) {
                      cant_total += parseFloat(cantidad);
                      if (peso) {
                            peso_total += parseFloat(cantidad*peso)
                      }
                  }

              });
              console.log('cantidad total', cant_total)
              console.log('total peso', peso_total)
              $("#asignar-total-elem").text(cant_total.toFixed(2));
              $("#asignar-total-peso").text(peso_total.toFixed(2));
          });



$('#tabla-eliminar tfoot input').on('keyup', function () {
            console.log('change')
              var cant_total = 0;
              var peso_total = 0;
              var obj = $('#tabla-eliminar tbody tr').map(function() {
                  var $row = $(this);
                  console.log('row',   $row)
                  var cantidad = $row.find(':nth-last-child(2)').text()
                  console.log('cantidad', cantidad)
                  var peso = $row.find(':nth-child(6)').text()
                  console.log('peso', peso)
                  if(cantidad) {
                      cant_total += parseFloat(cantidad);
                      if (peso) {

                            peso_total += parseFloat(cantidad*peso)
                      }
                  }

              });
              console.log('***total peso', peso_total)
              $("#eliminar-total-elem").text(cant_total.toFixed(2));
              $("#eliminar-total-peso").text(peso_total.toFixed(2));
          });


    $('#example-select-all').on('change', function(){
        console.log('clickeando ando')
          var rows = tabla_eliminar.rows({ 'search': 'applied' }).nodes();
          console.log('rowss', rows)
          var check = $('input[type="checkbox"].check-eliminar', rows).prop('checked', this.checked);
          let cantidad
          let input_cantidad
          console.log('check', check)
          if ($(this).prop('checked')) {
                check.map(function(index, elem) {
                    $row = $(this).closest('tr')
                     input_cantidad = $row.find('.cantidad-eliminar')
                    input_cantidad.prop("disabled", false);
                    input_cantidad.removeClass('error-data');
                    cantidad = $row.find(':nth-last-child(2)').text()
                    input_cantidad.val(cantidad)


                  })
            }else{
                check.map(function(index, elem) {
                    input_cantidad = $(this).closest('tr').find('.cantidad-eliminar')
                    input_cantidad.prop("disabled", "disabled");
                    input_cantidad.val('')
                    input_cantidad.removeClass('error-data');
                  })
            }
   });

$('.boton_anular').on('click', function(e){
    console.log('click anular');
    e.preventDefault();
    show_warning("¿Desea anular este packing?", "")
})

$('.continuar-warning').click(function(e){
    console.log('continuar warnign')
    let id_packing_list = $('#id_packing_list_eliminar').val()
    show_loader()
    $.ajax({
                url: url_anular_packing_list,
                type: 'GET',
                dataType: 'json',
                data: {'id_packing_list': id_packing_list},
                success: function(data){
                    hide_loader()
                        if (data.status == 200){
                            show_success('Se anuló correctamente');
                        }
                        else{
                            show_notify(['No se pudo eliminar', data.errors]);
                        }
                hide_loader()
                }
            })
});



function show_warning_2(titulo, texto){
            $(".message-pop--warning-2").addClass('message-pop-active')
            if (titulo) {
                $(".message-pop--warning-2 .message-pop-text h3").text(titulo)

            };
            if (texto) {
                $(".message-pop--warning-2 .message-pop-text .text").text(texto)

            };
            setTimeout(function(){
                $(".message-pop--warning-2 .message-pop-content").addClass('message-pop-content-active');
            }, 200);

        }

$('.boton_eliminar').click(function(e){
    e.preventDefault();
    console.log('eliminar')
     if (is_valid_cantidades_eliminar() == true) {
    show_warning_2("¿Desea eliminar este elemento?")
    }
});

$('.continuar-warning-2').click(function(event) {
    /* Act on the event */
    event.preventDefault();
    console.log('continuar warning 2')

                id_packing_list = $('#id_packing_list_eliminar').val()
                trs = $('#tabla-eliminar tbody tr')
                array_data = new Array()
                trs.each(function(index, el) {
                    // console.log('cod' ,$(this).find('td').eq(8));
                    codigo = $(this).find('td').eq(1).text()
                    cantidad = $(this).find('td').eq(9).find('.cantidad-eliminar').val()
                    if (!isNaN(cantidad)){
                        array_data.push([codigo, cantidad])
                    }
                });
                console.log('id_packing_list', id_packing_list)
                 show_loader()
                $.ajax({
                    url: url_eliminar_packing_list_detail,
                    type: 'POST',
                    dataType: 'JSON',
                    data: {'id_packing_list': id_packing_list, 'array_data': JSON.stringify(array_data)},
                    success: function(data){
                        hide_loader()
                        if (data.status == 200){
                            show_success('Se eliminó correctamente');
                        }
                        else{
                            show_notify(['No se pudo eliminar']);
                        }
                    }
                })




});

// $('.boton_eliminar').on('click', function(e){
//         e.preventDefault();
//         if (is_valid_cantidades_eliminar() == true) {
//                 id_packing_list = $('#id_packing_list_eliminar').val()
//                 trs = $('#tabla-eliminar tbody tr')
//                 array_data = new Array()
//                 trs.each(function(index, el) {
//                     // console.log('cod' ,$(this).find('td').eq(8));
//                     codigo = $(this).find('td').eq(1).text()
//                     cantidad = $(this).find('td').eq(9).find('.cantidad-eliminar').val()
//                     if (!isNaN(cantidad)){
//                         array_data.push([codigo, cantidad])
//                     }
//                 });
//                 console.log('id_packing_list', id_packing_list)
//                  show_loader()
//                 $.ajax({
//                     url: url_eliminar_packing_list_detail,
//                     type: 'POST',
//                     dataType: 'JSON',
//                     data: {'id_packing_list': id_packing_list, 'array_data': JSON.stringify(array_data)},
//                     success: function(data){
//                         hide_loader()
//                         if (data.status == 200){
//                             show_success('Se eliminó correctamente');
//                         }
//                         else{
//                             show_notify(['No se pudo eliminar']);
//                         }
//                     }
//                 })


//         }
//    });






// $('#datatable_armador tbody ').on('click', '.liberar_elementos', function(event) {
//         /* Act on the event */
//         event.preventDefault();
//         a_object = $(this)
//         show_warning("¿Esta seguro de liberar estos elementos?", "")

//     });
// $(".continuar-warning").click(function(event) {
//         /* Act on the event */

//         data = {
//                   'codigo_elemento' : a_object.data('codigoelemento'),
//                    'id_proyecto': a_object.data('idproyecto'),
//                    'id_prioridad': a_object.data('idprioridad'),
//                    'id_tarea': a_object.data('idtarea'),
//                    'id_paquete': a_object.data('idpaquete'),
//                    'id_planta': a_object.data('idplanta'),
//                    'id_etapa_ante': a_object.data('idetapainspe'),
//                    'id_empresa':a_object.data('idempresa'),
//                    'id_supervisor': a_object.data('idsupervisor'),
//                    'etapa_inspe': 'L',
//                    'obs': '',
//                    'id_etapa':a_object.data('idetapa')
//           }
//         json_data = JSON.stringify(data)
//         show_loader();
//       $.ajax({
//           url: '{% url "inspeccionar:ajax_detener_liberar_elementos" %}',
//           type: 'GET',
//           dataType: 'json',
//           cache:false,
//           data: {'data_elementos': json_data},
//           success: function(data){

//             if (data.status == 200) {
//                   console.log('STATUS')
//                    tabla_inspeccion.row(a_object.parents('tr')).remove().draw();
//                    show_success("Se Guardo Correctamente", "")

//             }else{
//                show_notify(['Ocurrio un problema', data.error])
//             }
//           hide_loader();
//           }
//         })

//       });

});

