/**
 * Evento
 * @param arrEvento ['id', 'hora_inicio', 'hora_fin', 'estado']
 * @constructor
 */
var Evento = function(arrEvento) {
    this.$evento_id = arrEvento[0];
    this.$hora_inicio = arrEvento[1];
    this.$hora_fin = arrEvento[2];
    this.$estado = arrEvento[3];
}

/**
 * setter id
 * @param id
 * @private
 */
Evento.prototype._set_evento_id = function(id) {
    this.$evento_id = id;
}


/**
 * setter hora_inicio
 * @param hora
 * @private
 */
Evento.prototype._set_hora_inicio = function(hora) {
    this.$hora_inicio = hora;
}

/**
 * setter hora_fin
 * @param hora
 * @private
 */
Evento.prototype._set_hora_fin = function(hora) {
    this.$hora_fin = hora;
}

/**
 * setter estado
 * @param estado
 * @private
 */
Evento.prototype._set_estado = function(estado) {
    this.$estado = estado;
}

/**
 * getter id
 * @returns {*}
 * @private
 */
Evento.prototype._get_evento_id = function() {
    return this.$evento_id;
}

/**
 * getter hora_inicio
 * @returns {*}
 * @private
 */
Evento.prototype._get_hora_inicio = function() {
    return this.$hora_inicio;
}

/**
 * getter hora_fin
 * @returns {*}
 * @private
 */
Evento.prototype._get_hora_fin = function() {
    return this.$hora_fin;
}

/**
 * getter estado
 * @returns {*}
 * @private
 */
Evento.prototype._get_estado = function() {
    return this.$estado;
}
