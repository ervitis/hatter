$(function(){

    var $agenda;
    var $agendas;

    $(window).load(function(){
        $agendas = new ArrayCollection();
    });

    $(document).on('click', '#bSearch', function(){

        var url = $('#hListado').val();

        var params = {
            'sDni': $.trim($('#sDni').val()),
            'sName': $.trim($('#sName').val())
        };

        $.post(url, params, function(response){
            for(var i in response) {
                $agenda = new Agenda(response[i]);
                $agendas._add_element($agenda);
            }
        });

        url = $('#hListadoTurno').val();

        $.post(url, params, function(response){
            console.log(response);
        });
    });

    function create_table_turnos() {

    }
});
