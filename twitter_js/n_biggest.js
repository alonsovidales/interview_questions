var ArrayHandler = (function(numsList) {
	var list = numsList;

	return {
		getMinAtPos: function(pos) {
		     var buffer = [];
		     var i, bi;
		     var smallestInBuff = -1;

		     for (i = 0; i < list.length; i++) {
			     if (list[i] > smallestInBuff || buffer.length < pos) {
				     buffer.push(list[i]);
				     if (buffer.length > pos) {
					     buffer.splice(buffer.indexOf(smallestInBuff), 1);
				     }
				     smallestInBuff = Infinity;
				     for (bi = 0; bi < pos; bi++) {
					     if (smallestInBuff > buffer[bi]) {
						     smallestInBuff = buffer[bi];
					     }
				     }
			     }
		     }

		     return smallestInBuff;
		}
	};
});

ah = ArrayHandler([4, 5, 6, 1, 3, 7, 3, 4]);
ah.getMinAtPos(3);
