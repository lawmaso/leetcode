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

class MedianFinder:
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


if __name__ == "__main__":
    medianFinder = MedianFinder()
    medianFinder.addNum(1)                   # arr = [1]
    medianFinder.addNum(2)                   # arr = [1, 2]
    assert medianFinder.findMedian() == 1.5  # return 1.5 (i.e., (1 + 2) / 2)
    medianFinder.addNum(3)                   # arr[1, 2, 3]
    assert medianFinder.findMedian() == 2.0  # return 2.0
