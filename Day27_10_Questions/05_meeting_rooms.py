# 5 Meeting Rooms 
def canAttendMeetings(intervals):
    intervals.sort()   

    for i in range(1, len(intervals)):
        
        if intervals[i][0] < intervals[i-1][1]:
            return False

    return True


print(canAttendMeetings([[0,30],[5,10],[15,20]]))  
print(canAttendMeetings([[7,10],[2,4]]))          