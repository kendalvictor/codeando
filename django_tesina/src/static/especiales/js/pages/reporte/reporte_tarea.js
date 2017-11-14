$(document).ready(function () {
    let select_zona = $('#select-zona');
    let select_ot = $('#select-ot');
    let select_tipoelemento = $('#select_tipoelemento');
    let select_etapa = $('#select-etapa');
    let select_unidad = $('#select-unidad');
    let btn_search = $('#btn-search');
    let projectBlock = $('#load-tree .prjBlockTree .openDetail');
    let load_tree = $("#load-tree");
    let loading = $("#overlay");
    let input_filter_tarea = $("#search_report_tarea");
    let input_filter_etapa = $("#search_report_etapa");
    let modal_paquete = $('#modal_paquete');

    let check_all_printer = $("#check_all_printer");


    function fileExists(url) {
        if (url) {
            const req = new XMLHttpRequest();
            req.open('GET', url, false);
            req.send();
            return req.status === 200;
        } else {
            return false;
        }
    }
    select_tipoelemento.select2();
    let wSelectOT = select_ot.select2()
        .on("change", function () {
            let _ot = $(this).val();
            select_zona.children('option:not(:first)').remove();
            const _parameter = {'proyecto_id': _ot};
            $.get(URL_AREA, _parameter, function (data) {
            }).done(function (data) {
                const _data = JSON.parse(data);
                $.each(_data, function (index, value) {
                    select_zona
                        .append($("<option></option>")
                            .attr("value", value[0])
                            .attr("data-text", value[0])
                            .text(value[0]));
                });
                select_zona.select2();
            });

            select_etapa.children('option:not(:first)').remove();
            $.get(URL_ETAPA, _parameter, function (data) {
            }).done(function (data) {
                $.each(data, function (index, value) {
                    select_etapa
                        .append($("<option></option>")
                            .attr("value", value.intIdEtapa)
                            .text(value.strDeEtapa));
                });
                select_etapa.select2();
            });
        });


    select_unidad.select2();

    btn_search.on('click', function () {
        let _ot = select_ot.val();
        let _zone = $("#select-zona option:selected").attr("data-text");
        let _unit = select_unidad.val();
        let _etapa = select_etapa.val();
        let _tipoelemento = select_tipoelemento.val();

        const _parameter = {
            'proyecto_id': _ot,
            'zona_id': _zone,
            'unidad_id': _unit,
            'etapa_id': _etapa,
            'tipoelemento_id': _tipoelemento
        };

        if (_ot === "-1") {
            loading.show();
            $.get(URL_TAREA, _parameter ,function(data) {
                if (data[0] === undefined) {
                    load_tree.empty();
                    let html_tarea = `<tr style="background-color: rgba(0, 208, 255, 0.25)">
                                <td colspan="15" style="text-align: center">No hay Registros</td>
                            </tr>`;
                    load_tree.append(html_tarea)

                } else {
                    swal("procesado", "Se ha cargado la informacion", "success");
                    $(".wResultsStore").remove();
                    load_tree.empty();
                    for (let i = 0; i < (data.length - 1); i++) {
                        let el = data[i];
                        let html_tarea = `<tr class="prjBlockTree"  data-id="${ el.id_proyecto }">
                                    <td style="width:99px;" class="openDetail">
                                        <i class="fa fa-plus" aria-hidden="true"></i> OT
                                        <i class="fa fa-refresh fa-spin fa-fw hidden"></i>
                                    </td>
                                    <td style="width: 100px;text-align: center">${ el.descripcion }</td>
                                    <td style="width: 100px;text-align: center">${ el.CantEtapa }</td>
                                    <td style="width: 100px;text-align: center">${ el.CantZona }</td>
                                    <td style="width: 100px;text-align: center">${ el.TotalF }</td>
                                    <td style="width: 100px;text-align: center">${ el.ProgramaF }</td>
                                    <td style="width: 100px;text-align: right">${ el.CantF }</td>
                                    <td style="width: 100px;text-align: right">${ el.CantIF }</td>
                                    <td style="width: 100px;text-align: right">${ el.CantGran }</td>
                                    <td style="width: 100px;text-align: right">${ el.CantPint }</td>
                                    <td style="width: 100px;text-align: right">${ el.CantEFG }</td>
                                    <td style="width: 100px;text-align: right">${ el.CantIG }</td>
                                    <td style="width: 100px;text-align: right">${ el.CantEGA }</td>
                                    <td style="width: 100px;text-align: right">${ el.CantAKit }</td>
                                    <td style="width: 100px;text-align: right">${ el.CantIAKit }</td>
                                    <td style="width: 100px;text-align: right">${ el.Despacho }</th>
                                </tr>`;
                        load_tree.append(html_tarea)
                    }

                    for (let i = (data.length - 1); i < data.length; i++) {
                        let el = data[i];
                        let html_tarea = `<tr class="tree-${ el.id_proyecto}">
                                    <td style="width:103px;"></td>
                                    <td style="width:99px;font-size: 15px;text-align: right"><strong>${ el.descripcion }</strong></td>
                                    <td style="width:100px;text-align: right">${ el.CantEtapa }</td>
                                    <td style="width:100px;text-align: right">${ el.CantZona }</td>
                                    <td style="width:99px;font-size: 15px;text-align: right"><strong>${ el.TotalF }</strong></td>
                                    <td style="width:99px;font-size: 15px;text-align: right"><strong>${ el.ProgramaF }</strong></td>
                                    <td style="width:99px;font-size: 15px;text-align: right"><strong>${ el.CantF }</strong></td>
                                    <td style="width:99px;font-size: 15px;text-align: right"><strong>${ el.CantIF }</strong></td>
                                    <td style="width:99px;font-size: 15px;text-align: right"><strong>${ el.CantGran }</strong></td>
                                    <td style="width:99px;font-size: 15px;text-align: right"><strong>${ el.CantPint }</strong></td>
                                    <td style="width:100px;font-size: 15px;text-align: right"><strong>${ el.CantEFG }</strong></td>
                                    <td style="width:100px;font-size: 15px;text-align: right"><strong>${ el.CantIG }</strong></td>
                                    <td style="width:100px;font-size: 15px;text-align: right"><strong>${ el.CantEGA }</strong></td>
                                    <td style="width:100px;font-size: 15px;text-align: right"><strong>${ el.CantAKit }</strong></td>
                                    <td style="width:100px;font-size: 15px;text-align: right"><strong>${ el.CantIAKit }</strong></td>
                                    <td style="width:100px;font-size: 15px;text-align: right"><strong>${ el.Despacho }</strong></td>
                                </tr>`;
                        load_tree.append(html_tarea)
                    }
                }
                loading.hide()
            });
            return false;
        }
        loading.show()
        $.get(URL_TAREA, _parameter, function (data) {
        }).done(function (data) {
            if (data[0] === undefined) {
                load_tree.empty();
                let html_tarea = `<tr style="background-color: rgba(0, 208, 255, 0.25)">
                            <td colspan="15" style="text-align: center">No hay Registros</td>
                        </tr>`;
                load_tree.append(html_tarea)

            } else {
                swal("procesado", "Se ha cargado la informacion", "success");
                $(".wResultsStore").remove();
                load_tree.empty();
                for (let i = 0; i < (data.length - 1); i++) {
                    let el = data[i];
                    let html_tarea = `<tr id="tree-jonap-${ el.id_tarea}" data-id=${ el.id_tarea} data-open="false" class="tree-jonap tree-${ el.id_tarea}" style="background-color: rgba(0, 208, 255, 0.25)">
                                <td class="fa-hover" style="width:99px;">
                                    <a href="javascript:void(0)">
                                        <i class="fa fa-plus" aria-hidden="true"></i> Tarea
                                        <i class="fa fa-refresh fa-spin fa-fw hidden"></i>
                                    </a>
                                </td>
                                <td style="width: 100px;text-align: center">${ el.descripcion }</td>
                                <td style="width:100px;text-align: center">${ el.CantEtapa }</td>
                                <td style="width:100px;text-align: center">${ el.CantZona }</td>
                                <td style="width: 100px;text-align: center">${ el.TotalF }</td>
                                <td style="width: 100px;text-align: center">${ el.ProgramaF }</td>
                                <td style="width: 100px;text-align: right">${ el.CantF }</td>
                                <td style="width: 100px;text-align: right">${ el.CantIF }</td>
                                <td style="width: 100px;text-align: right">${ el.CantGran }</td>
                                <td style="width: 100px;text-align: right">${ el.CantPint }</td>
                                <td style="width: 100px;text-align: right">${ el.CantEFG }</td>
                                <td style="width: 100px;text-align: right">${ el.CantIG }</td>
                                <td style="width: 100px;text-align: right">${ el.CantEGA }</td>
                                <td style="width: 100px;text-align: right">${ el.CantAKit }</td>
                                <td style="width: 100px;text-align: right">${ el.CantIAKit }</td>
                                <td style="width: 100px;text-align: right">${ el.Despacho }</th>
                            </tr>`;
                    load_tree.append(html_tarea)
                }

                for (let i = (data.length - 1); i < data.length; i++) {
                    let el = data[i];
                    let html_tarea = `<tr class="tree-${ el.id_tarea}">
                                <td style="width:103px;"></td>
                                <td style="width:99px;font-size: 15px;text-align: right"><strong>${ el.descripcion }</strong></td>
                                <td style="width:100px;text-align: right">${ el.CantEtapa }</td>
                                <td style="width:100px;text-align: right">${ el.CantZona }</td>
                                <td style="width:99px;font-size: 15px;text-align: right"><strong>${ el.TotalF }</strong></td>
                                <td style="width:99px;font-size: 15px;text-align: right"><strong>${ el.ProgramaF }</strong></td>
                                <td style="width:99px;font-size: 15px;text-align: right"><strong>${ el.CantF }</strong></td>
                                <td style="width:99px;font-size: 15px;text-align: right"><strong>${ el.CantIF }</strong></td>
                                <td style="width:99px;font-size: 15px;text-align: right"><strong>${ el.CantGran }</strong></td>
                                <td style="width:99px;font-size: 15px;text-align: right"><strong>${ el.CantPint }</strong></td>
                                <td style="width:100px;font-size: 15px;text-align: right"><strong>${ el.CantEFG }</strong></td>
                                <td style="width:100px;font-size: 15px;text-align: right"><strong>${ el.CantIG }</strong></td>
                                <td style="width:100px;font-size: 15px;text-align: right"><strong>${ el.CantEGA }</strong></td>
                                <td style="width:100px;font-size: 15px;text-align: right"><strong>${ el.CantAKit }</strong></td>
                                <td style="width:100px;font-size: 15px;text-align: right"><strong>${ el.CantIAKit }</strong></td>
                                <td style="width:100px;font-size: 15px;text-align: right"><strong>${ el.Despacho }</strong></td>
                            </tr>`;
                    load_tree.append(html_tarea)
                }
            }
            loading.hide();
        }).fail(function (data) {
            swal("Oops", "Se ha producido un error al cargar las Tarea", "error");
            loading.hide();
        });
    });

    load_tree.on('click',".prjBlockTree .openDetail", function () {
        $("[id*='tree-jonap']").remove();
        _thisContent = $(this).parent();
        _thisElement = $(this).parent();

        _thisElement.find('.fa-plus').addClass('fa-minus').removeClass('fa-plus');

        if(_thisContent.hasClass('open')){
            $('.prjBlockTree').removeClass('open');
            _thisElement.find('.fa-minus').addClass('fa-plus').removeClass('fa-minus');
            return;
        }
        //let _ot = select_ot.val();
        _thisElement.find('.fa-refresh').removeClass('hidden');
        $('.prjBlockTree').removeClass('open');
        _thisContent.addClass('open');

        let _ot = _thisContent.data("id");
        let _zone = $("#select-zona option:selected").attr("data-text");
        let _unit = select_unidad.val();
        let _etapa = select_etapa.val();
        let _tipoelemento = select_tipoelemento.val();
        if (_ot === "-1") {
            swal("Seleccione OT", "", "warning");
            return false;
        }

        select_ot.val(String(_ot));
        select_ot.trigger('change');

        const _parameter = {
            'proyecto_id': _ot,
            'zona_id': _zone,
            'unidad_id': _unit,
            'etapa_id': _etapa,
            'tipoelemento_id': _tipoelemento
        };
        $.get(URL_TAREA, _parameter, function (data) {
            _thisElement.find('.fa-refresh').addClass('hidden');
        }).done(function (data) {
            if (data[0] === undefined) {
                //load_tree.empty();
                let html_tarea = `<tr style="background-color: rgba(0, 208, 255, 0.25)">
                            <td colspan="15" style="text-align: center">No hay Registros</td>
                        </tr>`;
                _thisContent.after(html_tarea);

            } else {
                //swal("procesado", "Se ha cargado la informacion", "success");
                //load_tree.empty();
                $(".tree-jonap").remove();

                for (let i = (data.length - 1); i < data.length; i++) {
                    let el = data[i];
                    $(".wResultsStore").remove();
                    _thisContent.find("td:nth-child(5)").html(el.TotalF);
                    _thisContent.find("td:nth-child(6)").html(el.ProgramaF);
                    _thisContent.find("td:nth-child(7)").html(el.CantF);
                    _thisContent.find("td:nth-child(8)").html(el.CantIF);
                    _thisContent.find("td:nth-child(9)").html(el.CantGran);
                    _thisContent.find("td:nth-child(10)").html(el.CantPint);
                    _thisContent.find("td:nth-child(11)").html(el.CantEFG);
                    _thisContent.find("td:nth-child(12)").html(el.CantIG);
                    _thisContent.find("td:nth-child(13)").html(el.CantEGA);
                    _thisContent.find("td:nth-child(14)").html(el.CantAKit);
                    _thisContent.find("td:nth-child(15)").html(el.CantIAKit);
                    _thisContent.find("td:nth-child(16)").html(el.Despacho);
                }
                for (let i = (data.length - 2); i >= 0; i--) {
                    let el = data[i];
                    let html_tarea = `<tr id="tree-jonap-${ el.id_tarea}" data-id=${ el.id_tarea} data-open="false" class="tree-jonap tree-${ el.id_tarea}" style="background-color: rgba(0, 208, 255, 0.25)">
                                <td class="fa-hover" style="width:99px;">
                                    <a href="javascript:void(0)">
                                        <i class="fa fa-plus" aria-hidden="true"></i> Tarea
                                        <i class="fa fa-refresh fa-spin fa-fw hidden"></i>
                                    </a>
                                </td>
                                <td style="width: 100px;text-align: center">${ el.descripcion }</td>
                                <td style="width:100px;text-align: center">${ el.CantEtapa }</td>
                                <td style="width:100px;text-align: center">${ el.CantZona }</td>
                                <td style="width: 100px;text-align: center">${ el.TotalF }</td>
                                <td style="width: 100px;text-align: center">${ el.ProgramaF }</td>
                                <td style="width: 100px;text-align: right">${ el.CantF }</td>
                                <td style="width: 100px;text-align: right">${ el.CantIF }</td>
                                <td style="width: 100px;text-align: right">${ el.CantGran }</td>
                                <td style="width: 100px;text-align: right">${ el.CantPint }</td>
                                <td style="width: 100px;text-align: right">${ el.CantEFG }</td>
                                <td style="width: 100px;text-align: right">${ el.CantIG }</td>
                                <td style="width: 100px;text-align: right">${ el.CantEGA }</td>
                                <td style="width: 100px;text-align: right">${ el.CantAKit }</td>
                                <td style="width: 100px;text-align: right">${ el.CantIAKit }</td>
                                <td style="width: 100px;text-align: right">${ el.Despacho }</th>
                            </tr>`;
                    _thisContent.after(html_tarea);
                }
            }
        }).fail(function (data) {
            swal("Oops", "Se ha producido un error al cargar las Tarea", "error");
            loading.hide();
        });
    });


    load_tree.on("click", ".tree-jonap a", function () {
        let _this = $(this).parent().parent();
        let class_open = _this.attr("data-open");
        let _data_id = _this.attr("data-id");
        let _zone = $("#select-zona option:selected").attr("data-text");
        let _etapa = $("#select-etapa option:selected").val();
        let _unit = select_unidad.val();
        let _tipoelemento = select_tipoelemento.val();

        const _parameter = {
            'tarea_id': _data_id,
            'zona_id': _zone,
            'unidad_id': _unit,
            'etapa_id': _etapa,
            'tipoelemento_id': _tipoelemento
        };
        if (class_open === "true") {
            $(".children-tree-jonap").each(function () {
                const data_parent = $(this).attr("data-parent");
                if (data_parent === _data_id) {
                    $(this).remove();
                    $("#tree-jonap-" + data_parent).attr("data-open", "false");
                    $("#tree-jonap-" + data_parent).find("td a i.fa-minus").removeAttr('class').attr("class", "fa fa-plus")
                }
            });
            load_tree.find('.children-children-tree-jonap').remove();

        } else {
            _this.find("td a i.fa-plus").removeAttr('class').attr("class", "fa fa-minus");
            _this.find("td a i.fa-refresh").removeClass("hidden");
            _this.attr("data-open", "true");
            $.get(URL_PAQUETE, _parameter, function (data) {
            }).done(function (data) {
                _this.find("td a i.fa-refresh").addClass("hidden");

                if (data[0] === undefined) {
                    const html_package = `<tr id="children-tree-jonap-${_data_id}" data-open="false" data-parent="${_data_id}"  class="children-tree-jonap" style="background-color: rgba(118, 214, 79, 0.309804)">
                            <td colspan="15" style="text-align: center">No hay Registros</td>
                        </tr>`;
                    $(".tree-" + _data_id).after(html_package);

                } else {

                    for (let i = 0; i < data.length; i++) {
                        let el = data[i];
                        let html_paquete = `<tr id="children-tree-jonap-${ el.id_paquete}" data-open="false" data-parent="${_data_id}" data-id=${ el.id_paquete} class="children-tree-jonap tree-${ el.id_paquete}" style="background-color: rgba(118, 214, 79, 0.309804)">
                                    <td nowrap class="fa-hover" style="width:150px; text-align:center">
                                        <a href="javascript:void(0)">
                                            <i class="fa fa-plus" aria-hidden="true"></i>
                                            <img src="/static/img/palet.png" style="width: 20px; height: 15px" />
                                            <i class="fa fa-refresh fa-spin fa-fw hidden"></i>
                                        </a>
                                    </td>
                                    <td nowrap class="view_package" data-id=${ el.id_paquete} style="width:100px;text-align: center;cursor: pointer">${ el.descripcion }</td>
                                    <td nowrap style="width:100px;text-align: center">${ el.CantEtapa }</td>
                                    <td nowrap style="width:100px;text-align: center">${ el.CantZona }</td>
                                    <td nowrap style="width:100px;text-align: center">${ el.TotalF }</td>
                                    <td nowrap style="width:100px;text-align: center">${ el.ProgramaF }</td>
                                    <td nowrap style="width:100px;text-align: right">${ el.CantF }</td>
                                    <td nowrap style="width:100px;text-align: right">${ el.CantIF }</td>
                                    <td nowrap style="width:100px;text-align: right">${ el.CantGran }</td>
                                    <td nowrap style="width:100px;text-align: right">${ el.CantPint }</td>
                                    <td nowrap style="width:100px;text-align: right">${ el.CantEFG }</td>
                                    <td nowrap style="width:100px;text-align: right">${ el.CantIG }</td>
                                    <td nowrap style="width:100px;text-align: right">${ el.CantEGA }</td>
                                    <td nowrap style="width:100px;text-align: right">${ el.CantAKit }</td>
                                    <td nowrap style="width:100px;text-align: right">${ el.CantIAKit }</td>
                                    <td nowrap style="width:100px;text-align: right">${ el.Despacho }</td>
                                </tr>`;
                        $(".tree-" + data[i].id_tarea).after(html_paquete);
                        $("#children-tree-jonap-" + data[i].id_paquete).hide().fadeIn()

                    }
                }
            })
        }
    });

    load_tree.on("click", ".children-tree-jonap a", function () {
        let _this = $(this).parent().parent();
        let class_open = _this.attr("data-open");
        let _data_id = _this.attr("data-id");
        let _zone = $("#select-zona option:selected").attr("data-text");
        let _unit = select_unidad.val();
        let _tipoelemento = select_tipoelemento.val();

        const _parameter = {
            'paquete_id': _data_id,
            'zona_id': _zone,
            'unidad_id': _unit,
            'tipoelemento_id': _tipoelemento
        };
        if (class_open === "true") {
            $(".children-children-tree-jonap").each(function () {
                const data_parent = $(this).attr("data-parent");
                if (data_parent === _data_id) {
                    $(this).remove();
                    $("#children-tree-jonap-" + data_parent).attr("data-open", "false");
                    $("#children-tree-jonap-" + data_parent).find("td a i.fa-minus").removeAttr('class').attr("class", "fa fa-plus")
                }
            });
        } else {
            _this.find("td a i.fa-plus").removeAttr('class').attr("class", "fa fa-minus");
            _this.find("td a i.fa-refresh").removeClass("hidden");
            _this.attr("data-open", "true");
            $.get(URL_ELEMENTO, _parameter, function (data) {
            }).done(function (data) {
                _this.find("td a i.fa-refresh").addClass("hidden");
                for (let i = 0; i < data.length; i++) {
                    let el = data[i];
                    let html_elemento = `<tr id="children-children-tree-jonap-${ el.id_elemento}-${ el.id_paquete}" data-parent="${_data_id}" data-id="${ el.id_elemento}-${ el.id_paquete}" class="children-children-tree-jonap tree-${ el.id_elemento}-${ el.id_paquete}" style="background-color: rgba(153, 255, 127, 0.16)">
                                <td style="width: 100px; text-align:center"><a href="javascript:void(0)"><img src="/static/img/tuerca.png" style="width: 20px; height: 20px" /></a></td>
                                <td class="view_element_pdf" data-tarea="${el.id_tarea}" data-paquete="${el.id_paquete}" data-code="${el.id_elemento2}" style="width:100px;text-align: center" ><span>${ el.id_elemento2 }</span> <i class="fa fa-file-pdf-o"></i></td>
                                <td style="width:100px;text-align: center">${ el.CantEtapa }</td>
                                <td style="width:100px;text-align: center">${ el.CantZona }</td>
                                <td style="width:100px;text-align: center">${ el.TotalF }</td>
                                <td style="width:100px;text-align: center">${ el.ProgramaF }</td>
                                <td style="width:100px;text-align: right">${ el.CantF }</td>
                                <td style="width:100px;text-align: right">${ el.CantIF }</td>
                                <td style="width:100px;text-align: right">${ el.CantGran }</td>
                                <td style="width:100px;text-align: right">${ el.CantPint }</td>
                                <td style="width:100px;text-align: right">${ el.CantEFG }</td>
                                <td style="width:100px;text-align: right">${ el.CantIG }</td>
                                <td style="width:100px;text-align: right">${ el.CantEGA }</td>
                                <td style="width:100px;text-align: right">${ el.CantAKit }</td>
                                <td style="width:100px;text-align: right">${ el.CantIAKit }</td>
                                <td style="width:100px;text-align: right">${ el.Despacho }</td>
                            </tr>`;
                    $("#children-tree-jonap-" + data[i].id_paquete).after(html_elemento);
                    $("#children-children-tree-jonap-" + data[i].id_elemento + "-" + data[i].id_paquete)
                }
            })
        }
    });

    load_tree.on("mouseenter", ".tree-jonap td, .children-tree-jonap td, .children-children-tree-jonap td", function () {
        $('.pure-table td:nth-child(' + ($(this).index() + 1) + ')').addClass('hover');
    });

    load_tree.on("mouseleave", ".tree-jonap td, .children-tree-jonap td, .children-children-tree-jonap td", function () {
        $('.pure-table td:nth-child(' + ($(this).index() + 1) + ')').removeClass('hover');
    });


    input_filter_tarea.on("keyup", function () {
        load_tree.find('.children-children-tree-jonap').remove();
        $(".children-tree-jonap").each(function () {
            $(this).attr("data-open", "false");
            $(this).find("td a i.fa-minus").removeAttr('class').attr("class", "fa fa-plus");
        });

        let rex = new RegExp(input_filter_tarea.val(), 'i');
        const rows = $('.searchable').find('tr.children-tree-jonap');
        const rows_find_td = rows.find("td:eq(1)");
        rows.hide();
        rows_find_td.filter(function () {
            let tester;
            tester = rex.test($(this).text());
            return tester;
        }).parent().show();
    });

    input_filter_etapa.on("keyup", function () {
        load_tree.find('.children-children-tree-jonap').remove();
        $(".children-tree-jonap").each(function () {
            $(this).attr("data-open", "false");
            $(this).find("td a i.fa-minus").removeAttr('class').attr("class", "fa fa-plus");
        });

        let rex = new RegExp(input_filter_etapa.val(), 'i');
        const rows = $('.searchable').find('tr.children-tree-jonap');
        const rows_find_td = rows.find("td:eq(2)");
        rows.hide();
        rows_find_td.filter(function () {
            let tester;
            tester = rex.test($(this).text());
            return tester;
        }).parent().show();
    });


    load_tree.on("click", ".view_package", function (event) {
        event.preventDefault();
        const _data_id = $(this).attr("data-id");
        const _parameter = {
            'paquete_id': _data_id,
        };
        $.get(URL_PAQUETE_VIEW, _parameter, function (data) {
        }).done(function (data) {
            modal_paquete.find("#print_element").attr("data-id", _data_id);
            modal_paquete.find("#text-codigo-paquete").text("PAQUETE: " + data[0].paquete);
            modal_paquete.find("#text-contratista").text(data[0].contratista);
            modal_paquete.find("#text-etapa").text(data[0].etapa);
            modal_paquete.find("#text-armador").text(data[0].armador);
            modal_paquete.find("#text-ot").text(data[0].ot);
            modal_paquete.find("#text-prioridad").text(data[0].contratista);
            modal_paquete.find("#text-tarea").text(data[0].tarea);
            modal_paquete.find("#text-paquete").text(data[0].paquete);
            modal_paquete.find("#text-cantidad-elemento").text(data[0].cantidad_elemento);
            modal_paquete.find("#text-peso-total").text(data[0].peso_total);
            modal_paquete.find("#text-fecha-inicio").text(data[0].fecha_inicio);
            modal_paquete.find("#text-fecha-termino").text(data[0].fecha_termino);
            modal_paquete.find("#text-costo-kilo").text(data[0].costo_kilo);
            modal_paquete.find("#text-total").text(data[0].total);
            modal_paquete.find("#text-tarea-costo-kilo").text(data[0].dict_tarea.tarea_costo_kilo);
            modal_paquete.find("#text-tarea-total").text(data[0].dict_tarea.tarea_total);
            modal_paquete.find("#text-pre-tarea-costo-kilo").text(data[0].dict_paquete.pre_tarea_costo_kilo);
            modal_paquete.find("#text-pre-tarea-total").text(data[0].dict_paquete.pre_tarea_total);

            let list_element = data[0].lista_elementos;
            $("#tbody-modal-list-paquete").empty();
            $.each(list_element, function (index, value) {
                const counter = index + 1;
                let html_tbody = `
                        <tr>
                            <td><strong>${counter} .-</strong></td>
                            <td>${value.elemento}</td>
                            <td>${value.marca}</td>
                            <td>${value.cantidad}</td>
                            <td>${value.peso}</td>
                            <td>${value.etapa}</td>
                        </tr>`;
                $("#tbody-modal-list-paquete").append(html_tbody)
            });
            modal_paquete.modal({backdrop: 'static', keyboard: false});

        });
        return false;
    });

    load_tree.on("click", ".view_element_pdf", function (e) {
        e.preventDefault();
        let code = $(this).find('span').text();
        let ot = $("#select-ot>option:selected").text();
        let tr_parent = $(this).parent().attr("data-parent");
        let tr_children_tree = $("#children-tree-jonap-"+tr_parent);
        let tr_tree = $("#tree-jonap-"+tr_children_tree.attr("data-parent"));
        let code_tarea = tr_tree.find("td:eq(1)").text();
        let code_zona = tr_children_tree.find("td:eq(3)").text();

        $.ajax({
             url: URL_SEARCH_PDF,
             type: 'get',
             data: {
                 "ot": ot,
                 "code" : code,
                 "code_tarea": code_tarea,
                 "code_zona": code_zona
             },
             success : function(data){
                 if(data.error){
                     show_notify([data.error])
                 }else{
                     var pdf_link;
                     if(data.url){
                         pdf_link = data.url;
                     }else{
                         pdf_link = URL_PDF_NO_EXITS
                     }

                     const iframe =
                         '<iframe id="iframepdf" src="' + pdf_link + '" width="100%" height="500">' +
                         '<object type="application/pdf" data="' + pdf_link + '" width="100%" height="500">No Support</object>'+
                         '</iframe>';

                     $.createModal({
                        title: 'PDF',
                        message: iframe,
                        closeButton: true,
                        scrollable: false
                    });
                 }
             }
          });
        /*
        let pdf_link = URL_SERVER + '/static/js/test_print/' + code + '.PDF';
        const _file_exist = fileExists(pdf_link);
        if (_file_exist === false) {
            pdf_link = URL_SERVER + '/static/img/pdf_default.pdf';
        }
        const iframe = '<object type="application/pdf" data="' + pdf_link + '" width="100%" height="500">No Support</object>';
        $.createModal({
            title: 'PDF',
            message: iframe,
            closeButton: true,
            scrollable: false
        });
        return false;
        */
    });


});
