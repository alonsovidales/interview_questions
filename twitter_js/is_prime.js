// This is the Wilson's theorem: http://en.wikipedia.org/wiki/Wilson%27s_theorem

var Primes = (function () {
	var fact = function(x) {
		if (x <= 0) {
			return 1;
		}
		var fact = x, i;
		for (i = x-1; i > 0; i--) {
			fact *= i;
		}

		return fact;
	};

	return {
		wilsonFact: function (x) {
			return fact(x - 1) % x !== 0;
		}
	};
})();

console.log(Primes.wilsonFact(23));
