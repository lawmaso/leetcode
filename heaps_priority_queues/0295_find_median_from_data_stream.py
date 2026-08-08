"""
The median is the middle value in an ordered integer list. If the
size of the list is even, there is no middle value, and the median
is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

Implement the MedianFinder class:
    MedianFinder()
        initializes the MedianFinder object.
    void addNum(int num)
        adds the integer num from the data stream to the data structure.
    double findMedian()
        returns the median of all elements so far. Answers within 10^(-5) of the
        actual answer will be accepted.

Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
medianFinder = MedianFinder()
medianFinder.addNum(1)     # arr = [1]
medianFinder.addNum(2)     # arr = [1, 2]
medianFinder.findMedian()  # return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3)     # arr[1, 2, 3]
medianFinder.findMedian()  # return 2.0        
"""

class BruteMedianFinder:
    """
    Brute force: sort after each insertion

    addNum: T: O(nlog(n)), S: O(n)
    findMedian: T: O(1), S: O(1)
    """

    nums: list[int]

    def __init__(self):
        self.nums = []

    def addNum(self, num: int):
        self.nums.append(num)
        self.nums.sort()

    def findMedian(self) -> float:
        n = len(self.nums)
        mid = n // 2

        # [1, 2, 3], odd: return nums[n // 2]
        if n & 1:
            return self.nums[mid]

        # [1, 2], even: return nums[n // 2] + nums[n // 2 - 1]
        # [1, 2, 3, 4]: ^
        return (self.nums[mid] + self.nums[mid - 1]) / 2

import heapq
class MedianFinder:
    """
    Optimal approach: min and max heaps

    Balance the two heaps to make the retrieval of
    middle elements more efficient (i.e., O(1))

    Avoids sorting by utilizing the heap property
    """
    left: list[int]   # max heap (negated values)
    right: list[int]  # min heap

    def __init__(self):
        self.left = []
        self.right = []

    def _balance(self):
        while abs(len(self.right) - len(self.left)) > 1:
            l, r = len(self.left), len(self.right)

            # pop from the larger heap, and push that value to the other
            pop_heap  = self.left if l > r else self.right
            push_heap = self.right if l > r else self.left

            # push to right heap (undo negation)
            # push to left heap (must negate)
            heapq.heappush(push_heap, -heapq.heappop(pop_heap))

            # if l > r:
            #     heapq.heappush(self.right, -heapq.heappop(self.left))
            # else:
            #     heapq.heappush(self.left, -heapq.heappop(self.right))

        # NOTE: after rebalancing, the min and max heaps
        # will differ in length by at most 1 (i.e., <= 1)

    def addNum(self, num: int):
        left_max = -self.left[0] if self.left else float("inf")

        # push to the correct stack
        if num > left_max:
            # num belongs in the right heap
            heapq.heappush(self.right, num)
        else:
            # num belongs in the left heap
            heapq.heappush(self.left, -num)

        # print("before", self.left, self.right)
        self._balance()
        # print("after", self.left, self.right)

    def findMedian(self) -> float:
        l, r = len(self.left), len(self.right)

        # [odd case] return root of the larger heap
        if l != r:
            if l > r:
                # return using max heap
                return -self.left[0]
            else:
                # return using min heap
                return self.right[0]

        # [even case] return average of heap roots
        return (-self.left[0] + self.right[0]) / 2

    def clear(self):
        self.left.clear()
        self.right.clear()

"""
left: max heap
right: min heap

left = [1]
right = []

n = len(left) + len(right) = 1 (odd)
median = left[0]

    -> return the root of the heap with more elements

left = [1]
right = [2]

    2: insert left or right? right
        len(left) != len(right)

    2 > left[0]=1? false -> import left
median = (left[0] + right[0]) / 2

left = [1]
right = [2, 3]

at the start, just insert into the left heap

algorithm:
    add to heaps then rebalance:
        while abs(len(right) - len(left)) > 1
            shuffle elements to rebalance

NOTE: we allow the heaps to differ by at most 1 to handle
the case where the number of elements is odd; otherwise,
we'd run into an infinite loop trying to balance the two heaps
to an even length, which would be impossible
"""

if __name__ == "__main__":
    medianFinder = MedianFinder()

    medianFinder.addNum(1)  # [1]
    assert medianFinder.findMedian() == 1.0

    medianFinder.addNum(2)  # [1,2]
    assert medianFinder.findMedian() == 1.5

    medianFinder.addNum(3)  # [1,2,3]
    assert medianFinder.findMedian() == 2.0

    medianFinder.addNum(0)  # [0,1,2,3]
    assert medianFinder.findMedian() == 1.5

    medianFinder.addNum(4)  # [0,1,2,3,4]
    assert medianFinder.findMedian() == 2.0

    medianFinder.addNum(3)  # [0,1,2,3,3,4]
    assert medianFinder.findMedian() == 2.5


    medianFinder.clear()

    medianFinder.addNum(1)
    medianFinder.addNum(-1)
    assert medianFinder.findMedian() == 0.0

    medianFinder.addNum(0)
    assert medianFinder.findMedian() == 0.0