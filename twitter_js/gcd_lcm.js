// Eucledian algorithm
var DivTools = (function () {
	return {
		gcd: function (n, m) {
			var a;
			while (m !== 0) {
				a = m;
				m = n % m;
				n = a;
			}

			return n
		},
		lcm: function (n, m) {
			return n * m / this.gcd(n, m)
		},
	}
}) ();

DivTools.lcm(10, 5);
