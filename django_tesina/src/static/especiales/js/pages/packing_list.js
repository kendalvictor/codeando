
    $('select').select2();
    var todos_los_combos = $("#id_intIdProye, #id_intIdTarea, #id_tipo_elemento, #id_zona, #id_planta, #id_etapa, #id_situacion");
   var tabla_packing = $("#datatable_packing").DataTable({
            responsive: true,
            dom: 'Bfrtip',
            "language":lengauge_table,
            "scrollY": 420,
            'scrollCollapse': true,
            "paginate": false,


          });

   search_header_table([tabla_packing])

   var data_packing = {
        ot: '',
        tipo_elemento: '',
        tarea: '',
        zona: '',
        planta:'',
        etapa:'',
        situacion:'',
        elementos: {

        },
        update_filtro: function(data){
            this.ot = data.id_proyecto;
            this.tipo_elemento = data.id_tipo_elemento;
            this.tarea = data.id_tarea;
            this.planta = data.id_planta;
            this.zona = data.id_zona;
            this.etapa = data.id_etapa,
            this.situacion = data.id_situacion
        },
        add: function(codigo, cantidad){
            var self = this;
            if(parseInt(cantidad)){
                self.elementos[codigo] = cantidad
            }else{
              console.log(codigo)
                delete self.elementos[codigo]
           }
           console.log(self.elementos)
        },
        remove: function(codigo){
            var self = this;
            delete self.elementos[codigo]
             console.log(self.elementos)
        },
        add_remove: function(codigo, cantidad){
            var self = this;
            console.log(codigo)
            console.log(cantidad)

            if(parseInt(cantidad)){
                self.elementos[''+codigo+''] = cantidad
            }else{
              console.log(''+codigo+'')
                delete self.elementos[''+codigo+'']
           }
           console.log(self.elementos)
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
                elementos: self.elementos,
                situacion: self.situacion
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
                            $("#id_intIdTarea").append($('<option>', {value: -1, text: 'Seleccione'}));
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
            $("#id_intIdTarea").append($('<option>', {value: -1, text: 'Seleccione'}));
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
                    $("#id_etapa").append($('<option>', {value: -1, text: 'Seleccione'}));
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
                            $("#id_zona").append($('<option>', {value: -1, text: 'Seleccione'}));
                            $.each(data.list_zonas, function(index, val) {
                                $("#id_zona").append($('<option>', {value: val['strDeZonas'], text: val['strDeZonas']}));
                                 /* iterate through array or object */
                            });
                    }
                    hide_loader()
                }
            })
    });

    todos_los_combos.change(function(){
        data_packing.clean_data();
        tabla_packing.clear().draw()
    });

    $(".cargar_packing").click(function(event) {
        /* Act on the event */
        event.preventDefault();
        console.log('CARGAR PACKING')
        var data_enviar = {
            id_proyecto: $("#id_intIdProye").val(),
            id_tipo_elemento: $("#id_tipo_elemento").val(),
            id_tarea: $("#id_intIdTarea").val(),
            id_planta: $("#id_planta").val(),
            id_zona: $("#id_zona").val(),
            id_etapa: $("#id_etapa").val(),
            id_situacion: $("#id_situacion").val()
        }
        console.log("proyecto", $("#id_intIdProye").val());
        var data_validar = [
            {
                id: "#id_intIdProye",
                tipo: "select"
            },
            {
                id: "#id_tipo_elemento",
                tipo: "select"
            },
            {
                id: "#id_intIdTarea",
                tipo: "select"
            },
            {
                id: "#id_zona",
                tipo: "select"
            },
            {
                id: "#id_etapa",
                tipo: "select"
            },
            {
                id: "#id_planta",
                tipo: "select"
            },
        ]
        if (validate_data(data_validar)) {
            show_loader()
            data_packing.update_filtro(data_enviar)
            tabla_packing.clear().draw()
            $.ajax({
                url: url_packing_list,
                type: 'GET',
                dataType: 'json',
                data: data_enviar,
                success: function(data){
                    var input = ""
                    if (data.status == 200) {
                        total_elementos = 0
                        total_peso = 0
                         var results = data.results.map(function(val, index) {
                                result = []
                                input = '<input name="input_check" class="elegir_check" type="checkbox" data-id-paquete="'+val['intIdPaque']+'"  data-incompleto="' +val['Incompleto'] + '" >'
                                result.push(input)
                                result.push(val['strCoEleme'])
                                result.push(val['intnurevis'])
                                result.push(val['Cantidad'])
                                result.push('<input type="number" disabled="disabled" value="'+val['Cantidad']+'" class="max_num add-item-filtro" data-codigo="'+val["intIdPaque"]+'|'+val['strCoEleme']+'" data-max="'+val['Cantidad']+'" />')
                                result.push(val['Prioridad'])
                                result.push(val['Tarea'])
                                result.push(val['Paquete'])
                                result.push(val['strNoEleme'])
                                result.push(val['strDePerfi'])
                                result.push(val['numNuLongi'])
                                result.push(val['numNuPesosNetos'])
                                result.push(val['numNuAreas'])
                                result.push(val['EtapaSiguiente'])
                                result.push(val['EtapaAnterior'])

                                total_peso += parseFloat(val['Cantidad']) * parseFloat(val['numNuPesosNetos'])
                                total_elementos += parseFloat(val['Cantidad'])
                                return result

                        })
                         tabla_packing.rows.add(results).draw()
                         colorear_incompletos()
                         console.log('total elementos', total_elementos)
                         console.log('total peso', total_peso)
                         $('#id_total_elementos').text(parseFloat(total_elementos).toFixed(2))
                         $('#id_total_peso').text(parseFloat(total_peso).toFixed(2))
                         hide_loader()
                    }
                    console.log("testa")
                    console.log(data)
                }
            })

        }
    });
    function colorear_incompletos(){
        console.log('colorear incomplos')
        var rows = tabla_packing.rows({ 'search': 'applied' }).nodes();
        console.log('rows', rows)
        var check = $('input[type="checkbox"].elegir_check', rows)
        console.log('checks', check)
        check.map(function(index, elem) {
            if ($(this).data('incompleto') == 'R'){
                console.log('IF')
                $(this).closest('tr').css('background', '#d9534f');
            }
          })
    }

    $("body").on('click', '.editar_cantidad', function(event) {
        event.preventDefault();
        var tr = $(this).closest('tr')
        var td = $(this).closest('td')
        var codigo = $(this).closest('td').find('span').data('codigo')
        var cantidad_max = tr.find('td').eq(6).text()
        var input = '<input type="number"  class="max_num add-item-filtro" data-codigo="'+codigo+'" data-max="'+cantidad_max+'" />';
        /* Act on the event */
        td.find('span').remove();
        td.html(input);
    });

    $("body").on('keyup change click', '.add-item-filtro', function (e) {
        var codigo = $(this).data("codigo")
        data_packing.add_remove(codigo, $(this).val())
    });

    $(".generar_packing").on("click", function(e) {
        /* Act on the event */
        e.preventDefault();

        if (Object.values(data_packing.elementos).length > 0) {
            show_loader()
            $.ajax({
                url: url_post_packing_list,
                type: 'POST',
                contentType: 'application/json; charset=utf-8',
                data: data_packing.get_data(),
                dataType: 'json',
                success: function(data){
                    if (data.status==200) {
                        data_packing.codigo_correlativo = data.codigo_correlativo;

                        data_packing.id_packing = data.id_packing;
                        show_success("Se generó el packing list con número: " + data.codigo_correlativo)
                        hide_loader()

                    }else{
                        hide_loader()
                        show_notify([data.error])
                    }
                }
            })
        }else{
            show_notify(['Debe seleccionar al menos un elemento']);

        }


    });
    $(".continuar-success").click(function(event) {
        /* Act on the event */
        console.log('Continuar success');
        event.preventDefault();
        console.log('DATA PACKING', data_packing)
        window.open (url_reporte_packing_list+'?id_packing='+parseInt(data_packing.id_packing), "_blank")
        data_packing.clean_data()
        hide_message()


        $(".cargar_packing").trigger('click')
     // window.location.href = "{% url 'inspeccionar:listado_elementos_inspeccionados_pdf' %}?{{URL}}"
  });
    $("body").on('change', '.elegir_check', function(event) {
        event.preventDefault();
        var tr = $(this).closest('tr')
        var item =  tr.find('.add-item-filtro')
        var codigo = item.data("codigo")
        var valor = item.val();
        if ($(this).prop('checked')) {
            item.removeAttr('disabled')
            data_packing.add(codigo, valor)
        }else{
            item.attr('disabled', 'disabled')
            data_packing.remove(codigo)
        }
    });
    $('#example-select-all').on('change', function(){
          var rows = tabla_packing.rows({ 'search': 'applied' }).nodes();
          var item, codigo, valor;
          var check = $('input[type="checkbox"].elegir_check', rows).prop('checked', this.checked);
          if ($(this).prop('checked')) {
                check.map(function(index, elem) {
                    item = $(this).closest('tr').find('.add-item-filtro')
                    codigo = item.data("codigo")
                    valor = item.val();
                    item.removeAttr('disabled')
                    data_packing.add(codigo, valor)
                  })
            }else{
                check.map(function(index, elem) {
                    item = $(this).closest('tr').find('.add-item-filtro')
                    codigo = item.data("codigo")
                    valor = item.val();
                    item.attr('disabled', 'disabled')
                    data_packing.remove(codigo)
                  })
            }
   });

$('#datatable_packing_wrapper tfoot input').on('keyup', function () {
            console.log('change')
              var cant_total = 0;
              var peso_total = 0;
              var obj = $('#datatable_packing_wrapper tbody tr').map(function() {
                  var $row = $(this);
                  console.log('row',   $row)
                  var cantidad = $row.find(':nth-child(4)').text()
                  console.log('cantidad', cantidad)
                  var peso = $row.find(':nth-child(12)').text()
                  console.log('peso', peso)
                  if(cantidad) {
                      cant_total += parseFloat(cantidad);
                      if (peso) {

                            peso_total += parseFloat(cantidad*peso)
                      }
                  }

              });
              console.log('***total peso', peso_total)
              $('#id_total_elementos').text(cant_total.toFixed(2))
                $('#id_total_peso').text(peso_total.toFixed(2))
          });



// editar cantidad