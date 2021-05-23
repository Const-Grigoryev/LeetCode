# 848. Shifting Letters
# ---------------------
#
# We have a string `s` of lowercase letters, and an integer array `shifts`.
#
# Call the *shift* of a letter, the next letter in the alphabet, (wrapping around so that `'z'` becomes `'a'`).
#
# For example, `shift('a') = 'b'`, `shift('t') = 'u'`, and `shift('z') = 'a'`.
#
# Now for each `shifts[i] = x`, we want to shift the first `i+1` letters of `S`, `x` times.
#
# Return the final string after all such shifts to `s` are applied.
#
# ### Note:
#
#   1. `1 <= s.length = shifts.length <= 20000`
#   2. `0 <= shifts[i] <= 10^9`

from typing import List
from itertools import accumulate
import string

A = ord('a')
def shift(c, h):
    return string.ascii_lowercase[(ord(c) - A + h) % 26]

class Solution:
    def shiftingLetters(self, string: str, shifts: List[int]) -> str:
        h0 = sum(shifts)
        return "".join(shift(c, h0 - h) for c, h in zip(string, accumulate(shifts, initial=0)))


if __name__ == '__main__':
    s = Solution()

    # We start with "abc".
    # After shifting the first 1 letters of S by 3, we have "dbc".
    # After shifting the first 2 letters of S by 5, we have "igc".
    # After shifting the first 3 letters of S by 9, we have "rpl", the answer.
    print(f"{s.shiftingLetters(string='abc', shifts=[3, 5, 9])} == 'rpl'")