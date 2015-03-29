var ArrayManager = (function(elements) {
    return {
        getSize: function() {
            var i = 0, total = 0;
            var queue = [elements];

            while (queue.length > 0) {
                elems = queue.pop();
                if (typeof elems === typeof []) {
                    for (i = 0; i < elems.length; i++) {
                        queue.push(elems[i]);
                    }
                } else {
                    total++;
                }
            }

            return total;
        }
    };
});

am = ArrayManager([1, 2, [3, [4, 5], [4, 2, 1, 5]], [2, 3, [4, 5, [2, 3, 4, [5, [6, [2]]]], 6], 5]]);
print(am.getSize());
