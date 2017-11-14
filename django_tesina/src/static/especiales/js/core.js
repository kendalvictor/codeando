// Funcion para  validar fields



    function clean_data(data){
        var data_validar = data
        /*
            DATA EJEMPLO
            data = [
                {
                    id: "id_test",
                    tipo: "select2"
                },
                {
                    id: "id_test",
                    tipo: "select2"
                }
            ]
        */
        result = true
        if(data_validar.length > 0){
            console.log(data_validar)
            $(".error-data").removeClass('error-data')
            $.each(data_validar, function( index, value ) {
                // valida si existe el selector
                if ($(value['id']).length > 0) {
                      if (value['tipo'] == "select2") {
                                $(value['id']).val('');
                        }else{
                            $(value['id']).val('');

                        }
                }else {
                     throw new Error("No se encuentra el selector " + value['id']);
                }
            });
        }else{
           throw new Error("Necesita un Array con object");
        }
        return result;
    }

    function validate_data(data){
        var data_validar = data
        /*
            DATA EJEMPLO
            data = [
                {
                    id: "id_test",
                    tipo: "select2"
                },
                {
                    id: "id_test",
                    tipo: "select2"
                }
            ]
        */
        result = true
        if(data_validar.length > 0){
            console.log(data_validar)
            $(".error-data").removeClass('error-data')
            $.each(data_validar, function( index, value ) {
                // valida si existe el selector
                if ($(value['id']).length > 0) {

                    if($(value['id']).val() == null  || $(value['id']).val() == -1) {
                        $(value['id']).closest('.form-group').find('.select2-selection').addClass('error-data');
                        result = false;
                    }else{

                        if ($(value['id']).val().length > 0) {
                            if (value['tipo'] == "select2") {
                                $(value['id']).closest('.form-group').find('.select2-selection').removeClass('error-data');
                            }else{
                                $(value['id']).removeClass('error-data');

                            }
                        }else {
                            result = false
                            if (value['tipo'] == "select2") {
                                $(value['id']).closest('.form-group').find('.select2-selection').addClass('error-data');
                            }else{
                                $(value['id']).addClass('error-data');
                            }
                        }
                    }
                }else {
                     throw new Error("No se encuentra el selector " + value['id']);
                }
            });
        }
        // else{
        //    throw new Error("Necesita un Array con object");
        // }
        return result;
    }

/******************************************* TABLAS ********************************************/

    // Iniciarlizar Tablas

    var lengauge_table = {
                                "lengthMenu": "Mostrar _MENU_ registros por pagina",
                                "zeroRecords": "No se encontraron registros",
                                "info": "Mostrando pagina _PAGE_ de _PAGES_",
                                "infoEmpty": "No records available",
                                "infoFiltered": "(filtered from _MAX_ total records)",
                                "bFilter": false,
                                "search": "Buscar",
                                "paginate": {
                                    "previous": "Anterior",
                                    "next": "Siguiente"
                                }
                            }

// cargar table con buscador

function search_header_table(list_table){
    console.log('search header table')
    var length_list = list_table.length;
    var i=0;
    if (length_list > 0) {
        for (i; i<length_list; i++) {
             list_table[i].columns().every( function () {
                var that = this;
                $('input[type="text"]', this.footer() ).on( 'keyup change', function () {
                    if ( that.search() !== this.value ) {
                        that
                        .search( this.value )
                        .draw();
                    }
                });
            });

        }
    };
}
function validarNumeros(e){
    var key = window.Event ? e.which : e.keyCode;
    return (key >= 48 && key <= 57 || key==8)
}

// $(".input_numero").keypress(function(e) {
//     /* Act on the event */
//     console.log(e)
//    var key = window.Event ? e.which : e.keyCode;
//     return (key >= 48 && key <= 57 || key==8)
// });
$("body").on('keypress', '.input_numero', function(e) {

    /* Act on the event */
    var key = window.Event ? e.which : e.keyCode;
    return (key >= 48 && key <= 57 || key==8)
});
$("body").on('keyup', '.max_num', function(e) {


    var max = parseInt($(this).attr("data-max"));
    var val = parseInt($(this).val());
    if(val > max)
    {
        $(this).val(max);
        return false;
    }
    // else if(val < min)
    // {
    //     $(this).val(min);
    //     return false;
    // }



});
