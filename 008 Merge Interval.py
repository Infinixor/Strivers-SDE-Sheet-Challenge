class Solution:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def mergeIntervals(intervals):
    n = len(intervals)
    res = []

    for i in range(n):
        curS = intervals[i].start
        curE = intervals[i].end

        if len(res) == 0 or curS > res[-1].end:
            res.append(intervals[i])
        else:
            res[-1].end = max(res[-1].end, curE)

    return res


if __name__ == "__main__":
    # Test case 1
    pass