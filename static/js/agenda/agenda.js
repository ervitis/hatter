/**
 *
 * @constructor
 */
var Agenda = function(elements) {
    if (typeof elements !== 'undefined') {
        this.$actuacion = elements.actuacion_id;
        this.$estado = elements.estado_id;
        this.$hora_fin = elements.hora_fin || null;
        this.$hora_inicio = elements.hora_inicio;
        this.$tecnico = elements.tecnico_id;
        this.$nombre = elements.tecnico_nom_ape;
    } else {
        this.$actuacion = '';
        this.$estado = '';
        this.$hora_fin = '';
        this.$hora_inicio = '';
        this.$tecnico = '';
        this.$nombre = '';
    }
};

/**
 * setter nombre
 * @param nombre
 * @private
 */
Agenda.prototype._set_nombre = function(nombre) {
    this.$nombre = nombre;
}

/**
 * setter eventos
 * @param eventos
 * @private
 */
Agenda.prototype._set_eventos = function(eventos) {
    this.$eventos = eventos;
}

/**
 * getter nombre
 * @returns {*}
 * @private
 */
Agenda.prototype._get_nombre = function() {
    return this.$nombre;
}

/**
 * getter eventos
 * @returns {Evento|*}
 * @private
 */
Agenda.prototype._get_eventos = function() {
    return this.$eventos;
}

/**
 * draw table
 * @param nElementos
 * @returns {string}
 * @private
 */
Agenda.prototype._draw_table = function(nElementos) {
    var html = '<table class="table">';
    for (var i = 0; i<nElementos;i++) {
        html += '<tr>';
        for (var j = 0; j < 20; j++) {
            html += '<td>' + i + '' + j + '</td>';
        }
        html += '</tr>';
    }
    html += '</table>';

    return html;
}

/**
 * getter estado
 * @param evento
 * @returns {*}
 * @private
 */
Agenda.prototype._get_estado_evento = function(evento) {
    return evento.estado.nombre;
}

/**
 * setter tecnico
 * @param tecnico
 * @private
 */
Agenda.prototype._set_tecnico = function(tecnico) {
    this.$tecnico = tecnico;
}

/**
 * getter tecnico
 * @returns {*}
 * @private
 */
Agenda.prototype._get_tecnico = function() {
    return this.$tecnico;
}

/**
 * setter actuacion
 * @param actuacion
 * @private
 */
Agenda.prototype._set_actuacion = function(actuacion) {
    this.$actuacion = actuacion;
}

/**
 * getter actuacion
 * @returns {*}
 * @private
 */
Agenda.prototype._get_actuacion = function() {
    return this.$actuacion;
}

Agenda.prototype = new ArrayCollection;

Agenda.prototype._search_element = function(key, element) {

}
