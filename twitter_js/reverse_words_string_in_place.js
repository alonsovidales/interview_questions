// Reverse the order of words of a sentence in place
var StringsHandler = (function () {
    var my = {};
    
    my.reverseWordsInPlace = function(inStr) {
        var strLen = inStr.length, wi = 0, i = 0, wordBegining = 0;
        var aux = "";
        
        for (i = 0; i < strLen / 2; i++) {
            aux = inStr[i];
            inStr[i] = inStr[strLen-1-i];
            inStr[strLen-1-i] = aux;
            //console.log(inStr[i], inStr[strLen-1-i]);
        }
        
        i = 0;
        while (i < strLen) {
            wordBegining = i;
            for (; i < strLen && inStr[i] !== ' '; i++);
            for (wi = 0; wi < ((i - wordBegining) / 2); wi++) {
                aux = inStr[wordBegining + wi];
                inStr[wordBegining + wi] = inStr[i-1-wi];
                inStr[i-1-wi] = aux;
            }
            i++;
        }
        
        return inStr;
    };
    
    return my;
})();

console.log(StringsHandler.reverseWordsInPlace("This is a test...".split('')).join(''));
//...tset a si sihT
//test... a is This
