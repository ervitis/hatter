/**
 *
 * @param arrAgenda ['nombre_tecnico', 'arrEventos']
 * @constructor
 */
var Agenda = function(arrAgenda) {
    this.$nombre = arrAgenda[0];
    this.$eventos = new Evento(arrAgenda[1]);
    this.$count = 0;
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
 * add eventos
 * @param key
 * @param item
 * @returns {*}
 * @private
 */
Agenda.prototype._add = function(key, item) {
    if (typeof this.$eventos[key] != 'undefined') {
        return undefined;
    }

    this.$eventos[key] = item;
    return ++this.$count;
}

/**
 * remove eventos
 * @param key
 * @returns {*}
 * @private
 */
Agenda.prototype._remove = function(key) {
    if (typeof this.$eventos[key] == 'undefined') {
        return undefined;
    }

    delete this.$eventos[key];
    return --this.$count;
}

/**
 * get item via key
 * @param key
 * @returns {*}
 * @private
 */
Agenda.prototype._item = function(key) {
    return this.$eventos[key];
}

/**
 * get count elements
 * @returns {Number}
 * @private
 */
Agenda.prototype._get_n_elements = function() {
    return parseInt(this.$count);
}

/**
 * draw table
 * @param nElementos
 * @returns {string}
 * @private
 */
Agenda.prototype._draw_table = function(nElementos) {
    var html = '<table>';
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
