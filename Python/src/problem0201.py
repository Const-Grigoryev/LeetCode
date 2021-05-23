# 201. Bitwise AND of Numbers Range
# ---------------------------------
#
# Given two integers `left` and `right` that represent the range `[left, right]`, return *the bitwise AND of all
# numbers in this range, inclusive*.
#
# ### Constraints:
#
#   * `0 <= left <= right <= 2^31 - 1`

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        mask = n - m
        mask |= mask >> 1
        mask |= mask >> 2
        mask |= mask >> 4
        mask |= mask >> 8
        mask |= mask >> 16
        return (m & n) & ~mask


if __name__ == '__main__':
    s = Solution()

    print(f"{s.rangeBitwiseAnd(5, 7)} == 4")
    print(f"{s.rangeBitwiseAnd(0, 0)} == 0")
    print(f"{s.rangeBitwiseAnd(1, 2147483647)} == 0")