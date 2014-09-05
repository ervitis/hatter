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

Agenda.prototype._set_nombre = function(nombre) {
    this.$nombre = nombre;
}

Agenda.prototype._set_eventos = function(eventos) {
    this.$eventos = eventos;
}

Agenda.prototype._get_nombre = function() {
    return this.$nombre;
}

Agenda.prototype._get_eventos = function() {
    return this.$eventos;
}

Agenda.prototype._add = function(key, item) {
    if (typeof this.$eventos[key] != 'undefined') {
        return undefined;
    }

    this.$eventos[key] = item;
    return ++this.$count;
}

Agenda.prototype._remove = function(key) {
    if (typeof this.$eventos[key] == 'undefined') {
        return undefined;
    }

    delete this.$eventos[key];
    return --this.$count;
}

Agenda.prototype._item = function(key) {
    return this.$eventos[key];
}

Agenda.prototype._get_n_elements = function() {
    return parseInt(this.$count);
}

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

Agenda.prototype._get_estado_evento = function(evento) {
    return evento.estado.nombre;
}
