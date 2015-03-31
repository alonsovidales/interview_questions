// Add two strings as integers without cast them

var IntegersHandler = (function() {
    var my = {};
    var zeroCode = "0".charCodeAt(0);
    
    my.addStrings = function(str1, str2) {
        var i = 0, result = 0;
        var str1Len = str1.length, str2Len = str2.length;
        
        for (i = 0; i < str1Len && i < str2Len; i++) {
            result += (str1[str1Len-1-i].charCodeAt(0) - zeroCode + str2[str2Len-1-i].charCodeAt(0) - zeroCode) * Math.pow(10, i)
        }
        
        if (i === str1Len) {
            for (; i < str2Len; i++) {
                result += (str2[str2Len-1-i].charCodeAt(0) - zeroCode) * Math.pow(10, i)
            }
        } else {
            for (; i < str1Len; i++) {
                result += (str1[str1Len-1-i].charCodeAt(0) - zeroCode) * Math.pow(10, i)
            }
        }
        
        return result;
    };
    
    return my;
})();

console.log(IntegersHandler.addStrings("123", "234664"));
