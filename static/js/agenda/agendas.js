$(function(){
    var $agendas;

    $(window).load(function(){
        $agendas = new ArrayCollection();
    });

    $(document).on('click', '#bSearch', function(){

        var url = $('#hListado').val();

        var params = {
            'sName': $.trim($('#sName').val())
        };

        $.post(url, params, function(response){
            console.log(response);

            $('#resultados').empty();
            if (response.length == 0) {
                $('#resultados').append('<p class="alert alert-info text-center">No hay turnos para los filtros escogidos</p>');
                return;
            }

            for(var i in response) {
                var $agenda = new Agenda(response[i]);
                $agendas._add_element($agenda);
            }

            get_turnos(params);
        });


    });

    function get_turnos(params) {
        var url = $('#hListadoTurno').val();

        $.post(url, params, function(response){
            create_data_turnos(response)
        });
    }

    function create_data_turnos(response) {
        var $arrAgendas = new ArrayCollection();

        var i = 0;
        for (i in response) {
            var $agenda = new Agenda();
            $agenda = $agendas._search_element($agenda, 'tecnico', response[i].tecnico_id);
            if (!$agenda) {
                console.log('Error');
                return;
            } else {
                $arrAgendas._add_element($agenda);
            }
        }

        draw_table($arrAgendas, response);

    }

    function draw_table(arrElements, turnos) {
        $results = $('#resultados');

        var hini0, hini1, hfin0, hfin1;

        var html = '<table id="tabla-agenda" class="table table-bordered">';
        html += '<thead><tr>';
        html += '<th class="cell-schedule-name">Nombre</th>';

        for(var i=0;i<24;i++) {
            var hora = (i<10) ? '0' + i : i;
            html += '<th class="active cell-schedule">' + hora + '</th>';
        }

        html += '</tr></thead>';
        html += '<tbody>';

        for (var i = 0; i < arrElements._get_total_elements(); i++) {
            var $agenda = arrElements._get_item_by_key(i);

            hini0 = parseInt(turnos[i].turno_inicio0.substr(0, 2));
            hfin0 = parseInt(turnos[i].turno_fin0.substr(0, 2));

            if (turnos[i].turno_inicio1) {
                hini1 = parseInt(turnos[i].turno_inicio1.substr(0, 2));
                hfin1 = parseInt(turnos[i].turno_fin1.substr(0, 2));
            } else {
                hini1 = -1;
                hfin1 = -1;
            }

            html += '<tr id="tec_' + $agenda.$tecnico + '">';

            for (var j = 0; j < 25; j++) {
                if (j === 0) {
                    html += '<td class="cell-schedule-name">' + $agenda.$nombre + '</td>';
                } else {
                    if (j >= hini0 && j <= hfin0 || (hini1 !== -1 && j >= hini1 && j <= hfin1)) {
                        html += '<td id="act_' + i + (j-1) + '" class="success cell-schedule"></td>';
                    } else {
                        html += '<td id="dis_' + i + (j-1) + '" class="cell-schedule"></td>';
                    }
                }
            }

            html += '</tr>';

        }
        html += '</tbody></table>';

        $results.append(html);

    }

    $(document).on('click', '.cell-schedule', function(e) {
        alert('has hecho click en la celda ' + $(this).attr('id'));
    });
});
