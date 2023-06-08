import bisect

"""
@author:  Infinixor 

"""
def jobScheduling(jobs):
    jobs.sort(key=lambda x: (-x[1], -x[0]))
    maxProfit = 0
    maxDeadline = 0

    # Find the maximum deadline among all the jobs.
    for i in range(len(jobs)):
        maxDeadline = max(maxDeadline, jobs[i][0])

    slots = list()

    # Insert all the elements from maxDeadline to 1 into the list.
    for i in range(1, maxDeadline + 1):
        slots.append(i)

    maxProfit = 0
    for i in range(len(jobs)):
        # If the set is empty or the deadline is less than the last element of the set, then ignore this job.
        if len(slots) == 0 or jobs[i][0] < slots[0]:
            continue

        availableSlot = slots[bisect.bisect(slots, jobs[i][0]) - 1]
        maxProfit += jobs[i][1]
        slots.remove(availableSlot)

    return maxProfit

def main():
    # Test case
    jobs = [(2, 60), (1, 100), (3, 20), (2, 40)]

    maxProfit = jobScheduling(jobs)

    print("Maximum Profit:", maxProfit)

if __name__ == "__main__":
    main()
