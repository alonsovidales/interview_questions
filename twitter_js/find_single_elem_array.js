var ArrayManager = (function(inArray) {
    var array = inArray;

    return {
        getSingleElement: function() {
            var i = 0, len = array.length;
            var elems = {};
            var keys = [];

            for (i = 0; i < len; i++) {
                if (elems[array[i]]) {
                    delete elems[array[i]];
                } else {
                    elems[array[i]] = true;
                }
            }

            keys = Object.keys(elems);
            if (keys.length !== 1) {
                return false
            }
            return keys[0];
        }
    }
});

am = ArrayManager([1, 1, 4, 2, 3, 5, 4, 2, 5]);
print(am.getSingleElement());
