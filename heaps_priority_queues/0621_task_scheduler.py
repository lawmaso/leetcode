"""
You are given an array of CPU tasks, each labeled with
a letter from A to Z, and a number n. Each CPU interval
can be idle or allow the completion of one task. Tasks
can be completed in any order, but there's a constraint:
there has to be a gap of at least n intervals between two tasks
with the same label.

Return the minimum number of CPU intervals required to complete all tasks.

Input: tasks = ["A","A","A","B","B","B"], n = 2

Output: 8

Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

After completing task A, you must wait two intervals before doing A again.
The same applies to task B. In the 3rd interval, neither A nor B can be done,
so you idle. By the 4th interval, you can do A again as 2 intervals have passed.
"""

class Solution:
    """
    Approach: max heap + queue

    Utilize a queue to simulate the cooldown

    T: O(m)  [m=number of tasks]
    S: O(1)
    """

    def leastInterval(self, tasks: list[str], n: int) -> int:
        import heapq
        from collections import deque

        counts = dict()
        for task in tasks:
            counts[task] = counts.get(task, 0) + 1

        heap = [-count for _, count in counts.items()]
        heapq.heapify(heap)  # (-count)

        cooldown = deque([])  # (time_free, -count)
        interval = 0

        while heap or cooldown:
            interval += 1  # the new interval (to process or idle in)

            # fast-track to the earliest available task in the cooldown
            if not heap:
                interval = cooldown[0][0]
            # choose task in the heap otherwise
            else:
                count = heapq.heappop(heap) + 1
                if count != 0:
                    cooldown.append((interval + n, count))

            # task in cooldown is eligible to be scheduled again
            if cooldown and cooldown[0][0] == interval:
                heapq.heappush(heap, cooldown.popleft()[-1])
                # NOTE: we don't process it right away, as we need n intervals between
                # (the current interval is the interval before it can be processed)

        return interval

if __name__ == "__main__":
    scheduler = Solution()

    res = scheduler.leastInterval(["A","A","A","B","B","B"], 2)
    print(res)

    res = scheduler.leastInterval(["A","A"], 2)
    print(res)

"""
ex: [A, A], n=2

A, -, -, A, res=4

heap = [2A]
cooldown = []

t=0
t=1
    heap = []
    cooldown = [1 + 2, 1]
t=2:
    not heap; t=3
    heap = [(1A)]
t=4:
    heap = []

return 4
"""
