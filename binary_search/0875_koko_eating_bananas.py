"""
Koko loves to eat bananas. There are n piles of bananas,
the ith pile has piles[i] bananas. The guards have gone
and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k.
Each hour, she chooses some pile of bananas and eats k
bananas from that pile. If the pile has less than k bananas,
she eats all of them instead and will not eat any more
bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all
the bananas before the guards return.

Return the minimum integer k such that she can eat all
the bananas within h hours.

Example 1:
Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:
Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:
Input: piles = [30,11,23,4,20], h = 6
Output: 23
"""

import math

class Solution:
    def brute_minEatingSpeed(self, piles: list[int], h: int) -> int:
        n = len(piles)
        mx = res = max(piles)

        for bph in range(1, mx + 1):
            took = 0  # hours taken

            for b in piles:
                took += math.ceil(b / bph)  # b/bph = time
                # ex: b=1, bph=3; b / bph = 0.33, but need int hours
                # ceil(0.33) = 1

            # eaten all piles within the time
            if took <= h:
                res = min(res, bph)
                break

                # NOTE: we can break here since we want the min
                #       eating speed that allows koko to eat all piles
                #       within h hours, which is just that

        return res

    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        n = len(piles)
        mx = res = max(piles)

        lo, hi = 1, mx

        while lo <= hi:
            bph = lo + (hi-lo) // 2
            
            # compute time taken to eat all piles at speed bph
            time = 0
            for b in piles:
                time += math.ceil(b / bph)

            if time <= h:  # eating too fast; search slower bph speeds
                hi = bph - 1
                res = min(res, bph)        
            else:  # eating too slow; search larger bph speeds
                lo = bph + 1
        
        return res

"""
brute force: try all eating speeds

lowest speed would be 1
highest speed would be max(piles)

for each speed, see how long it would take to eat
all the bananas

res = arg_min [...]

T: O(max(piles) * n)
S: O(1)
"""

"""
optimal: binary search on the eating speeds bph

lo, hi = 1, max(piles)

compute mid eating speed
determine time taken to eat all piles at this speed

if time <= h:  # eating too fast; decrease speed
    right = speed - 1
    res = min(res, speed)
if time > h:   # eating too slow; increase speed
    left = speed + 1

T: O(log[max(piles)] * n)
S: O(1)
"""

