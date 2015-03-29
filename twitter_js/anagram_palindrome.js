var StringsAnalyzer = (function() {
	return {
		isAnagramOrPalindrome: function(str1, str2) {
		       if (str1.length !== str2.length) {
			       return [false, false];
		       }

		       var palindrome = true;
		       var strLen = str1.length;
		       var charsOnS1 = {};
		       var charsOnS2 = {};

		       for (var i = 0; i < strLen / 2; i++) {
			       if (str1[i] !== str2[strLen - 1 - i]) {
				       palindrome = false;
			       }
		       }

		       if (palindrome) {
			       return [true, true]
		       }
		       return [str1.split('').sort().join('') === str2.split('').sort().join(''), false];
	       }
	};
});

sa = StringsAnalyzer();
console.log(sa.isAnagramOrPalindrome("hello", "heoll"));
console.log(sa.isAnagramOrPalindrome("casa", "asac"));
