from collections import defaultdict
import functools

"""
@author:  Infinixor 

"""
def compare(a, b):
    if a[2] == b[2]:
        if a[0] < b[0]:
            return -1
        return 1
    else:
        if a[2] < b[2]:
            return -1
        return 1

def maximumMeetings(start, end):
    n = len(start)
    meetings = [defaultdict(int) for _ in range(n)]
    
    for i in range(n):
        meetings[i][0] = i + 1
        meetings[i][1] = start[i]
        meetings[i][2] = end[i]
    
    meetings = sorted(meetings, key=functools.cmp_to_key(compare))
    result = []
    result.append(meetings[0][0])
    currentTime = meetings[0][2]
    
    for i in range(n):
        if meetings[i][1] > currentTime:
            result.append(meetings[i][0])
            currentTime = meetings[i][2]
    
    return result

def main():
    # Test case 1
    start1 = [1, 3, 0, 5, 8, 5]
    end1 = [2, 4, 6, 7, 9, 9]
    result1 = maximumMeetings(start1, end1)
    print("Maximum meetings for test case 1:", result1)

    # Test case 2
    start2 = [1, 2, 3, 4, 5]
    end2 = [2, 3, 4, 5, 6]
    result2 = maximumMeetings(start2, end2)
    print("Maximum meetings for test case 2:", result2)

# Run the main method
if __name__ == "__main__":
    main()
