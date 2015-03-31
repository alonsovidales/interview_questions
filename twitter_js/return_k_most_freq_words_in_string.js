// Returning the k most frequent words in a string delimited by space.

var StringsManipulator = (function () {
    var my = {};
    
    var getSmallerInBuffItem = function(buffer, wordsCount) {
        var i = 0, smaller = Infinity, buffLen = buffer.length, pos = 0;
        
        for (i = 0; i < buffLen; i++) {
            if (wordsCount[buffer[i]] < smaller) {
                smaller = wordsCount[buffer[i]];
                pos = i;
            }
        }
        
        return pos;
    }
    
    my.kMostFreq = function(strWords, k) {
        var words = strWords.split(' ');
        var wordsLen = words.length, i = 0, buffLen = 0, smallInBuff = Infinity;
        var wordsCounter = {};
        var buffer = [];
        
        for (i = 0; i < wordsLen; i++) {
            wordsCounter[words[i]] = wordsCounter[words[i]] || 1;
        }
        
        for (word in wordsCounter) {
            if (buffer.length < k || wordsCounter[word] > smallInBuff) {
                buffer.push(word);
                
                buffLen = buffer.length;
                if (buffLen > k) {
                    buffer.splice(getSmallerInBuffItem(buffer, wordsCounter), 1);
                    smallInBuff = wordsCounter[getSmallerInBuffItem(buffer, wordsCounter)];
                }
            }
        }
        
        return buffer;
    };
    
    return my;
})();

console.log(StringsManipulator.kMostFreq("this is is a test is this a test here I'm testing this test", 2));
