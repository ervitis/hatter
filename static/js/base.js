$(function(){
    /**
     * keypress event only numbers
     */
    $('.only-numbers').keypress(function(event) {
        var key = event.keyCode || event.which;

        return (37 === key || 39 === key || 9 === key || 8 === key || (key >= 48 && key <= 57));
    });

    /**
     * keypress event only delete
     */
    $('.only-delete').keypress(function(event) {
        var key = event.keyCode || event.which;

        return (8 === key);
    });

    $('.mouse-pointer').mouseover(function() {
        $(this).css({
            'cursor': 'pointer'
        })
    });

    $(document).on('click', '.datetimepicker-input', function(event) {
        $(this).val('');
        event.preventDefault();

    });

    $('.datetimepicker-input').datetimepicker({
        'language': 'es-ES',
        'format': 'DD/MM/YYYY',
        'pickTime': false
    });
});
