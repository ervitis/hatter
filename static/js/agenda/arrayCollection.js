
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
    for (var i in this.$element) {
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
