from collections import deque, defaultdict

def _create_graph(meetings):
    result = defaultdict(list)
    for meeting in meetings:
        key = '-'.join(map(str, meeting))
        for meeting_to in meetings:
            if meeting_to[0] >= meeting[1]:
                to_str = '-'.join(map(str, meeting_to))
                result[key].append(to_str)

    return result

def calc_best_meetings(meetings):
    graph = _create_graph(meetings)
    queue = deque([(graph.keys()[0], 0)])
    max_distance = 0
    visited = set()
    while len(queue) > 0:
        aux = queue.popleft()
        current = aux[0]
        dist = aux[1]
        if max_distance < dist:
                max_distance = dist
                
        for dest in graph[current]:
            new_node = (dest, dist+1)
            if new_node not in visited:
                visited.add(new_node)
                queue.append((dest, dist+1))

    return max_distance

def calc_min_rooms(meetings):
    rooms = []

    for meeting in sorted(meetings, key=lambda x:x[0]):
	found_room = False
	for room in rooms:
	    last_meeting = room[len(room)-1]
	    if meeting[0] >= last_meeting[1]:
		found_room = True
		room.append(meeting)
		break

	if not found_room:
	    rooms.append([meeting])

    return len(rooms)

meetings = (
    (10, 12),
    (10, 11),
    (10, 13),
    (11, 15),
    (13, 15),
    (13, 14),
    (14, 18),
    (12, 14))
    
print calc_best_meetings(meetings)
print calc_min_rooms(meetings)

"""
{
    "10-12": [(13, 14), (14, 18), (12, 14)],
    "10-11": [(11, 15), (13, 14), (14, 18), (12, 14)],
    ...
}
(10, 12) 
"""
