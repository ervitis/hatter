$(function(){
    var $mapa;
    var $datos;
    var $opcionesMapa = {
        zoom: 10,
        center: new google.maps.LatLng(40.4378271,-3.6795366)
    };

    $(window).load(function(){
        var url = $('#dataurl').val();

        $.get(url, function(response){
            $datos = response;

            if (0 === $datos.length || ! $datos) {
                $('#mapa').hide();

                $('#nodata').removeClass('hidden', function(){
                    var $this = $(this);
                    $errorContador = setTimeout(function(){
                        $this.slideUp('slow', function(){
                            $this.addClass('hidden');
                        });
                    }, 20000);
                });

                return false;
            }

            set_mapa($opcionesMapa);
        });
    });

    function set_mapa(opciones) {
        var mapaId = document.getElementById('mapa');
        $mapa = new google.maps.Map(mapaId, $opcionesMapa);
    }
});
