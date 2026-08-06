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
