// Using BFS, create a graph, and find the sortest path

var FindSortestPath = (function(matrix) {
	var r, c;
	var graph = [];
	var h = matrix.length, w = matrix[0].length;

	for (r = 0; r < h; r++) {
		for (c = 0; c < w; c++) {
			var graphPos = w * r + c;

			if (matrix[r][c] === 1) {
				continue;
			}

			var connectedNodes = [];

			if (r > 1 && matrix[r-1][c] == 0) {
				connectedNodes.push((w*(r-1)) + c)
			}
			if (r < h-1 && matrix[r+1][c] == 0) {
				connectedNodes.push((w*(r+1)) + c)
			}
			if (c > 1 && matrix[r][c-1] == 0) {
				connectedNodes.push(w*r + (c - 1))
			}
			if (c < w-1 && matrix[r][c+1] == 0) {
				connectedNodes.push(w*r + (c + 1))
			}

			graph[graphPos] = connectedNodes
		}
	}

	console.log(graph);

	return {
		getSortestPath: function() {
			var distances = {};
			var i = 0;
			var queue = [[0, 0]];
			var distances = {};

			while (queue.length > 0) {
				var elem = queue.pop(0);
				console.log("Iter", elem);
				var nextToVisit = graph[elem[0]]

				for (i = 0; i < nextToVisit.length; i++) {
					console.log("Elem:", elem[0]);
					if (distances[nextToVisit[i]] === undefined || distances[nextToVisit[i]] > elem[1]+1) {
						distances[nextToVisit[i]] = elem[1]+1;
						console.log("IN", distances);
						queue.push([nextToVisit[i], elem[1]+1]);
					}
				}
			}

			console.log(distances);
			if (distances[graph.length-1] === undefined) {
				return false;
			}

			return distances[graph.length-1];
		}
	};
});

matrix = [
	[0, 1, 0, 0, 0, 0],
	[0, 1, 0, 0, 0, 0],
	[0, 0, 0, 1, 1, 0],
	[0, 1, 1, 1, 0, 0],
	[0, 1, 0, 0, 0, 0],
	[0, 1, 0, 0, 0, 0]
]

sp = FindSortestPath(matrix)
console.log(sp.getSortestPath());
