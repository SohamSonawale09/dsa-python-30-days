# 4 Merge Intervals 
def merge(intervals):
    intervals.sort()   # Step 1: sort by first value
    
    result = [intervals[0]]   # store first interval
    
    for start, end in intervals[1:]:
        last_end = result[-1][1]
        
        if start <= last_end:   # overlap
            result[-1][1] = max(last_end, end)
        else:
            result.append([start, end])
    
    return result


print(merge([[1,3],[2,6],[8,10],[15,18]]))