var SearchTrie = (function(elems) {
    var trie = {};

    (function(elems) {
        var trieIter = {};
        var chars = [];
        var i = 0, ci = 0, len = elems.length, cLen = 0;

        for (i = 0; i < len; i++) {
            chars = elems[i].split('');
            cLen = chars.length;
            trieIter = trie;
            for (ci = 0; ci < cLen; ci++) {
                if (!trieIter[chars[ci]]) {
                    trieIter[chars[ci]] = {};

                }
                trieIter = trieIter[chars[ci]];
            }

            trieIter['elem'] = elems[i]
        }
    }) (elems);


    var getAllChilds = function(iterNode) {
        var queue = [iterNode];
        var elem = {};
        var result = [];

        while (queue.length > 0) {
            elem = queue.pop();
            for (child in elem) {
                if (child === 'elem') {
                    result.push(elem['elem']);
                } else {
                    queue.push(elem[child]);
                }
            }
        }

        return result;
    };

    return {
        getWithPrefix: function(pattern) {
            var trieIter = trie;
            var chars = pattern.split('');
            var charsLen = chars.length;
            var i = 0;

            for (i = 0; i < charsLen; i++) {
                if (!trieIter[chars[i]]) {
                    if (chars[i] == "*") {
                        return getAllChilds(trieIter);
                    }

                    return false;
                } else {
                    trieIter = trieIter[chars[i]];
                }
            }

            if (trieIter['elem']) {
                return trieIter['elem'];
            }

            return false;
        }
    };
});

var st = SearchTrie(["hello", "hell", "hellllloooooo", "home", "aux"]);
print(st.getWithPrefix("hell*"));
print(st.getWithPrefix("hello"));
print(st.getWithPrefix("h*"));
print(st.getWithPrefix("home*"));
