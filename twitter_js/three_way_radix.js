var StringSorter = (function() {
    var my = {};

    my.sortThreeWayRadix = function(strings, pos) {
        var strLen = strings.length;
        var i = 0;
        var pivot = false;
        var left = [], center = [], right = [], result = [];

        pos = pos || 0;

        for (i = 0; i < strLen; i++) {
            if (pos < strings[i].length) {
                pivot = pivot || strings[i][pos];
                if (strings[i][pos] < pivot) {
                    left.push(strings[i]);
                } else if (strings[i][pos] > pivot) {
                    right.push(strings[i]);
                } else {
                    center.push(strings[i]);
                }
            } else {
                center.push(strings[i]);
            }
        }
        
        if (pivot === false) {
            return strings;
        }
        
        return this.sortThreeWayRadix(left, pos + 1).concat(
            this.sortThreeWayRadix(center, pos + 1)).concat(
                this.sortThreeWayRadix(right, pos + 1));
    };

    return my;
})();

console.log(StringSorter.sortThreeWayRadix(["hella", "hellu", "holla"]));
console.log(StringSorter.sortThreeWayRadix(["hellooo", "hellu", "hella", "hola", "house"]));
