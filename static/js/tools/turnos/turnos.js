$(function(){
    $('.input-inicio').on('dp.change', function(e) {
        var $this = $(this);

        if ('' !== $this.val()) {
            var $tr = $this.closest('tr');
            var $fecha_fin = $tr.find('td:eq(3) input');

            if ('' !== $fecha_fin.val()) {
                validate_dates($this.val(), $fecha_fin.val());
            }
        }
    });

    $('.input-fin').on('dp.change', function(e) {
        var $this = $(this);

        if ('' !== $this.val()) {
            var $tr = $this.closest('tr');
            var $fecha_inicio = $tr.find('td:eq(2) input');

            if ('' !== $fecha_inicio.val()) {
                validate_dates($fecha_inicio.val(), $this.val());
            }
        }
    });

    $(document).on('change', '.chk-tecnico', function() {
        var $this = $(this);
        var $tr = $this.closest('tr');

        if ($this.is(':checked')) {
            $tr.find('td input').prop('required', true);
            $tr.find('td select').prop('required', true);
        } else {
            $tr.find('td input').prop('required', false);
            $tr.find('td select').prop('required', false);
        }
    });

    function validate_dates(since, end) {
        var s = parse_date_to_object(since);
        var e = parse_date_to_object(end);

        if (e <= s) {
            var message = 'La fecha fin no puede ser menor o igual a la fecha inicial del turno';

            display_error_message(message);
        } else {
            $('#aplica_turnos').prop('disabled', false);

            hide_message();
        }
    }

    function parse_date_to_object(date) {
        var f = date.split('/');

        return new Date(f[2], f[1], f[0]);
    }

    function display_error_message(message) {
        $('#aplica_turnos').prop('disabled', true);

        var $id = $('#error_messages');

        $id.empty().append(message).removeClass('hidden', function(){
            var $this = $(this);
            $this.slideDown('slow');
            $errorContador = setTimeout(function(){
                $this.slideUp('slow', function(){
                    $this.addClass('hidden');
                });
            }, 10000);
        });

    }

    function hide_message() {
        var $id = $('#error_messages');

        $id.slideUp('fast');
    }

});
