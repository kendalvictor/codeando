      $("#id_planta").change(function(event) {
        /* Act on the event */
        var planta = $(this).val()
        var tipo_etapa = $("#id_tipo_etapa").val()
        console.log(planta, tipo_etapa)
        if ((tipo_etapa != -1 ) || (planta != -1 )) {
          show_loader()
          $.ajax({
            url: '/inspeccionar/ajax_get_etapa_inspeccionar/',
            type: 'GET',
            dataType: 'json',
            data: {id_etapa: tipo_etapa, id_planta: planta},
            success: function(data){
                 hide_loader()
              if (data.status==200) {
                $("#id_etapa").find('option').remove()
                $("#id_etapa").append($('<option>', {value: -1, text: '--------------'}));
                $.each(data.result, function(index, val) {
                      $("#id_etapa").append($('<option>', {value: val['intIdEtapa'], text: val['strDeEtapa']}));
                       /* iterate through array or object */
                  });
              }
            }
          })


        }else{
          $("#id_etapa").find('option').remove()
          $("#id_etapa").append($('<option>', {value: -1, text: '--------------'}));
        }
      });


      $("#id_tipo_etapa").change(function(event) {
        /* Act on the event */
        var tipo_etapa = $(this).val()
        var planta = $("#id_planta").val()
        if (tipo_etapa || planta) {
          show_loader()
          $.ajax({
            url: '/inspeccionar/ajax_get_etapa_inspeccionar/',
            type: 'GET',
            dataType: 'json',
            data: {id_etapa: tipo_etapa, id_planta: planta},
            success: function(data){
                 hide_loader()
              if (data.status==200) {
                $("#id_etapa").find('option').remove()
                $("#id_etapa").append($('<option>', {value: -1, text: '--------------'}));
                $.each(data.result, function(index, val) {
                      $("#id_etapa").append($('<option>', {value: val['intIdEtapa'], text: val['strDeEtapa']}));
                       /* iterate through array or object */
                  });
              }
            }
          })


        }else{
          $("#id_etapa").find('option').remove()
          $("#id_etapa").append($('<option>', {value: -1, text: '--------------'}));
        }
      });
   $("#id_intIdProye").change(function(event) {
        var id_proyecto = $(this).val()
        if (id_proyecto) {
          show_loader()
          $.ajax({
            url: '/pcp_paquetes/ajax_get_prioridad_tarea_paquete',
            type: 'GET',
            dataType: 'json',
            data: {id_proyecto: id_proyecto},
            success: function(data){
              hide_loader()
              if (data.status==200) {

                $("#id_intIdPrior").find('option').remove();
                $("#id_intIdPrior").append($('<option>', {value: -1, text: 'TODOS'}));
                $.each(data.list_prioridad, function(index, val) {
                    $("#id_intIdPrior").append($('<option>', {value: val['intIdPrior'], text: val['strDePrior']}));
                });


                $("#id_intIdTarea").find('option').remove();
                $("#id_intIdTarea").append($('<option>', {value: -1, text: 'TODOS'}));
                $.each(data.list_tarea, function(index, val) {
                    $("#id_intIdTarea").append($('<option>', {value: val['intIdTarea'], text: val['strDeTarea']}));
                });

                $("#id_intIdPaque").find('option').remove();
                $("#id_intIdPaque").append($('<option>', {value: -1, text: 'TODOS'}));
                $.each(data.list_paquete, function(index, val) {
                    $("#id_intIdPaque").append($('<option>', {value: val['intIdPaque'], text: val['strDePaque']}));
                });

              }

            }
          })
        }else{
          $("#id_intIdPrior").find('option').remove();
          $("#id_intIdPrior").append($('<option>', {value: -1, text: 'TODOS'}));
          $("#id_intIdTarea").find('option').remove();
          $("#id_intIdTarea").append($('<option>', {value: -1, text: 'TODOS'}));
          $("#id_intIdPaque").find('option').remove();
          $("#id_intIdPaque").append($('<option>', {value: -1, text: 'TODOS'}));
        }
      });


      $("#id_intIdPrior").change(function(event) {
        var id_prioridad = $(this).val()
        var id_proyecto = $('#id_intIdProye').val()
        if (id_prioridad) {
          show_loader()
          $.ajax({
            url: '/pcp_paquetes/ajax_get_prioridad_tarea_paquete',
            type: 'GET',
            dataType: 'json',
            data: {id_prioridad: id_prioridad, id_proyecto:id_proyecto},
            success: function(data){
              hide_loader()
              if (data.status==200) {

                $("#id_intIdTarea").find('option').remove();
                $("#id_intIdTarea").append($('<option>', {value: -1, text: 'TODOS'}));

                $.each(data.list_tarea, function(index, val) {
                    $("#id_intIdTarea").append($('<option>', {value: val['intIdTarea'], text: val['strDeTarea']}));
                     /* iterate through array or object */
                });
                $("#id_intIdPaque").find('option').remove();
                $("#id_intIdPaque").append($('<option>', {value: -1, text: 'TODOS'}));
                $.each(data.list_paquete, function(index, val) {
                    $("#id_intIdPaque").append($('<option>', {value: val['intIdPaque'], text: val['strDePaque']}));
                });

              }

            }
          })
        }else{

          $("#id_intIdTarea").find('option').remove();
          $("#id_intIdTarea").append($('<option>', {value: -1, text: 'TODOS'}));
          $("#id_intIdPaque").find('option').remove();
          $("#id_intIdPaque").append($('<option>', {value: -1, text: 'TODOS'}));
        }
      });



      $("#id_intIdTarea").change(function(event) {
        var id_tarea = $(this).val()
        var id_proyecto = $('#id_intIdProye').val()
        if (id_tarea) {
          show_loader()
          $.ajax({
            url: '/pcp_paquetes/ajax_get_prioridad_tarea_paquete',
            type: 'GET',
            dataType: 'json',
            data: {id_tarea: id_tarea, id_proyecto:id_proyecto},
            success: function(data){
              hide_loader()
              if (data.status==200) {
                $("#id_intIdPaque").find('option').remove();
                $("#id_intIdPaque").append($('<option>', {value: -1, text: 'TODOS'}));

                $.each(data.list_paquete, function(index, val) {
                    $("#id_intIdPaque").append($('<option>', {value: val['intIdPaque'], text: val['strDePaque']}));
                     /* iterate through array or object */
                });
              }

            }
          })
        }else{
          $("#id_intIdPaque").find('option').remove();
          $("#id_intIdPaque").append($('<option>', {value: -1, text: 'TODOS'}));

        }
      });

