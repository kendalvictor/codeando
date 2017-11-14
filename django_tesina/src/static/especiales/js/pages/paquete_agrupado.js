/**
 * Created by vvillacorta on 16/08/17.
 */
var comboproyecto = $("#id_intIdProye");
var combotipoelemento = $("#id_tipo_elemento");
var comboprioridad = $("#id_intIdPrior");
var combotarea = $("#id_intIdTarea");
var combozona = $("#id_zona");
var combocontratista = $("#id_contratista");
var cantidadp = $("#id_cantidadp");
var export_xls = $("#export_xls");
var cargar_data = $("#cargar_data");
var todos_los_combos = $("#id_intIdProye, #id_tipo_elemento, #id_intIdPrior," +
    " #id_intIdTarea, #id_contratista");
var cantidad_maxima = 0;
var data_enviar = {};
$('select').select2();
var tabla_paquete = $("#datatable_paquete").DataTable({
    responsive: true,
    dom: 'Bfrtip',
    "language":language_datatable,
    "scrollY": 420,
    'scrollCollapse': true,
    "paginate": false,
    "footerCallback": function ( row, data, start, end, display ) {
        var api = this.api();
        console.log("callback");
        var intVal = function ( i ) {
            return typeof i === 'string' ?
                i.replace(/[\$,]/g, '')*1 :
                typeof i === 'number' ?
                    i : 0;
        };

        var total_conbono = api
            .column( 9, { page: 'current'} )
            .data()
            .reduce( function (a, b) {
                return intVal(a) + intVal(b);
            }, 0 );

        var total_sinbono = api
            .column( 10, { page: 'current'} )
            .data()
            .reduce( function (a, b) {
                return intVal(a) + intVal(b);
            }, 0 );

        $("#id_con_bono").html(String(total_conbono));
        $("#id_sin_bono").html(String(total_sinbono));
    },
    "createdRow" : function( row, data, index) {
        $.each($(row).find("td").slice(2, 9), function(index, val) {
            if(parseInt($(this).text()) >= parseInt(cantidad_maxima)){
                $(this).addClass("cellgreen")
            }
        });
        $(row).find("td").slice(9, 11).addClass("cellbold")
    }
});

todos_los_combos.change(function(){
    tabla_paquete.clear().draw();
    export_xls.hide()
});

tabla_paquete.columns().every( function () {
    var that = this;
    $( 'input', this.footer() ).on( 'keyup change', function () {
        if (that.search() !== this.value) {
            that
                .search( this.value )
                .draw();
        }
    });
});

comboproyecto.change(function() {
    var id_proyecto = $(this).val();
    combotarea.find('option').not(':first').remove();
    comboprioridad.find('option').not(':first').remove();
    combocontratista.find('option').not(':first').remove();
    combozona.find('option').not(':first').remove();

    if(parseInt(id_proyecto) != -1){
        show_loader();
        var comboajaxprioridad =$.ajax({
            url: url_get_prioridad,
            type: 'GET',
            dataType: 'json',
            data: {"id_proyecto": comboproyecto.val()},
            success: function (data) {
                if (data.list_prioridad) {
                    $.each(data.list_prioridad, function(index, val) {
                        comboprioridad.append($(
                            '<option>', {value: val['intIdPrior'],
                                text: val['strDePrior']})
                        );
                    });
                }
            }
        });

        var comboajaxtarea = $.ajax({
            url: url_get_tarea,
            type: 'GET',
            dataType: 'json',
            data: {
                "id_proyecto": comboproyecto.val(),
                "id_prioridad": comboprioridad.val()
            },
            success: function(data){
                if(data.list_tarea){
                    $.each(data.list_tarea, function(index, val) {
                        combotarea.append($('<option>',
                            {value: val['intIdTarea'],
                                text: val['strDeTarea']})
                        );
                    });
                }
            }
        });

        var comboajaxzona = $.ajax({
            url: url_get_zonas,
            type: 'GET',
            dataType: 'json',
            data: {
                "id_proyecto": comboproyecto.val(),
                "id_tarea": combotarea.val()
            },
            success: function(data){
                if(data.list_zonas){
                    $.each(data.list_zonas, function(index, val) {
                        combozona.append(
                            $('<option>', {value: val['strDeZonas'],
                                text: val['strDeZonas']})
                        );
                    });
                }
            }
        });

        var comboajaxcontratista = $.ajax({
            url: url_get_contratistas,
            type: 'GET',
            dataType: 'json',
            data: {
                'id_proyecto': comboproyecto.val(),
                "id_elemento": combotipoelemento.val()
            },
            success: function(data){
                if (data.result){
                    $.each(data.result, function(index, val) {
                          combocontratista.append(
                              $('<option>', {value: val['intIdContr'],
                                  text: val['strNoEmpre']})
                          );
                    });
                }
            }
        });

        $.when(comboajaxtarea, comboajaxprioridad, comboajaxcontratista,
        comboajaxzona).then(
            function(){
                 hide_loader()
            },
            function(jqXHR, status, error){
                show_notify(["ERROR EN CARGA DE COMBOS : <br> " + error]);
                hide_loader()
            }
        );
    }
});


comboprioridad.change(function() {
    combotarea.find('option').not(':first').remove();

    if(comboproyecto.val() != -1){
        show_loader();
        var comboajaxtarea = $.ajax({
            url: url_get_tarea,
            type: 'GET',
            dataType: 'json',
            data: {
                "id_proyecto": comboproyecto.val(),
                "id_prioridad": comboprioridad.val()
            },
            success: function(data){
                if(data.list_tarea){
                    $.each(data.list_tarea, function(index, val) {
                        combotarea.append($('<option>',
                            {value: val['intIdTarea'],
                                text: val['strDeTarea']})
                        );
                    });
                }
            }
        });

        $.when(comboajaxtarea).then(
            function(){
                 hide_loader()
            },
            function(jqXHR, status, error){
                show_notify(["ERROR EN CARGA DE COMBOS : <br> " + error]);
                hide_loader()
            }
        );
     }
});

combotipoelemento.change(function() {
    combocontratista.find('option').not(':first').remove();

    if(comboproyecto.val() != -1){
        show_loader();
        var comboajaxcontratista = $.ajax({
            url: url_get_contratistas,
            type: 'GET',
            dataType: 'json',
            data: {
                'id_proyecto': comboproyecto.val(),
                "id_elemento": combotipoelemento.val()
            },
            success: function(data){
                if (data.result){
                    $.each(data.result, function(index, val) {
                          combocontratista.append(
                              $('<option>', {value: val['intIdContr'],
                                  text: val['strNoEmpre']})
                          );
                    });
                }
            }
        });

        $.when(comboajaxcontratista).then(
            function(){
                 hide_loader()
            },
            function(jqXHR, status, error){
                show_notify(["ERROR EN CARGA DE COMBOS : <br> " + error]);
                hide_loader()
            }
        );
    }
});

combotarea.change(function() {
    combozona.find('option').not(':first').remove();
    if(comboproyecto.val() != -1){
        $.ajax({
            url: url_get_zonas,
            type: 'GET',
            dataType: 'json',
            data: {
                "id_proyecto": comboproyecto.val(),
                "id_tarea": combotarea.val()
            },
            success: function(data){
                if(data.list_zonas){
                    $.each(data.list_zonas, function(index, val) {
                        combozona.append(
                            $('<option>', {value: val['strDeZonas'],
                                text: val['strDeZonas']})
                        );
                    });
                }
            }
        });
    }
});

$("body").on('keyup change click', '#id_cantidadp', function (e) {
    var cantidad_digitada = $(this).val();

    if(!$.isNumeric(cantidad_digitada)){
        $(this).val("")
    }

    if(parseInt(cantidad_digitada) > 17|| parseInt(cantidad_digitada) <= 0){
        $(this).addClass('error-data');
        if(parseInt(cantidad_digitada) <= 0){
            $(this).val("1")
        }else{
            $(this).val(17)
        }
    }else{
        $(this).removeClass('error-data');
    }
});

cargar_data.on("click", function(e) {
    e.preventDefault();
    data_enviar = {
        "id_proyecto": comboproyecto.val(),
        "id_tipo_elemento": combotipoelemento.val(),
        "id_prioridad": comboprioridad.val(),
        "id_tarea": combotarea.val(),
        "id_zona": combozona.val(),
        "id_contratista": combocontratista.val(),
        "cantidadp": cantidadp.val()
    };

    var data_validar = [
        {
            id: "#id_intIdProye",
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
            id: "#id_cantidadp",
            tipo: "input"
        }
    ];

    if (validate_data(data_validar)) {
        show_loader();
        tabla_paquete.clear().draw();
        export_xls.show();
        $.ajax({
            url: url_get_grilla,
            type: 'GET',
            dataType: 'json',
            data: data_enviar,
            success: function (data) {
                if (data.result){
                    cantidad_maxima = data_enviar['cantidadp'];
                    console.log("DATA ", data);
                    console.log("data_result ", data.result);

                    var results = data.result.map(function(val, index) {
                        result = [];
                        result.push(val['Contratista']);
                        result.push(val['strCoAgrupa']);
                        result.push(val['Dia_01']);
                        result.push(val['Dia_02']);
                        result.push(val['Dia_03']);
                        result.push(val['Dia_04']);
                        result.push(val['Dia_05']);
                        result.push(val['Dia_06']);
                        result.push(val['Dia_07']);
                        result.push(val['ConBono']);
                        result.push(val['SinBono']);
                        return result
                    });
                     tabla_paquete.rows.add(results).draw();

                }
                hide_loader()
            }
        }).fail(function(jqXHR, status, error){
            show_notify([error]);
            hide_loader()
        });
    }else{
        show_notify(["Complete los campos requeridos"])
    }
});


export_xls.on('click', function(e){
    e.preventDefault();
    var filter = "may";

    $.each($('tfoot>tr>th>input'), function() {
      var $row = $(this);

      if(filter != "may"){
          filter += "|" + $row.val()
      }else{
          filter = $row.val()
      }
    });
    var parametros = "";
    $.each(data_enviar, function(key, val) {
        parametros += "&" + key + "=" + val
    });
    window.location.replace(url_xport_xls + filter + parametros)
});



