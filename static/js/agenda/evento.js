/**
 *
 * @param arrEvento ['id', 'hora_inicio', 'hora_fin', 'estado']
 * @constructor
 */
var Evento = function(arrEvento) {
    this.$evento_id = arrEvento[0];
    this.$hora_inicio = arrEvento[1];
    this.$hora_fin = arrEvento[2];
    this.$estado = arrEvento[3];
}

Evento.prototype._set_evento_id = function(id) {
    this.$evento_id = id;
}

Evento.prototype._set_hora_inicio = function(hora) {
    this.$hora_inicio = hora;
}

Evento.prototype._set_hora_fin = function(hora) {
    this.$hora_fin = hora;
}

Evento.prototype._set_estado = function(estado) {
    this.$estado = estado;
}

Evento.prototype._get_evento_id = function() {
    return this.$evento_id;
}

Evento.prototype._get_hora_inicio = function() {
    return this.$hora_inicio;
}

Evento.prototype._get_hora_fin = function() {
    return this.$hora_fin;
}

Evento.prototype._get_estado = function() {
    return this.$estado;
}
