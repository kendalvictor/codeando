
      var tabla_paquete = $("#datatablePaquete").DataTable({
            responsive: true,
            dom: 'Bfrtip',
            "language":lengauge_table,

          });
      var estado_paquete = {
          'T': 'Terminado',
          'P': 'Pendiente',
          'R': 'En proceso'
      }
      search_header_table([tabla_paquete])
      $('select').select2();
      $('.date-picker').datepicker({
          });
      $(".dia-libre").click(function(event) {
        /* Act on the event */
        $(".pop-up").addClass('pop-up-active')
      });
      $("body").on('click', '.seleccionar', function(event) {
        event.preventDefault();
        /* Act on the event */

        $("#datatablePaquete tbody tr td").removeClass('dia-seleccionar')

        $(this).closest('tr').find('td').addClass('dia-seleccionar')
      });

      $("#id_intIdProye").change(function(event) {
        var id_proyecto = $(this).val()
        if (id_proyecto) {
          show_loader()
          $.ajax({
            url: '{% url "pcp_paquetes:ajax_get_prioridad" %}',
            type: 'GET',
            dataType: 'json',
            data: {id_proyecto: id_proyecto},
            success: function(data){
              hide_loader()
              if (data.status==200) {
                $("#id_intIdPrior").find('option').remove();
                $("#id_intIdPrior").append($('<option>', {value: -1, text: '--------------'}));

                $.each(data.list_prioridad, function(index, val) {
                    $("#id_intIdPrior").append($('<option>', {value: val['intIdPrior'], text: val['strDePrior']}));
                     /* iterate through array or object */
                });

                $("#id_intIdTarea").find('option').remove();
                $("#id_intIdTarea").append($('<option>', {value: -1, text: '--------------'}));
                $("#id_intIdPaque").find('option').remove();
                $("#id_intIdPaque").append($('<option>', {value: -1, text: '--------------'}));

              }

            }
          })
        }else{
          $("#id_intIdPrior").find('option').remove();
          $("#id_intIdPrior").append($('<option>', {value: -1, text: '--------------'}));
          $("#id_intIdTarea").find('option').remove();
          $("#id_intIdTarea").append($('<option>', {value: -1, text: '--------------'}));
          $("#id_intIdPaque").find('option').remove();
          $("#id_intIdPaque").append($('<option>', {value: -1, text: '--------------'}));
        }
      });


      $("#id_intIdPrior").change(function(event) {
        var id_prioridad = $(this).val()
        if (id_prioridad) {
          show_loader()
          $.ajax({
            url: '{% url "pcp_paquetes:ajax_get_tarea" %}',
            type: 'GET',
            dataType: 'json',
            data: {id_prioridad: id_prioridad},
            success: function(data){
              hide_loader()
              if (data.status==200) {

                $("#id_intIdTarea").find('option').remove();
                $("#id_intIdTarea").append($('<option>', {value: -1, text: '--------------'}));

                $.each(data.list_tarea, function(index, val) {
                    $("#id_intIdTarea").append($('<option>', {value: val['intIdTarea'], text: val['strDeTarea']}));
                     /* iterate through array or object */
                });
                $("#id_intIdPaque").find('option').remove();
                $("#id_intIdPaque").append($('<option>', {value: -1, text: '--------------'}));

              }

            }
          })
        }else{

          $("#id_intIdTarea").find('option').remove();
          $("#id_intIdTarea").append($('<option>', {value: -1, text: '--------------'}));
          $("#id_intIdPaque").find('option').remove();
          $("#id_intIdPaque").append($('<option>', {value: -1, text: '--------------'}));
        }
      });



      $("#id_intIdTarea").change(function(event) {
        var id_tarea = $(this).val()
        if (id_tarea) {
          show_loader()
          $.ajax({
            url: '{% url "pcp_paquetes:ajax_get_paquete" %}',
            type: 'GET',
            dataType: 'json',
            data: {id_tarea: id_tarea},
            success: function(data){
              hide_loader()
              if (data.status==200) {
                $("#id_intIdPaque").find('option').remove();
                $("#id_intIdPaque").append($('<option>', {value: -1, text: '--------------'}));

                $.each(data.list_tarea, function(index, val) {
                    $("#id_intIdPaque").append($('<option>', {value: val['intIdPaque'], text: val['strDePaque']}));
                     /* iterate through array or object */
                });
              }

            }
          })
        }else{
          $("#id_intIdPaque").find('option').remove();
          $("#id_intIdPaque").append($('<option>', {value: -1, text: '--------------'}));

        }
      });
      $(".cargar_paquetes").click(function(event) {
        event.preventDefault()
        var id_proyecto = $("#id_intIdProye").val()
        var id_prioridad = $("#id_intIdPrior").val()
        var id_tarea = $("#id_intIdTarea").val()
        var id_paquete = $("#id_intIdPaque").val()


          show_loader()
         tabla_paquete.clear().draw()
          $.ajax({
            url: '{% url "pcp_paquetes:ajax_get_listado_paquete" %}',
            type: 'GET',
            dataType: 'json',
            data: {
              id_proyecto: id_proyecto,
              id_prioridad: id_prioridad,
              id_tarea: id_tarea,
              id_paquete: id_paquete
            },
            success: function(data){
              hide_loader()
              console.log(data)
              if (data.status==200) {
                var result = []
                var botones = ""
                var estado = ""
                var results = data.list_paquete.map(function(val, index) {
                  console.log(val)
                  result = []
                  result.push(val['strProye'])
                  result.push(val['strDePrior'])
                  result.push(val['strDeTarea'])
                  result.push(val['strDePaque'])
                  estado = '<div class="button-group">'
                  if (val['bitFlHabil']) {
                    estado += '<span class="btn btn--success n-m-b"><i class="fa fa-check"></i></span>'
                  }else{
                    estado += '<span class="btn btn--danger n-m-b"><i class="fa fa-close"></i></span>'
                  }
                  estado += '</div>'


                  result.push(estado)
                  result.push(val['Peso'])
                  result.push(val['Cantidad'])
                  result.push(val['numNuCosto'])
                  result.push(val['dttFeInici'])
                  result.push(val['dttFeTermi'])
                  botones = '<div class="button-group">'
                  if (val['bitFlHabil'] && val['strCoEstad'] == "P" ) {
                    botones += '<a href="" class="btn btn--success n-m-b seleccionar">Seleccionar</a>'
                  }else{
                    if (val['strCoEstad'] != "P") {
                      botones += '<a href="" class="btn btn--info n-m-b">Ver</a><a href="" class="btn btn--warning n-m-b">Contrato</a>'
                    }
                  }
                  botones += '</div>'

                  result.push(estado_paquete[val['strCoEstad']])

                  result.push(botones)
                  return result
                })
                console.log(results)
                tabla_paquete.rows.add(results).draw()
              }

            }
          })

      });
       $("#id_intIdPlant").change(function(event) {
        var id_planta = $(this).val()
        if (id_planta) {
          show_loader()
          $.ajax({
            url: '{% url "pcp_paquetes:ajax_get_etapa" %}',
            type: 'GET',
            dataType: 'json',
            data: {id_planta: id_planta},
            success: function(data){
              hide_loader()
              if (data.status==200) {
                $("#id_intIdEtapa").find('option').remove();
                $("#id_intIdEtapa").append($('<option>', {value: -1, text: '--------------'}));
                $.each(data.list_etapa, function(index, val) {
                    $("#id_intIdEtapa").append($('<option>', {value: val['intIdEtapa'], text: val['strDeEtapa']}));
                     /* iterate through array or object */
                });

              }

            }
          })
        }else{
          $("#id_intIdEtapa").find('option').remove();
          $("#id_intIdEtapa").append($('<option>', {value: -1, text: '--------------'}));
        }
      });
