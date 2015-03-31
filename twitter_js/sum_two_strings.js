// Add two super large strings as integers without cast them

var IntegersHandler = (function() {
    var my = {};

    my.addStrings = function(str1, str2) {
        var i = 0, sumResultInt = 0;
        var result = "", sumResult = "";
        var carry = false;
        var str1Len = str1.length, str2Len = str2.length;

        for (i = 0; i < str1Len || i < str2Len; i++) {
            if (i >= str1Len) {
                sumResultInt = parseInt(str2[str2Len-1-i]);
            } else if (i >= str2Len) {
                sumResultInt = parseInt(str2[str1Len-1-i]);
            } else {
                console.log(i, parseInt(str1[str1Len-1-i]));
                sumResultInt = parseInt(str1[str1Len-1-i]) + parseInt(str2[str2Len-1-i]);
            }
            if (carry) {
                sumResultInt++;
            }
            sumResult = String(sumResultInt);
            result = sumResult[sumResult.length-1] + result;
            carry = sumResult.length === 2;
        }
        
        if (carry) {
            result = "1" + result;
        }

        return result;
    };
    
    return my;
})();

console.log(IntegersHandler.addStrings("123", "234664"));
