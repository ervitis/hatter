$(function(){
    var $arrDireccion = {
        'direccion': 'direccion',
        'coordenadas': 'coordenadas',
        'emplazamiento': 'emplazamiento'
    };
    var $previous;
    var $actuacion;

    $(window).ready(function(){
        $actuacion = new Actuacion();

        if (! $actuacion._has_name()) {
            $previous = $arrDireccion[$('input[name="dir"]:checked').val()];
            $actuacion._set_required($previous);
        } else {
            $previous = $actuacion._show_element_address();
            $actuacion._set_required($previous);

            $('#direccion').prop('checked', false);
            $('#' + $previous).prop('checked', true);
            $('.direccion').addClass('hidden');
            $('.' + $previous).removeClass('hidden');
        }
    });

    $(document).on('change', '.radDireccion', function() {
        var $this = $(this);

        $actuacion._set_required($this.val());

        if ('coordenadas' === $this.val()) {
            $actuacion._reset_required_address();
            $actuacion._reset_required_placement();

            $('.' + $previous).addClass('hidden');
            $('.' + $this.val()).removeClass('hidden');
        } else if ('emplazamiento' === $this.val()) {
            $actuacion._reset_required_address();
            $actuacion._reset_required_coordinates();

            $('.' + $previous).addClass('hidden');
            $('.' + $this.val()).removeClass('hidden');
        } else {
            $actuacion._reset_required_coordinates();
            $actuacion._reset_required_placement();

            $('.' + $previous).addClass('hidden');
            $('.' + $this.val()).removeClass('hidden');
        }

        $previous = $arrDireccion[$this.val()];
    });

    $(document).on('mouseover', '#id_fecha', function(){
        $(this).css({
            'cursor': 'pointer'
        });
    });

    $(document).on('click', '#id_fecha', function(event){
        $(this).val('');
        event.preventDefault();
    });

    $('#id_fecha').datetimepicker({
        'language': 'es-ES',
        'format': 'DD/MM/YYYY HH:mm:ss',
        'pickTime': true
    });
});
