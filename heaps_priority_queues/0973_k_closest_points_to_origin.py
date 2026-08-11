"""
Given an array of points where points[i] = [xi, yi] represents a point on
the X-Y plane and an integer k, return the k closest points to the origin
(0, 0).

The distance between two points on the X-Y plane is the Euclidean distance
(i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique
(except for the order that it is in).
"""

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        """
        Brute force: compute + sort by distances

        T: O(n + nlog(n) + k) = O(nlog(n))
            O(n): computing distances to origin
            O(nlog(n)): sort
            O(k): get the k closest
        S: O(n)
        """

        def sq_dist(x: int, y: int) -> int:
            # sqrt[(x - 0)^2 + (y - 0)^2]
            # == sqrt(x^2 + y^2) 

            # sqrt is strictly increasing, so we can
            # just return the square of the distance
            # same result either way + lower computation cost
            return x*x + y*y

        # sort -> non-decreasing order
        point_tuples = sorted([
            (sq_dist(x, y), x, y)
            for x, y in points
        ])

        # extract the k closest to 0
        return [
            [x, y]
            for _, x, y in point_tuples[:k]
        ]

    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        """
        New approach: full min heap

        T: O(n + klog(n))
        S: O(n)
        """
        import heapq

        def sq_dist(x: int, y: int) -> int:
            # sqrt[(x - 0)^2 + (y - 0)^2]
            # == sqrt(x^2 + y^2) 

            # sqrt is strictly increasing, so we can
            # just return the square of the distance
            # same result either way + lower computation cost
            return x*x + y*y

        # build out the min heap
        heap = [
            (sq_dist(x, y), x, y)
            for x, y in points
        ]
        heapq.heapify(heap)

        res = []

        # pop off the k mins
        for _ in range(k):
            _, x, y = heapq.heappop(heap)
            res.append([x, y])

        return res

    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        """
        Optimal approach: heap of size k

        Want to keep the minimum k elements

        Max heap of size k: when the heap becomes too large,
        popping will remove the maxes, which is what we need

        T: O(nlog(k) + k) = O(nlog(k))
        S: O(k)
        """
        import heapq

        def sq_dist(x: int, y: int) -> int:
            # sqrt[(x - 0)^2 + (y - 0)^2]
            # == sqrt(x^2 + y^2) 

            # sqrt is strictly increasing, so we can
            # just return the square of the distance
            # same result either way + lower computation cost
            return x*x + y*y

        heap = []

        for x, y in points:
            dist = sq_dist(x, y)
            heapq.heappush(heap, (-dist, x, y))

            # heap is overpopulated
            if len(heap) > k:
                heapq.heappop(heap)

        # unnegate + get the k closest
        return [
            [x, y]
            for _, x, y in heap
        ]
