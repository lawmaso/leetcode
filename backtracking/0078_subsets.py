"""
Given an integer array nums of unique elements,
return all possible subsets (the power set).

The solution set must not contain duplicate subsets.
Return the solution in any order.
"""

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        """
        Approach: DFS

        We're just computing the power set, which has 2^n possible
        subsets given a set of length n

        T: O(n * 2^n)  [DFS + adding result]
        S: O(2^n)      [output]
        """
        subsets = []

        def dfs(i: int = 0, subset: list[int] = []):
            if i >= len(nums):
                # we formed a subset; add it to the result
                subsets.append(subset.copy())
                return

            # exclude nums[i] from subset
            dfs(i + 1, subset)

            # include nums[i] in subset
            subset.append(nums[i])
            dfs(i + 1, subset)
            subset.pop()

        dfs()
        return subsets

if __name__ == "__main__":
    soln = Solution()

    for test_input in [
        [],
        [8],
        [1,2],
        [1,2,3,4]
    ]:
        res = soln.subsets(test_input)
        print(test_input, "->", res)

        assert len(res) == 2 ** (len(test_input))
