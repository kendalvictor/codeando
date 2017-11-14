/**
 * Created by vvillacorta on 12/07/17.
 */

var comboproyecto = $("#id_intIdProye");
var combotarea = $("#id_intIdTarea");
var cargar_data = $(".cargar_data");
var todos_los_combos = $("#id_intIdProye, #id_intIdTarea, #id_lote, #id_etapa, #id_situacion");
$('select').select2();
$("#id_observacion").autosize();
var tabla_acta_final = $("#datatable_packing").DataTable({
    responsive: true,
    dom: 'Bfrtip',
    "language":lengauge_table,
    "scrollY": 420,
    'scrollCollapse': true,
    "paginate": false
});

search_header_table([tabla_acta_final]);

var data_packing = {
   ot: '',
   id_acta: 0,
   observacion: '',
   correlativo_acta: '',
   tipo_elemento: '',
   tarea: '',
   zona: '',
   planta:'',
   etapa:'',
   situacion:'',
   lote: '',
   elementos: {},

   update_filtro: function(data){
       this.ot = data.id_proyecto;
       this.tipo_elemento = data.id_tipo_elemento;
       this.tarea = data.id_tarea;
       this.planta = data.id_planta;
       this.zona = data.id_zona;
       this.lote = data.id_lote;
       this.etapa = data.id_etapa;
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
           "ot": self.ot,
           "tipo_elemento":  self.tipo_elemento,
           "tarea": self.tarea,
           "zona": self.zona,
           "lote": self.lote,
           "planta": self.planta,
           "etapa": self.etapa,
           "elementos": self.elementos,
           "situacion": self.situacion,
           "observacion": self.observacion
       };
       return JSON.stringify(data_json)
   }
};

comboproyecto.change(function() {
    var id_proyecto = $(this).val();
    $("#id_etapa").find('option').not(':first').remove();
    combotarea.find('option').not(':first').remove();
    $("#id_lote").find('option').not(':first').remove();

    if (parseInt(id_proyecto) != -1) {
        show_loader();
        var comboajaxetapa = $.ajax({
            url: url_get_etapa,
            type: 'GET',
            dataType: 'json',
            data: {id_proyecto: id_proyecto},
            success: function (data) {
                if (data.result) {
                    $.each(data.result, function (index, val) {
                        $("#id_etapa").append($('<option>', {value: val[0], text: val[2]}));
                    });
                }
            }
        });
        var comboajaxtarea = $.ajax({
            url: url_get_tarea,
            type: 'GET',
            dataType: 'json',
            data: {"id_proyecto": id_proyecto},
            success: function (data) {
                if (data.result) {
                    $.each(data.result, function (index, val) {
                        combotarea.append($('<option>', {value: val['intIdTarea'], text: val['strDeTarea']}));
                    });
                }
            }
        });
        var combolote = $.ajax({
            url: url_get_lote,
            type: 'GET',
            dataType: 'json',
            data: {
                "id_proyecto": id_proyecto,
                "id_tarea": combotarea.val()
            },
            success: function (data) {
                if (data.result){
                    $.each(data.result, function (index, val) {
                        $("#id_lote").append($('<option>', {value: val["intIdPacking"], text: val["strNuLote"]}));
                    });
                }
            }
        });
        $.when(comboajaxetapa, comboajaxtarea, combolote).then(
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
    if(parseInt(comboproyecto.val()) != -1){
        show_loader();
        $("#id_lote").find('option').not(':first').remove();
        $.ajax({
            url: url_get_lote,
            type: 'GET',
            dataType: 'json',
            data: {
                "id_proyecto": comboproyecto.val(),
                "id_tarea": combotarea.val()
            },
            success: function (data) {
                if (data.result){
                    $.each(data.result, function (index, val) {
                        $("#id_lote").append($('<option>', {value: val["intIdPacking"], text: val["strNuLote"]}));
                    });
                }
                hide_loader()
            }
        }).fail(function(jqXHR, status, error){
            show_notify(["ERROR EN CARGA DE COMBOS : <br> " + error]);
            hide_loader()
        });
    }
});


todos_los_combos.change(function() {
    tabla_acta_final.clear().draw();
    data_packing.clean_data();
});


cargar_data.click(function(e) {
    e.preventDefault();

    var data_enviar = {
        id_proyecto: comboproyecto.val(),
        id_tarea: combotarea.val(),
        id_lote: $("#id_lote").val(),
        id_etapa: $("#id_etapa").val(),
        id_situacion: $("#id_situacion").val()
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
            id: "#id_lote",
            tipo: "select"
        },
        {
            id: "#id_etapa",
            tipo: "select"
        }
    ];

    if (validate_data(data_validar)) {
        data_packing.update_filtro(data_enviar);
        tabla_acta_final.clear().draw();
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
                    var results = data.result.map(function(val, index) {
                        result = [];
                        console.log("intIdPaque", val['intIdPaque']);
                        console.log("Incompleto", val['Incompleto']);
                        var input = '<input name="input_check" class="elegir_check" type="checkbox" data-id-paquete="'+val['intIdPaque']+'"  data-incompleto="' +val['Incompleto'] + '">';
                        result.push(input);
                        result.push(val['strCoEleme']);
                        result.push(val['intnurevis']);
                        result.push(val['Cantidad']);
                        result.push('<input type="number" disabled="disabled" value="'+val['Cantidad']+'" class="max_num add-item-filtro" data-codigo="'+val["intIdPaque"]+'|'+val['strCoEleme']+'" data-max="'+val['Cantidad']+'" />');
                        result.push(val['Prioridad']);
                        result.push(val['Tarea']);
                        result.push(val['Paquete']);
                        result.push(val['strNoEleme']);
                        result.push(val['strDePerfi']);
                        result.push(val['numNuLongi']);
                        result.push(val['numNuPesosNetos']);
                        result.push(val['numNuAreas']);
                        result.push(val['EtapaSiguiente']);
                        result.push(val['EtapaAnterior']);

                        total_peso += parseFloat(val['Cantidad']) * parseFloat(val['numNuPesosNetos'])
                        total_elementos += parseFloat(val['Cantidad'])
                        return result

                    });
                     tabla_acta_final.rows.add(results).draw();
                     colorear_incompletos()
                     console.log('total elementos', total_elementos);
                     console.log('total peso', total_peso);
                     $('#id_total_elementos').text(parseFloat(total_elementos).toFixed(2))
                     $('#id_total_peso').text(parseFloat(total_peso).toFixed(2))
                }
                hide_loader()
            }
        }).fail(function(jqXHR, status, error){
            show_notify(["ERROR EN CARGA TABLA : <br> " + error]);
            hide_loader()
        });
    }else{
        show_notify(["Complete los campos obligatorios <br> "]);
    }
});

$('#example-select-all').on('change', function(){
    var rows = tabla_acta_final.rows({ 'search': 'applied' }).nodes();
    var item, codigo, valor;
    var check = $('input[type="checkbox"].elegir_check', rows).prop('checked', this.checked);
    if ($(this).prop('checked')) {
        check.map(function(index, elem){
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

function colorear_incompletos(){
    var rows = tabla_acta_final.rows({ 'search': 'applied' }).nodes();
    var check = $('input[type="checkbox"].elegir_check', rows);
    check.map(function(index, elem) {
        if ($(this).data('incompleto') == 'R'){
            $(this).closest('tr').css('background', '#d9534f');
        }
    })
}

$("body").on('keyup change click', '.add-item-filtro', function (e) {
    console.log("")
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
    data_packing.add_remove(codigo, $(this).val())
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

$('#datatable_packing_wrapper tfoot input').on('keyup', function () {
    var cant_total = 0;
    var peso_total = 0;
    var obj = $('#datatable_packing_wrapper tbody tr').map(function() {
        var $row = $(this);
        var cantidad = $row.find(':nth-child(4)').text();
        var peso = $row.find(':nth-child(12)').text();
        if(cantidad) {
            cant_total += parseFloat(cantidad);
            if (peso) {
                peso_total += parseFloat(cantidad*peso)
            }
        }
    });
    $('#id_total_elementos').text(cant_total.toFixed(2));
    $('#id_total_peso').text(peso_total.toFixed(2))
});


$(".generar_packing").on("click", function(e) {
    e.preventDefault();
    $("#id_observacion").val("");
    if (Object.values(data_packing.elementos).length > 0) {
        $("#modal_load_acta").addClass("pop-up-active");
    }else{
        show_notify(['Debe seleccionar al menos un elemento']);
    }
});

$("#send_acta").on("click", function(e) {
    e.preventDefault();
    data_packing.observacion = $("#id_observacion").val();
    if (Object.values(data_packing.elementos).length > 0) {
        show_loader();
        $.ajax({
            url: url_post_acta_list,
            type: 'POST',
            data: {"serialize_array": data_packing.get_data()},
            dataType: 'json',
            success: function(data){
                console.log("DATAAAAAAA");
                console.log(data)
                if (data.error) {
                    show_notify(["ERROR DETECTADO: <br> " + data.error]);
                }else{
                    data_packing.correlativo_acta = data.stracta;
                    data_packing.id_acta = data.intacta;
                    show_success("Se generó el packing list con número: " + data.stracta);
                }
                hide_loader()
            }
        }).fail(function(jqXHR, status, error){
            show_notify(["ERROR EN GENERACION DE ACTA : <br> " + error]);
            hide_loader()
        });
    }else{
        show_notify(['Debe seleccionar al menos un elemento']);
    }
});


$(".continuar-success").click(function(e) {
    e.preventDefault();
    console.log('DATA ACTA', data_packing);
    window.open (url_reporte_acta+'?id_acta='+parseInt(data_packing.id_acta), "_blank");
    data_packing.clean_data();
    hide_message();
    cargar_data.trigger('click');
    $("#cerrar-pop-up").trigger('click')
});
