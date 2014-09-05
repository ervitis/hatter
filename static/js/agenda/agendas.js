$(function(){

    var $agenda;

    $(document).on('click', '#bSearch', function(){

        var url = $('#hListado').val();

        var params = {
            'sDni': $.trim($('#sDni').val()),
            'sName': $.trim($('#sName').val())
        };

        $.post(url, params, function(response){
            console.log(response);
        });
    });

    function create_table() {
        var table = $agenda._draw_table($agenda._get_n_elements());
        $('#resultados').empty().html(table);
    }

    function populate_data(data) {
        for (var i in data) {
            $agenda._add(data[i].eventos, i);
        }

        console.log($agenda._get_eventos());
    }

});
