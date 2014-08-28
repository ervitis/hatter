$(function(){
    $('.only-numbers').keypress(function(event) {
        var key = event.keyCode || event.which;

        return (37 === key || 39 === key || 9 === key || 8 === key || (key >= 48 && key <= 57)) ? true : false;
    });
});
