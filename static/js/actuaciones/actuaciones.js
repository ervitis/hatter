$(function(){
    var $arrDireccion = {
        'direccion': 'direccion',
        'coordenadas': 'coordenadas',
        'emplazamiento': 'emplazamiento'
    };
    var $previous;
    var $actuacion;

    $(document).ready(function(){
        $actuacion = new Actuacion();

        $previous = $arrDireccion[$('input[name="dir"]:checked').val()];
        $actuacion._set_required($previous);
    });

    $(document).on('change', '.radDireccion', function() {
        var $this = $(this);

        $actuacion._set_required($this.val());

        if ('coordenadas' === $this.val()) {
            $actuacion._initialize_address();
            $actuacion._initialize_placement();

            $('.' + $previous).addClass('hidden');
            $('.' + $this.val()).removeClass('hidden');
        } else if ('emplazamiento' === $this.val()) {
            $actuacion._initialize_address();
            $actuacion._initialize_coordinates();

            $('.' + $previous).addClass('hidden');
            $('.' + $this.val()).removeClass('hidden');
        } else {
            $actuacion._initialize_coordinates();
            $actuacion._initialize_placement();

            $('.' + $previous).addClass('hidden');
            $('.' + $this.val()).removeClass('hidden');
        }

        $previous = $arrDireccion[$this.val()];
    });
});
