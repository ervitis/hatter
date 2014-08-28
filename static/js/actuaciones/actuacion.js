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

/**
 * Reset require property of address
 *
 * @private
 */
Actuacion.prototype._reset_required_address = function() {
    this.$tipo_via.prop('required', false);
    this.$direccion.prop('required', false);
    this.$direccion.prop('required', false);
    this.$codigo_postal.prop('required', false);
    this.$provincia.prop('required', false);
}

/**
 * Reset require property of coordinates
 * @private
 */
Actuacion.prototype._reset_required_coordinates = function() {
    this.$latitud.prop('required', false);
    this.$longitud.prop('required', false);
}

/**
 * Reset require property of placement
 *
 * @private
 */
Actuacion.prototype._reset_required_placement = function() {
    this.$emplazamiento.prop('required', false);
}

/**
 * Set require property
 *
 * @param elemento
 * @private
 */
Actuacion.prototype._set_required = function (elemento) {
    if ('direccion' === elemento) {
        this.$tipo_via.prop('required', true);
        this.$direccion.prop('required', true);
        this.$codigo_postal.prop('required', true);
        this.$provincia.prop('required', true);

        this._reset_required_coordinates();
        this._reset_required_placement();
    } else if ('coordenadas' === elemento) {
        this.$latitud.prop('required', true);
        this.$longitud.prop('required', true);

        this._reset_required_address();
        this._reset_required_placement();
    } else {
        this.$emplazamiento.prop('required', true);

        this._reset_required_address();
        this._reset_required_coordinates();
    }
}

/**
 * Return which element should be shown in the form
 *
 * @returns {string}
 * @private
 */
Actuacion.prototype._show_element_address = function() {
    if (this._has_address()) {
        return 'direccion';
    } else if (this._has_coordinates()) {
        return 'coordenadas';
    } else if (this._has_placement()) {
        return 'emplazamiento';
    } else {
        return 'nuevo';
    }
}

/**
 *
 * @returns {boolean}
 * @private
 */
Actuacion.prototype._has_name = function() {
    return '' !== this.$nombre.val() ? true : false;
}

/**
 *
 * @returns {boolean}
 * @private
 */
Actuacion.prototype._has_placement = function() {
    return '' !== this.$emplazamiento.val() ? true : false;
}

/**
 *
 * @returns {boolean}
 * @private
 */
Actuacion.prototype._has_coordinates = function() {
    return ('' !== this.$latitud.val() && '' !== this.$longitud.val()) ? true : false;
}

/**
 *
 * @returns {boolean}
 * @private
 */
Actuacion.prototype._has_address = function() {
    return ('' !== this.$direccion.val() && '' !== this.$provincia.val() && '' !== this.$codigo_postal.val()) ? true : false;
}
