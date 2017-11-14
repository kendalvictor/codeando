/**
 * Created by vvillacorta on 17/07/17.
 */
var comboproyecto = $("#id_intIdProye");
var combotarea = $("#id_intIdTarea");
var combotipoelemento = $("#id_tipo_elemento");
var tarea_proyecto = $('#id_intIdTarea , #id_intIdProye');
var prioridad_proyecto = $('#id_intIdPrior , #id_intIdProye');
var comboprioridad = $("#id_intIdPrior");
var combozona = $("#id_zona");
var comboagrupador = $("#id_agrupador");
var cargar_data = $(".cargar_data");
var combosituacion = $("#id_situacion");
var grabar_asignacion = $("#id_grabar_asignacion");
var todos_los_combos = $("#id_intIdProye, #id_tipo_elemento, #id_intIdPrior, #id_intIdTarea, #id_zona, #id_situacion");
var select_tabla_asignar = $("#select_tabla_asignar");
var select_tabla_final = $("#select_tabla_final");
$('select').select2();

var tabla_pintura = $("#datatable_pintura").DataTable({
    responsive: true,
    dom: 'Bfrtip',
    "language":language_datatable,
    "scrollY": 420,
    'scrollCollapse': true,
    "paginate": false
});

var table_asignar = $("#datatable_asignar").DataTable({
   "iCookieDuration": 60,
      "iDisplayLength": -1,
      "bStateSave": false,
      "bAutoWidth": false,
      "bRetrieve": true,
      "bJQueryUI": true,
      "bScrollAutoCss": true,
      "bProcessing": true,
      "bPaginate": false,
      "ordering": true,
      "language": language_datatable
});

var table_final = $("#datatable_final").DataTable({
   "iCookieDuration": 60,
      "iDisplayLength": -1,
      "bStateSave": false,
      "bAutoWidth": false,
      "bRetrieve": true,
      "bJQueryUI": true,
      "bScrollAutoCss": true,
      "bProcessing": true,
      "bPaginate": false,
      "ordering": true,
      "language": language_datatable
});

search_header_table([tabla_pintura]);

var data_pintura = {
   ot: '',
   id_acta: 0,
   observacion: '',
   correlativo_acta: '',
   tipo_elemento: '',
   tarea: '',
   zona: '',
   etapa:'',
   situacion:'',
   lote: '',
   row_idpaquete: 0,
   row_codigo: '',
   row_cantidad: 0,
   elementos: {},
   asignaciones : {},
   asigdel : {},
   errorres: {},

   update_filtro: function(data){
       this.ot = data.id_proyecto;
       this.tipo_elemento = data.id_tipo_elemento;
       this.tarea = data.id_tarea;
       this.zona = data.id_zona;
       this.situacion = data.id_situacion
   },

   add: function(codigo, cantidad){
       var self = this;
       if(parseInt(cantidad)){
           self.elementos[codigo] = cantidad
       }else{
           delete self.elementos[codigo]
       }
   },

   add_asig: function(etapa, num){
       var self = this;
       if(etapa){
           self.asignaciones[etapa] = num
       }
   },

   remove: function(codigo){
       var self = this;
       delete self.elementos[codigo]
   },

   remove_asig: function(etapa){
       var self = this;
       delete self.asignaciones[etapa]
   },

   add_remove: function(codigo, cantidad){
       var self = this;
       if(parseInt(cantidad)){
           self.elementos[''+codigo+''] = cantidad
       }else{
           delete self.elementos[''+codigo+'']
       }
   },

   add_data_main: function(idpaquete, codigo, cantidad){
       this.row_idpaquete = idpaquete;
       this.row_codigo = codigo;
       this.row_cantidad = cantidad;
   },

   clean_data: function(){
       this.elementos = {};
       this.asignaciones = {};
       $("#select_tabla_main").prop('checked', false)
   },

   clean_asig: function(){
       this.asignaciones = {};
       this.asigdel = {}
   },

   get_data: function(){
       var self = this;
       var data_json = {
           "ot": self.ot,
           "tipo_elemento":  self.tipo_elemento,
           "tarea": self.tarea,
           "zona": self.zona,
           "lote": self.lote,
           "etapa": self.etapa,
           "situacion": self.situacion,
           "observacion": self.observacion,
           "elementos": self.elementos,
           "asignaciones": self.asignaciones,
           "asigdel": self.asigdel,
           "row_idpaquete": self.row_idpaquete,
           "row_codigo": self.row_codigo,
           "row_cantidad": self.row_cantidad
       };
       return JSON.stringify(data_json)
   },

   get_data_validacion: function(){
       var self = this;
       return {
           "ot": self.ot,
           "row_idpaquete": self.row_idpaquete,
           "row_codigo": self.row_codigo,
           "row_cantidad": self.row_cantidad
       };
   }
};

todos_los_combos.change(function(){
    data_pintura.clean_data();
    tabla_pintura.clear().draw()
});

comboproyecto.change(function() {
    comboprioridad.find('option').not(':first').remove();
    if (comboproyecto.val() != -1){
        show_loader();
        $.ajax({
            url: url_get_prioridad,
            type: 'GET',
            dataType: 'json',
            data: {"id_proyecto": comboproyecto.val()},
            success: function (data) {
                if (data.list_prioridad) {
                    $.each(data.list_prioridad, function(index, val) {
                        $("#id_intIdPrior").append($('<option>', {value: val['intIdPrior'], text: val['strDePrior']}));
                    });
                }
                hide_loader()
            }
        }).fail(function(jqXHR, status, error){
            show_notify(["ERROR COMBO PRIORIDAD: ...." + error]);
            hide_loader()
        });
    }
});


prioridad_proyecto.on('change', function(e) {
    e.preventDefault();
    combotarea.find('option').not(':first').remove();
    if (comboproyecto.val() != -1){
        show_loader();
        $.ajax({
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
                        combotarea.append($('<option>', {value: val['intIdTarea'], text: val['strDeTarea']}));
                    });
                }
                hide_loader()
            }
        }).fail(function(jqXHR, status, error){
            show_notify(["ERROR COMBO TAREA: ...." + error]);
            hide_loader()
        });
    }
});

tarea_proyecto.on('change', function(e) {
    e.preventDefault();
    combozona.find('option').not(':first').remove();
    if (comboproyecto.val() != -1){
        show_loader();

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
                        combozona.append($('<option>', {value: val['strDeZonas'], text: val['strDeZonas']}));
                    });
                }
                hide_loader()
            }
        }).fail(function(jqXHR, status, error){
            show_notify(["ERROR COMBO ZONA: ...." + error]);
            hide_loader()
        });
    }
});

cargar_data.click(function(e) {
    e.preventDefault();

    var data_enviar = {
        "id_proyecto": comboproyecto.val(),
        "id_tarea": combotarea.val(),
        "id_tipo_elemento": combotipoelemento.val(),
        "id_zona": combozona.val(),
        "id_situacion": combosituacion.val()
    };

    var data_validar = [
        {
            id: "#id_intIdProye",
            tipo: "select"
        },
        {
            id: "#id_intIdTarea",
            tipo: "select"
        }
    ];

    if (validate_data(data_validar)) {
        data_pintura.update_filtro(data_enviar);
        tabla_pintura.clear().draw();
        table_final.clear().draw();
        data_pintura.clean_asig();
        show_loader();
        $.ajax({
            url: url_get_grilla,
            type: 'GET',
            dataType: 'json',
            data: data_enviar,
            success: function (data) {
                if (data.result){
                    console.log("DATA ", data);
                    console.log("data_result ", data.result);
                    var total_elementos = 0;
                    var total_peso = 0;
                    var total_area = 0;
                    var results = data.result.map(function(val, index) {
                        result = [];
                        console.log("intIdPaque", val['intIdPaque']);
                        console.log("Incompleto", val['Incompleto']);
                        var input = '<input name="input_check" class="elegir_check" type="checkbox" data-id-paquete="'+val['intIdPaque']+'"  data-incompleto="' +val['Incompleto'] + '">';
                        result.push(input);
                        result.push(val['strCoEleme']);
                        result.push(val['intnurevis']);
                        result.push(val['Cantidad']);
                        result.push('<input type="number" disabled="disabled" value="'+val['Cantidad']+'" class="max_num add-item-filtro" data-codigo="'+val["intIdPaque"]+'|'+val['strCoEleme']+'|'+val['Paquete']+'" data-max="'+val['Cantidad']+'"/>');
                        result.push(val['Prioridad']);
                        result.push(val['Tarea']);
                        result.push(val['Paquete']);
                        result.push(val['strNoEleme']);
                        result.push(val['strDePerfi']);
                        result.push(val['numNuLongi']);
                        result.push(val['numNuPesosNetos']);
                        result.push(val['numNuAreas']);

                        total_peso += parseFloat(val['Cantidad']) * parseFloat(val['numNuPesosNetos']);
                        total_area += parseFloat(val['Cantidad']) * parseFloat(val['numNuAreas']);
                        total_elementos += parseFloat(val['Cantidad']);
                        return result

                    });
                    $('#select_tabla_main').prop("checked", false);
                     tabla_pintura.rows.add(results).draw();
                     colorear_incompletos();
                     $('#id_total_elementos').text(parseFloat(total_elementos).toFixed(2));
                     $('#id_total_peso').text(parseFloat(total_peso).toFixed(2));
                     $('#id_total_area').text(parseFloat(total_area).toFixed(2))
                }
                hide_loader()
            }
        }).fail(function(jqXHR, status, error){
            show_notify(["ERROR EN CARGA TABLA: <br> " + error]);
            hide_loader()
        });
    }else{
        show_notify(["Complete los campos obligatorios <br>"]);
    }
});

$('#select_tabla_main').on('change', function(){
    var rows = tabla_pintura.rows({ 'search': 'applied' }).nodes();
    var item, codigo, valor;
    var check = $('input[type="checkbox"].elegir_check', rows).prop('checked', this.checked);
    if ($(this).prop('checked')) {
        check.map(function(index, elem){
                item = $(this).closest('tr').find('.add-item-filtro');
                codigo = item.data("codigo");
                valor = item.val();
                item.removeAttr('disabled');
                data_pintura.add(codigo, valor)
        })
    }else{
        check.map(function(index, elem) {
            item = $(this).closest('tr').find('.add-item-filtro');
            codigo = item.data("codigo");
            valor = item.val();
            item.attr('disabled', 'disabled');
            data_pintura.remove(codigo)
        })
    }
});

function colorear_incompletos(){
    var rows = tabla_pintura.rows({ 'search': 'applied' }).nodes();
    var check = $('input[type="checkbox"].elegir_check', rows);
    check.map(function(index, elem) {
        if ($(this).data('incompleto') == 'R'){
            $(this).closest('tr').css('background', '#d9534f')
        }
    })
}

$("body").on('keyup change click', '.add-item-filtro', function (e) {
    var codigo = $(this).data("codigo");
    var cantidad_maxima = $(this).data("max");
    var cantidad_digitada = $(this).val();

    if(!$.isNumeric(cantidad_digitada)){
        $(this).val("")
    }

    if(parseInt(cantidad_digitada) > parseInt(cantidad_maxima) || parseInt(cantidad_digitada) <= 0){
        $(this).addClass('error-data');
        if(parseInt(cantidad_digitada) <= 0){
            $(this).val("1")
        }else{
            $(this).val(cantidad_maxima)
        }
    }else{
        $(this).removeClass('error-data');
    }
    data_pintura.add_remove(codigo, $(this).val())
});

$("body").on('change', '.elegir_check', function(e) {
     e.preventDefault();
     var tr = $(this).closest('tr');
     var item =  tr.find('.add-item-filtro');
     var codigo = item.data("codigo");
     var valor = item.val();

     if ($(this).prop('checked')) {
         item.removeAttr('disabled');
         data_pintura.add(codigo, valor);
     }else{
         item.attr('disabled', 'disabled');
         data_pintura.remove(codigo)
     }
 });

$('#datatable_pintura_wrapper tfoot input').on('keyup', function () {
    var cant_total = 0;
    var peso_total = 0;
    var area_total = 0;
    var obj = $('#datatable_pintura_wrapper tbody tr').map(function() {
        var $row = $(this);
        var cantidad = $row.find(':nth-child(4)').text();
        var peso = $row.find(':nth-child(12)').text();
        var area = $row.find(':nth-child(13)').text();
        if(cantidad) {
            cant_total += parseFloat(cantidad);
            if (peso) {
                peso_total += parseFloat(cantidad*peso)
            }
            if (area) {
                area_total += parseFloat(cantidad*area)
            }
        }
    });
    $('#id_total_elementos').text(cant_total.toFixed(2));
    $('#id_total_peso').text(peso_total.toFixed(2));
    $('#id_total_area').text(area_total.toFixed(2))
});

table_asignar.columns().every( function () {
    var that = this;
    $( 'input', this.footer() ).on( 'keyup change', function () {
        if (that.search() !== this.value) {
            that
                .search( this.value )
                .draw();
        }
    });
});

function add_row_since_assign(concat, orden, nombre_etapa, nombre_planta){
    var ya_existe = false;

    $.each(data_pintura.asignaciones, function(concat_final, val){
        if(concat_final === concat){
            ya_existe = true;
            return false
        }
    });

    if(!ya_existe){
        data_pintura.add_asig(concat, orden);
        var result = [];
        var input = '<input name="input_check_final" checked class="check_final" type="checkbox" data-concat="'+ concat +'">';
        result.push(input);
        result.push(nombre_etapa);
        result.push(nombre_planta);
        table_final.row.add(result).draw();
        console.log("ADD ", concat ,orden, nombre_etapa, nombre_planta)
    }
}

function del_row_since_assign(concat, filas_tabla_final) {
    data_pintura.remove_asig(concat);
     $.each(filas_tabla_final, function(index, val){
         var fila = $(this);
         var concat_final = fila.find(".check_final").data("concat");
         if(concat_final && concat_final === concat){
             table_final
                 .row(fila)
                 .remove()
                 .draw();
             console.log("DEL ", concat)
         }
     });
}

function del_row_since_final(fila, concat, filas_tabla_assign){
    data_pintura.remove_asig(concat);
    table_final
        .row(fila)
        .remove()
        .draw();
    console.log("DEL ", concat);
    var list_concat = concat.split("|");
    if(list_concat[2] === comboagrupador.val()){
        $.each(filas_tabla_assign, function(index, val){
            var check_asignar = $(this).find(".check_asignar");
            if(list_concat[0] == check_asignar.data("id_etapa") && list_concat[1] == check_asignar.data("id_planta")){
                check_asignar.prop("checked", false);
                return false
            }
        });
    }
}

$("body").on('change', '.check_asignar', function(e){
    e.preventDefault();
    var item = $(this);
    var columnas = item.closest("tr").children("td");
    var nombre_etapa = columnas.eq(1).text();
    var nombre_planta = columnas.eq(2).text();
    var orden = item.data("orden");
    var concat = item.data("id_etapa") + "|" + item.data("id_planta") + "|" + comboagrupador.val();
    var filas_tabla_final = $("#datatable_final").find("tr");

    if (item.prop('checked')) {
        add_row_since_assign(concat ,orden, nombre_etapa, nombre_planta)
    }else{
        del_row_since_assign(concat, filas_tabla_final)
    }
    select_tabla_final.prop("checked", true)
});

$("body").on('change', '.check_final', function(e){
    e.preventDefault();
    var item = $(this);
    var concat = item.data("concat");
    var tr = item.closest("tr");
    var filas_tabla_assign = $("#datatable_asignar").find("tr");

    if (item.prop('checked')) {
    }else{
        del_row_since_final(tr, concat, filas_tabla_assign)
    }
});

select_tabla_asignar.on('click', function(){
    var rows = table_asignar.rows({ 'search': 'applied' }).nodes();
    $('input[type="checkbox"]', rows).prop('checked', this.checked);
    var check = $('input[type="checkbox"].check_asignar', rows).prop('checked', this.checked);

    if ($(this).prop('checked')) {
        check.map(function(index, elem){
            var item = $(this);
            var columnas = item.closest("tr").children("td");
            var nombre_etapa = columnas.eq(1).text();
            var nombre_planta = columnas.eq(2).text();
            var orden = item.data("orden");
            var concat = item.data("id_etapa") + "|" + item.data("id_planta") + "|" + comboagrupador.val();
            add_row_since_assign(concat ,orden, nombre_etapa, nombre_planta)
        })
    }else{
        check.map(function(index, elem) {
            var item = $(this);
            var filas_tabla_final = $("#datatable_final").find("tr");
            var concat = item.data("id_etapa") + "|" + item.data("id_planta") + "|" + comboagrupador.val();
            del_row_since_assign(concat, filas_tabla_final)
        })
    }
});

select_tabla_final.on('click', function(){
    var rows = table_final.rows({ 'search': 'applied' }).nodes();
    $('input[type="checkbox"]', rows).prop('checked', this.checked);
    var check = $('input[type="checkbox"].check_final', rows).prop('checked', this.checked);

    if ($(this).prop('checked')){
    }else{
        check.map(function(index, elem){
            var item = $(this);
            var concat = item.data("concat");
            if(concat){
                var tr = item.closest("tr");
                var filas_tabla_assign = $("#datatable_asignar").find("tr");
                del_row_since_final(tr, concat, filas_tabla_assign)
            }
        })
    }
});

comboagrupador.on('change', function() {
    table_asignar.clear().draw();
    show_loader();
    $.ajax({
        url: url_get_grilla_asignar,
        type: 'GET',
        dataType: 'json',
        data: {
            "id_proyecto": comboproyecto.val(),
            "id_agrupador": comboagrupador.val()
        },
        success: function(data){
            if (data.result) {
                var results = data.result.map(function(val, index) {
                    result = [];
                    var text_check = '';
                    var concat_assign = val['INTIDETAPA'] + "|" + val['intIdPlant'] + "|" + comboagrupador.val();
                    $.each(data_pintura.asignaciones, function(concat_final, val){
                        if(concat_final === concat_assign){
                            text_check = 'checked';
                            return false
                        }
                    });
                    var input = '<input name="input_check_asignar" class="check_asignar" type="checkbox" '+ text_check +' data-orden="'+val['INTNUORDEN']+'"  data-id_etapa="' +val['INTIDETAPA'] + '" data-id_planta="' + val['intIdPlant'] + '">';
                    result.push(input);
                    result.push(val['strDeEtapa']);
                    result.push(val['Planta']);
                    return result
                 });
                 select_tabla_asignar.prop("checked", false);
                 select_tabla_final.prop("checked", true);
                 table_asignar.rows.add(results).draw();
            }
            $("#modal_load_acta").addClass("pop-up-active");
            $("#modal_load_acta").addClass("pop-up-active");
            hide_loader();
        }
    }).fail(function(jqXHR, status, error){
        show_notify(["ERROR EN CARGA TABLA DE ASIGNACION: <br> " + error]);
        hide_loader()
    });
});

$(".generar_asignacion").on("click", function(e){
    e.preventDefault();
    data_pintura.clean_asig();
    table_final.clear().draw();
    if (Object.values(data_pintura.elementos).length > 0){
        comboagrupador.trigger("change")
    }else{
        show_notify(['Debe seleccionar al menos un elemento']);
    }
});

grabar_asignacion.on("click", function(e){
    e.preventDefault();
    if (Object.values(data_pintura.asignaciones).length > 0){
        /*
        $.each(data_pintura.elementos, function(data_concat, val){
            console.log("elementos : ", data_concat, val);
            var list_concat = data_concat.split("|");
            data_pintura.add_data_main(list_concat[0], list_concat[1], val);
            show_loader();
            $.ajax({
                url: url_post_validacion,
                type: 'POST',
                data: data_pintura.get_data_validacion,
                dataType: 'json',
                success: function(data){
                    console.log("DATAAAAAAA");
                    if (data.error) {
                        show_notify(["ERROR DETECTADO: <br> " + data.error]);
                    }else{
                        data_pintura.clean_data();
                        cargar_data.trigger('click');
                        $("#cerrar-pop-up").trigger('click');
                        console.log(data);
                    }
                    hide_loader()
                }
            }).fail(function(jqXHR, status, error){
                show_notify(["ERROR EN GENERACION DE ACTA : <br> " + error]);
                hide_loader()
            });
        });
        */

        show_loader();
        console.log("%%%%%%%%%%");
        console.log(data_pintura.asignaciones);
        console.log("%%%%%%%%%%");
        $.ajax({
            url: url_post_asignacion,
            type: 'POST',
            data: {"serialize_array": data_pintura.get_data()},
            dataType: 'json',
            success: function(data){
                console.log("DATAAAAAAA");
                if (data.error) {
                    show_notify_2([ data.error]);
                }else{
                    data_pintura.clean_data();
                    cargar_data.trigger('click');
                    $("#cerrar-pop-up").trigger('click');
                    show_success('Se grabó correctamente')
                }
                hide_loader()
            }
        }).fail(function(jqXHR, status, error){
            show_notify_2([error]);
            hide_loader()
        });
    }else{
        show_notify(['Debe seleccionar al menos un elemento a asignar']);
    }
});

function hide_notify_2(){
    $(".notify2").removeClass('notify-activate')
}

function show_notify_2(data){
    var li = "";
    $(".notify2 ul li").remove();
    $(".notify2").addClass("notify--danger");
    $(".notify2").removeClass("notify--success");
    if (data) {
        $.each(data, function(val, index) {
             li += "<li>"+index+"</li>"
        });
        $(".notify2 ul").append(li);
        $(".notify2").addClass('notify-activate');
    }
}

$("#id_close_errors").on("click", function(e){
    hide_notify_2()
});
