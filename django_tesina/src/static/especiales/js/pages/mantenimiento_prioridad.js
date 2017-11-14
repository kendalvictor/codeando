/**
 * Created by vvillacorta on 11/08/17.
 */
let comboproyecto = $("#id_intIdProye");
let comboprioridad = $("#id_intIdPrior");
let cargar_grilla = $("#cargar_grilla");
let form_prioridad = $("#form_prioridad");
let iddprioridad = $("#id_iddprioridad");
let form_fecha = $("#form_fecha");
let cargar_fechas = $("#id_cargar_fechas");
let modal_load_prioridad = $("#modal_load_prioridad");
let todos_los_combos = $("#id_intIdProye, #id_intIdPrior");

$('.date-picker').datepicker({});
$('select').select2();

var tabla_prioridad = $("#datatablePrioridad").DataTable({
    responsive: true,
    dom: 'Bfrtip',
    "language":language_datatable,
    "scrollY": 450,
    'scrollCollapse': true,
    "paginate": false
});

function validate_fechamayor(fechaInicial,fechaFinal) {
    var valuesStart=fechaInicial.split("/");
    var valuesEnd=fechaFinal.split("/");
    var dateStart=new Date(valuesStart[2],(valuesStart[1]-1),valuesStart[0]);
    var dateEnd=new Date(valuesEnd[2],(valuesEnd[1]-1),valuesEnd[0]);
    if(dateStart>=dateEnd){
        return false;
    }
    return true;
}

todos_los_combos.change(function(){
    tabla_prioridad.clear().draw()
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
                        comboprioridad.append($('<option>', {value: val['intIdPrior'], text: val['strDePrior']}));
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

cargar_grilla.on("click", function(e) {
    e.preventDefault();

    var data_validar = [
        {
            id: "#id_intIdProye",
            tipo: "select2"
        }
    ];
    if (validate_data(data_validar)) {
        show_loader();
        $.ajax({
            url: url_get_grilla_prioridad,
            type: 'GET',
            dataType: 'json',
            data: form_prioridad.serialize(),
            success: function (data) {
                if (data.result) {
                    tabla_prioridad.clear().draw()
                    console.log("DATA//////////");
                    console.log(data.result)
                    var results = data.result.map(function(val, index) {
                        result = [];
                        result.push(
                          '<center>' +
                          '<button class="btn btn--info edite" data-id_prioridad="'+val['intIdPrior']+'" ' +
                          'data-fecha_inicio="'+val['dttFeInicio']+'" data-fecha_fin="'+val['dttFeTermino']+'"' +
                          'data-str_prioridad="'+val['strDePrior']+'"><i class="fa fa-edit"></i></button>' +
                          '</center>'
                          );
                        result.push(val['strDePrior']);
                        result.push(val['dttFeInicio']);
                        result.push(val['dttFeTermino']);
                        result.push(val['UsuarioCreacion']);
                        result.push(val['dttFeUsuarCreac']);
                        result.push(val['UsuarioModificacion']);
                        result.push(val['dttFechaModif']);
                        return result
                    });
                    tabla_prioridad.rows.add(results).draw();
                }
                hide_loader()
            }
        }).fail(function(jqXHR, status, error){
            show_notify([error]);
            hide_loader()
        });
    }else{
        show_notify(["Seleccione OT"]);
    }
});

$("#datatablePrioridad tbody").on('click', '.edite', function(e){
    e.preventDefault();
    var id_prioridad = $(this).data("id_prioridad");
    var fecha_inicio = $(this).data("fecha_inicio");
    var fecha_fin = $(this).data("fecha_fin");
    var str_prioridad = $(this).data("str_prioridad");

    if(fecha_inicio){$("#id_fechainicio").val(fecha_inicio)}
    if(fecha_fin){$("#id_fechatermino").val(fecha_fin)}
    $("#id_strprioridad").removeAttr('disabled');
    $("#id_strprioridad").val(str_prioridad);
    $("#id_strprioridad").attr("disabled", "disabled");
    iddprioridad.val(id_prioridad);
    modal_load_prioridad.addClass("pop-up-active");
});


cargar_fechas.on("click", function(e) {
    e.preventDefault();
    var campos_validar = [
        {
            id: "#id_fechainicio",
            tipo: "input"
        },
        {
            id: "#id_fechatermino",
            tipo: "input"
        }
    ];
    if (validate_data(campos_validar)) {
        if(validate_fechamayor($("#id_fechainicio").val(), $("#id_fechatermino").val() )){
            $.ajax({
                url: url_grabar_fecha,
                type: 'GET',
                dataType: 'json',
                    data: form_fecha.serialize(),
                success: function (data) {
                    if(data.error){
                        show_notify([data.error]);
                    }else{
                        $("#cerrar-pop-up").trigger("click");
                        cargar_grilla.trigger("click");
                        show_success("Proceso Satisfactorio")
                    }
                    hide_loader()
                }
            }).fail(function(jqXHR, status, error){
                show_notify([error]);
                hide_loader()
                });
        }else{
            show_notify(["Ingrese una Fecha de Inicio inferior a la final"])
        }
        console.log("// id_prioridad ", cargar_fechas.data("id_prioridad"))
    }else{
        show_notify(["Ingrese Fechas requeridas"])
    }
});