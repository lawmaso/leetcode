"""
There are n cars at given miles away from the starting mile 0,
traveling to reach the mile target.

You are given two integer arrays position and speed, both of
length n, where position[i] is the starting mile of the ith car
and speed[i] is the speed of the ith car in miles per hour.

A car cannot pass another car, but it can catch up and then travel
next to it at the speed of the slower car.

A car fleet is a single car or a group of cars driving next to each
other. The speed of the car fleet is the minimum speed of any car in
the fleet.

If a car catches up to a car fleet at the mile target, it will still be
considered as part of the car fleet.

Return the number of car fleets that will arrive at the destination.

Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]

Output: 3

Explanation:

The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting
    each other at 12. The fleet forms at target.
The car starting at 0 (speed 1) does not catch up to any other car, so it
    is a fleet by itself.
The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting
    each other at 6. The fleet moves at speed 1 until it reaches target.

0 1 2 3 4 5 6 7 8 9 10 11 12
+     +   +     +   +
  +         +             ++

8 time to destination = (target - start) / speed
    = (12 - 8) / 4 = 1

10 time to destination = (12 - 10) / 2 = 1

8 and 10 form a fleet since ttd(8) <= ttd(12) [i.e., a car ahead of it]

Update fleet while ttd(curr) <= ttd(stack[-1])
"""

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        """
        Optimal: monotonic stack

        position: start of each car
        speed:    speed of each car

        All are aiming to reach <target> mile

        Utilize time-to-destination to see if
        cars can form a fleet

        If they do become a fleet, update the speed to the minimum
        of the fleet

        T: O(nlog(n))
        S: O(n)
        """
        stack = []  # (time to arrive at target)

        for start, speed in sorted(zip(position, speed)):
            arrival = (target - start) / speed

            # add to current fleet while previous cars can pass this one
            while stack and stack[-1] <= arrival:
                stack.pop()

            # append the new fleet
            stack.append(arrival)            

        # the stack consists of the fleets and their arrivals
        return len(stack)

if __name__ == "__main__":
    soln = Solution()

    for res, exp in [
        [soln.carFleet(12, [10,8,0,5,3], [2,4,1,1,3]), 3],
        [soln.carFleet(100, [0,2,4], [4,2,1]), 1],
        [soln.carFleet(10, [1,4], [3,2]), 1],
        [soln.carFleet(10, [4,1,0,7], [2,2,1,1]), 3]
    ]:
        print(res)
        assert res == exp
