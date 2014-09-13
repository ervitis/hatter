$(function(){
    var $mapa;
    var $datos;
    var $opcionesMapa = {
        zoom: 6,
        center: new google.maps.LatLng(40.4378271,-3.6795366),
        disableDefaultUI: true,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };

    var $arrMarkers = [];
    var $tempDict;

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

            $mapa = set_mapa($opcionesMapa);

            set_markers($mapa, $datos);
        });
    });

    function set_mapa(opciones) {
        var mapaId = document.getElementById('mapa');
        return new google.maps.Map(mapaId, $opcionesMapa);
    }

    function set_markers(mapa, dict_elementos) {
        for (var i in dict_elementos) {
            if (dict_elementos[i].lat) {
                $arrMarkers.push(new google.maps.Marker({
                    position: convert_into_latlng(dict_elementos[i].lat, dict_elementos[i].lon),
                    map: mapa,
                    title: dict_elementos[i].nombre
                }));
            } else {
                //Google GEO
                $tempDict = dict_elementos[i];
                convert_from_address_to_latlng($tempDict.address);
            }
        }
    }

    function convert_into_latlng(lat, long) {
        return new google.maps.LatLng(lat, long);
    }

    function convert_from_address_to_latlng(direccion) {
        var geocoder = new google.maps.Geocoder();

        geocoder.geocode({
            'address': direccion
        }, results_geocoder);
    }

    function results_geocoder(results, status) {
        if (google.maps.GeocoderStatus.OK == status) {
            var lat = results[0].geometry.location.lat();
            var lng = results[0].geometry.location.lng();

            $arrMarkers.push(new google.maps.Marker({
                position: convert_into_latlng(lat, lng),
                map: $mapa,
                title: $tempDict.name
            }));
        } else {
            console.log('Error ' + status);
            return false;
        }
    }
});
