# 39. Combination Sum
# -------------------
#
# Given an array of **distinct** integers `candidates` and a target integer `target`, return *a list of all **unique
# combinations** of `candidate`s where the chosen numbers sum to `target`*. You may return the combinations in **any
# order**.
#
# The **same** number may be chosen from `candidates` an **unlimited number of times**. Two combinations are unique if
# the frequency of at least one of the chosen numbers is different.
#
# It is **guaranteed** that the number of unique combinations that sum up to target is less than 150 combinations
# for the given input.
#
# ### Constraints:
#
#   * `1 <= candidates.length <= 30`
#   * `1 <= candidates[i] <= 200`
#   * All elements of `candidates` are **distinct**.
#   * `1 <= target <= 500`.
#
# Source: https://leetcode.com/problems/combination-sum/

from typing import List
from collections import namedtuple

Sum = namedtuple('Sum', 'value times tail')

def iterateSum(sum):
    while sum is not None:
        yield sum
        sum = sum.tail

def renderSum(sum):
    return list(s.value for s in iterateSum(sum) for _ in range(s.times))

def generateSums(candidates, target, sum):
    if target == 0:
        yield sum
    elif candidates:
        value, times = candidates[0], 0
        while target - value * times >= 0:
            yield from generateSums(candidates[1:], target - value * times, Sum(value, times, sum))
            times += 1

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return list(renderSum(sum) for sum in generateSums(candidates, target, None))


if __name__ == '__main__':
    s = Solution()

    # Example 1:
    #
    # Input: candidates = [2,3,6,7], target = 7
    # Output: [[2,2,3],[7]]
    # Explanation:
    # 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
    # 7 is a candidate, and 7 = 7.
    # These are the only two combinations.
    print(f"{s.combinationSum(candidates=[2, 3, 6, 7], target=7)} == [[2,2,3], [7]]")

    # Example 2:
    #
    # Input: candidates = [2,3,5], target = 8
    # Output: [[2,2,2,2],[2,3,3],[3,5]]
    print(f"{s.combinationSum(candidates=[2, 3, 5], target=8)} == [[2,2,2,2], [2,3,3], [3,5]]")

    # Example 3:
    #
    # Input: candidates = [2], target = 1
    # Output: []
    print(f"{s.combinationSum(candidates=[2], target=1)} == []")

    # Example 4:
    #
    # Input: candidates = [1], target = 1
    # Output: [[1]]
    print(f"{s.combinationSum(candidates=[1], target=1)} == [[1]]")

    # Example 5:
    #
    # Input: candidates = [1], target = 2
    # Output: [[1,1]]
    print(f"{s.combinationSum(candidates=[1], target=2)} == [[1,1]]")