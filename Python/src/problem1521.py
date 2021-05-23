# 1521. Find a Value of a Mysterious Function Closest to Target
# -------------------------------------------------------------
#
#     func(arr, l, r) {
#         if (r < l) {
#             return -1000000000
#         }
#         and = arr[l]
#         for (i = l + 1; i <= r; i++) {
#             ans = ans & arr[i]
#         }
#         return ans
#     }
#
# Winston was given the above mysterious function `func`. He has an integer array `arr` and an integer `target` and
# he wants to find the values `l` and `r` that make the value `|func(arr, l, r) - target|` minimum possible.
#
# Return *the minimum possible value* of `|func(arr, l, r) - target|`.
#
# Notice that `func` should be called with the values `l` and `r` where `0 <= l, r < arr.length`.
#
# ### Constraints:
#
#   * `1 <= arr.length <= 10^5`
#   * `1 <= arr[i] <= 10^6`
#   * `0 <= target <= 10^7`

import itertools

class ElementWise:
    def __rand__(self, lhs):
        return (x & y for x, y in zip(lhs, self))

class repeat(itertools.repeat, ElementWise): pass

def subranges(n):
    h = 1
    while h < n:
        for m in range(h, n, 2 * h):
            yield m - h, m, min(m + h, n)
        h *= 2

def traverse(xs, ys, target):
    x = next(xs := iter(xs), None)
    y = next(ys := iter(ys), None)
    while x is not None and y is not None:
        yield (v := x & y)
        if v < target:
            x = next(xs, None)
        else:
            y = next(ys, None)

def problem1521(arr, target):
    n = len(arr)
    cf = lambda v: abs(v - target)
    cost = list(repeat(None, 2 * n - 1))
    suff = list(arr)
    pref = list(arr)
    for m in range(n):
        cost[2 * m] = cf(arr[m])
    for l, m, r in subranges(n):
        cost[2 * m - 1] = min(cf(v) for v in traverse(suff[l:m], pref[m:r], target))
        suff[l:m] &= repeat(suff[m])
        pref[m:r] &= repeat(pref[m - 1])
    return min(cost)

class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        return problem1521(arr, target)


if __name__ == '__main__':
    s = Solution()

    # Calling func with all the pairs of [l,r] = [[0,0],[1,1],[2,2],[3,3],[4,4],[0,1],[1,2],[2,3],[3,4],[0,2],[1,3],
    # [2,4],[0,3],[1,4],[0,4]], Winston got the following results [9,12,3,7,15,8,0,3,7,0,0,3,0,0,0]. The value closest
    # to 5 is 7 and 3, thus the minimum difference is 2.
    print(f"{s.closestToTarget(arr=[9, 12, 3, 7, 15], target=5)} == 2")

    # Winston called the func with all possible values of [l,r] and he always got 1000000, thus the min difference
    # is 999999.
    print(f"{s.closestToTarget(arr=[1000000, 1000000, 1000000], target=1)} == 999999")

    print(f"{s.closestToTarget(arr=[1,2,4,8,16], target=0)} == 0")