$(function(){
    var $agendas;

    $(window).load(function(){
        $agendas = new ArrayCollection();

        $('.draggable').draggable({
            revert: 'invalid'
        });
    });

    $(document).on('click', '#bSearch', function(){
        var url = $('#hListado').val();

        var params = {
            'sName': $.trim($('#sName').val())
        };

        $.post(url, params, function(response){
            $('#resultados').empty();
            var i = 0;
            for(i in response) {
                var $agenda = new Agenda(response[i]);

                $agendas._add_element($agenda);
            }

            get_turnos(params);
        });


    });

    function get_turnos(params) {
        var url = $('#hListadoTurno').val();

        $.post(url, params, function(response){
            if (response.length == 0) {
                $('#resultados').append('<p class="alert alert-info text-center">No hay turnos para los filtros escogidos</p>');
                return;
            }

            create_data_turnos(response)
        });
    }

    function create_data_turnos(response) {
        var $arrAgendas = new ArrayCollection();

        var i = 0;
        for (i in response) {
            var $agenda = new Agenda();
            
            if ($agendas._get_total_elements() === 0) {
                break;
            } else {
                $agenda = $agendas._search_element($agenda, 'tecnico', response[i].tecnico_id);
            }

            if ($agenda !== false) {
                $arrAgendas._add_element($agenda);
            }
        }

        draw_table($agendas, $arrAgendas, response);

        $('.droppable').droppable({
            accept: '.draggable',
            tolerance: 'pointer',
            drop: function(event, ui) {
                var params = {
                    'turno': parseInt(event.target.id.split('_')[1]),
                    'turno_hora': parseInt(event.target.id.split('_')[2]),
                    'tecnico': event.target.parentElement.attributes['id'].value.split('_')[1],
                    'actuacion': ui.draggable.attr('id').split('_')[1]
                };

                asigna_actuacion_tecnico(params);
            }
        });

        $('.ayuda').tooltip({
            container: 'body'
        });

    }

    function asigna_actuacion_tecnico(params) {
        var url = $('#resultados').attr('data-url');

        $.post(url, params, function(response) {
            if (response.ok) {
                alert('Se ha asignado la actuación al técnico');
                location.reload(true);
            } else {
                alert('Ha ocurrido un error en la asignación');
                console.log(response);
                return;
            }
        });
    }

    function draw_table(arrElements, arrAgendas, turnos) {
        $results = $('#resultados');

        var hini0, hini1, hfin0, hfin1;

        var html = '<table id="tabla-agenda" class="table table-bordered">';
        html += '<thead><tr>';
        html += '<th class="cell-schedule-name">Nombre</th>';

        for(var i=0;i<24;i++) {
            var hora = (i<10) ? '0' + i : i;
            html += '<th class="active cell-schedule-hour">' + hora + '</th>';
        }

        html += '</tr></thead>';
        html += '<tbody>';

        for (var i = 0; i < turnos.length; i++) {
            var $agenda = arrAgendas._get_item_by_key(i);
            var arrActuaciones = [];

            if (arrElements._get_total_elements() !== 0 && typeof $agenda != 'undefined') {
                arrActuaciones = arrElements._get_actuaciones_groupby_tecnico($agenda.$tecnico);
            }

            var turno0, turno1;

            if (turnos[i].turno_inicio0) {
                hini0 = parseInt(turnos[i].turno_inicio0.substr(0, 2)) + 1;
                hfin0 = parseInt(turnos[i].turno_fin0.substr(0, 2)) + 1;
                turno0 = turnos[i].turno_id0;

                if (turnos[i].turno_inicio1) {
                    hini1 = parseInt(turnos[i].turno_inicio1.substr(0, 2)) + 1;
                    hfin1 = parseInt(turnos[i].turno_fin1.substr(0, 2)) + 1;
                    turno1 = turnos[i].turno_id1;
                } else {
                    hini1 = -1;
                    hfin1 = -1;
                }
            } else {
                hini0 = -1;
                hini1 = -1;
            }

            html += '<tr id="tec_' + turnos[i].tecnico_id + '">';

            for (var j = 0; j < 25; j++) {
                if (j === 0) {
                    html += '<td class="cell-schedule-name">' + turnos[i].tecnico_nombre + '</td>';
                } else {
                    if (hini0 !== -1 && j >= hini0 && j <= hfin0 ||
                        (hini1 !== -1 && j >= hini1 && j <= hfin1)) {

                        var hasActuacion = false;

                        for (var k=0; k<arrActuaciones.length; k++) {
                            var hora_actuacion = parseInt(arrActuaciones[k].$hora_inicio);
                            if (hora_actuacion === j) {
                                html += '<td id="act_' + j + '" class="ayuda cell-schedule danger" data-toggle="tooltip" data-placement="top" title="' + arrActuaciones[k].$nombre_act + '"></td>';
                                hasActuacion = true;
                                break;
                            }
                        }

                        if (!hasActuacion) {
                            html += '<td id="tur_' + turno0 + '_' + j + '" class="droppable cell-schedule success"></td>';
                        }
                    } else {
                        html += '<td id="dis_' + j + '" class="cell-schedule"></td>';
                    }
                }
            }

            html += '</tr>';

        }

        html += '</tbody></table>';

        $results.append(html);
    }
});
