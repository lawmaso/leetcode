"""
You are part of a university admissions office and need
to keep track of the kth highest test score from applicants
in real-time. This helps to determine cut-off marks for
interviews and admissions dynamically as new applicants
submit their scores.

You are tasked to implement a class which, for a given
integer k, maintains a stream of test scores and continuously
returns the kth highest test score after a new score has been
submitted. More specifically, we are looking for the kth highest
score in the sorted list of all scores.

Implement the KthLargest class:
    KthLargest(int k, int[] nums)
        Initializes the object with the integer k and the stream of test
        scores nums.
    int add(int val)
        Adds a new test score val to the stream and returns the element
        representing the kth largest element in the pool of test scores so far.

ex1:
Input:
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]

Output: [null, 4, 5, 5, 8, 8]

Explanation:

kthLargest = KthLargest(3, [4, 5, 8, 2])
kthLargest.add(3)  // return 4
kthLargest.add(5)  // return 5
kthLargest.add(10) // return 5
kthLargest.add(9)  // return 8
kthLargest.add(4)  // return 8

[2,4,5,8]
"""

import heapq

class KthLargest:
    """
    Approach: min heap with capacity k

    After an insert and we are over capacity, balance
    the heap (i.e., remove excess elements not within
    k largest elements)

    After balanceing, the top of the heap will be the
    kth largest in the stream of data

    T: O(log(n))  [heap pop/push]
    S: O(k)       [heap upper limit of elements]

    At initialization, time is O(n + max(0, n-k) * log(n))
        O(n): heapify cost  [better than inserting 1-by-1]
        O(max(0, n - k) * log(n)): pop non-kth-largest items
    """
    k: int
    heap: list[int]

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = nums.copy()
        heapq.heapify(self.heap)

        # ensure the heap is the bounded by k
        self._balance()

    def _balance(self):
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        self._balance()
        return self.heap[0]
        
"""
dryrun: kthLargest = KthLargest(3, [4, 5, 8, 2])

after init, heap consists of [4,5,8]

+: indicates it's being returned

kthLargest.add(3)  // return 4: [3,4,5,8]  -> [4+,5,8]
kthLargest.add(5)  // return 5: [4,5,5,8]  -> [5+,5,8]
kthLargest.add(10) // return 5: [5,5,8,10] -> [5+,8,10]
kthLargest.add(9)  // return 8: [5,8,9,10] -> [8+,9,10]
kthLargest.add(4)  // return 8: [4,8,9,10] -> [8+,9,10]

all cases pass
"""

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

if __name__ == "__main__":
    kthLargest = KthLargest(3, [4, 5, 8, 2])

    assert kthLargest.add(3)  == 4  # return 4
    assert kthLargest.add(5)  == 5  # return 5
    assert kthLargest.add(10) == 5  # return 5
    assert kthLargest.add(9)  == 8  # return 8
    assert kthLargest.add(4)  == 8  # return 8
