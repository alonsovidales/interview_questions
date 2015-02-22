def can_i_assist_to_all_meetings(meetings):
    sorted_meetings = sorted(meetings, key=lambda x: x[0]) # O(n log n)
    for i in xrange(len(sorted_meetings)-1):
        if sorted_meetings[i][1] > sorted_meetings[i+1][0]:
               return False
               
    return True

https://github.com/alonsovidales/interview_questions/blob/master/meetings.py <=
https://github.com/alonsovidales/interview_questions <=

import from colections defaultdict

def _create_graph(meetings):
    result = defaultdict(list)
    for meeting in meetings:
        key = '-'.join(meeting)
        for meeting_to in meetings:
            to_str = '-'.join(meeting_to)
            result[key].append(to_str)

    return result
    
def calc_max_rooms(meetings):
    max_rooms = 0
    for meeting in meetings:
        overlap_meetings = 1 # <==
        rooms = set(meeting)
        for meeting_to in meetings:
             if (
                (meeting[0] < meeting_to[1] < meeting[0] or
                 meeting[0] < meeting_to[1] < meeting[0] or
                 meeting[1] < meeting_to[0] < meeting[1] or
                 meeting[1] < meeting_to[0] < meeting[1]):
                 can_i_reuse_a_room = False
                 for room in rooms:
                     if room[1] < meeting_to[0] or room[0] > meeting_to[1]:
                         can_i_reuse_a_room = True
                         break
                        
                if not can_i_reuse_a_room:   
                    rooms.add(meeting_to)
                    overlap_meetings += 1
                
        if max_rooms < overlap_meetings:
            max_rooms = overlap_meetings
            
    return max_rooms

[
  [1,2]
  [2,3]
  [1,3] <--
  [2,2]
]

[1,3] - [1,2]
[1,3] - [2,3]

meetings = ([
  [1, 3]
  [10, 15]
  [10, 30]
  [12, 45]
  [40, 50]
  [1000000000000, 10000000000001]
])


1 - 3   10 - 15    40 - 50
              12 - 45
        10 - 30

print can_i_assist_to_all_meetings(meetings)

{
 '1-3': ['10-15', '10-30'] <--
}

1 - 3 - 2 -  1
3
