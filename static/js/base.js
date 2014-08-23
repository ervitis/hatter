$(function(){
    $(window).resize(function(event){
        var $this = $(this);

        compruebaWidthVentana($this);
    });

    $(window).ready(function(){
        var $this = $(this);

        compruebaWidthVentana($this);
    });

    var compruebaWidthVentana = function(elemento) {
        var WIDTH = 499;

        if (elemento.width() <= WIDTH) {
            $('.nombreLink').hide();
        } else {
            $('.nombreLink').show('normal');
        }
    };
});
