var NumbersManager = (function () {
    var my = {};
    
    my.searchTwoSum = function (numList, sumTo) {
        var usedNumbers = {};
        var numListLen = numList.length, i = 0;
        
        for (i = 0; i < numListLen; i++) {
            if (usedNumbers[sumTo - numList[i]]) {
                return [sumTo - numList[i], numList[i]];
            }
            
            usedNumbers[numList[i]] = true;
        }
        
        return false;
    };
    
    return my;
})();

console.log(NumbersManager.searchTwoSum([3, 4, 5, 6, 1, 3, 0, 9, 2], 10));
