function Actuacion() {
    this.$nombre         = $('#id_nombre');
    this.$tipo_via       = $('#id_tipo_via');
    this.$direccion      = $('#id_direccion');
    this.$codigo_postal  = $('#id_codigo_postal');
    this.$provincia      = $('#id_provincia');
    this.$latitud        = $('#id_latitud');
    this.$longitud       = $('#id_longitud');
    this.$emplazamiento  = $('#id_emplazamiento');
    this.$cliente        = $('#id_cliente');
    this.$estado         = $('#id_estado');
    this.$prioridad      = $('#id_prioridad');
    this.$severidad      = $('#id_severidad');
    this.$alerta         = $('#id_alerta');
}

Actuacion.prototype._initialize_address = function() {
    this.$tipo_via.prop('required', false);
    this.$direccion.prop('required', false);
    this.$direccion.prop('required', false);
    this.$codigo_postal.prop('required', false);
    this.$provincia.prop('required', false);
}

Actuacion.prototype._initialize_coordinates = function() {
    this.$latitud.prop('required', false);
    this.$longitud.prop('required', false);
}

Actuacion.prototype._initialize_placement = function() {
    this.$emplazamiento.prop('required', false);
}

Actuacion.prototype._set_required = function (elemento) {
    if ('direccion' === elemento) {
        this.$tipo_via.prop('required', true);
        this.$direccion.prop('required', true);
        this.$codigo_postal.prop('required', true);
        this.$provincia.prop('required', true);

        this._initialize_coordinates();
        this._initialize_placement();
    } else if ('coordenadas' === elemento) {
        this.$latitud.prop('required', true);
        this.$longitud.prop('required', true);

        this._initialize_address();
        this._initialize_placement();
    } else {
        this.$emplazamiento.prop('required', true);

        this._initialize_address();
        this._initialize_coordinates();
    }
}
