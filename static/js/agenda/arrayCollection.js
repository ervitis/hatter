
/**
 *
 * @constructor
 */
var ArrayCollection = function() {
    this.$element = [];
    this.$count = 0;
}

ArrayCollection.prototype._add_element = function(element) {
    this.$element.push(element);
    ++ this.$count;
}

ArrayCollection.prototype._remove_element = function(element) {
    var i = 0;
    for (i in this.$element) {
        if (this.$element[i] == element) {
            this.$element[i].pop();
            -- this.$count;

            return;
        }
    }
}

ArrayCollection.prototype._get_total_elements = function() {
    return this.$count;
}

ArrayCollection.prototype._get_item_by_key = function(key) {
    return this.$element[key];
}

ArrayCollection.prototype._is_empty = function() {
    return this.$count === 0;
}

ArrayCollection.prototype._search_element = function(object, key, element) {
    var obj = object;
    var obj_keys = this._get_keys(obj);

    key = (obj_keys[0].indexOf('$') !== -1) ? '$' + key : key;

    for (var i=0; i<this.$count; i++) {
        for (var j=0;j<obj_keys.length;j++) {
            if (obj_keys[j] == key) {
                var $obj = this.$element[i];

                if ($obj[key] === element) {
                    return this.$element[i];
                }
            }
        }
    }

    return false;
}

ArrayCollection.prototype._get_keys = function(element) {
    return Object.keys(element);
}
