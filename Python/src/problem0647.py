# 647. Palindromic Substrings
# ---------------------------

# Given a string `s`, return *the number of **palindromic substrings** in it*.
#
# A string is a **palindrome** when it reads the same backward as forward.
#
# A **substring** is a contiguous sequence of characters within the string.
#
# ### Constraints:
#
#   * `1 <= s.length <= 1000`
#   * `s` consists of lowercase English letters.

def gcp(xs, ys):
    n = 0
    for x, y in zip(xs, ys):
        if x == y:
            n += 1
        else:
            break
    return n

class Solution:
    def countSubstrings(self, s: str) -> int:
        return sum(
            gcp(s[k::-1], s[k:]) + gcp(s[k::-1], s[(k + 1):])
            for k in range(len(s))
        )


if __name__ == '__main__':
    s = Solution()

    # Three palindromic strings: "a", "b", "c".
    print(f"{s.countSubstrings(s='abc')} == 3")

    # Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
    print(f"{s.countSubstrings(s='aaa')} == 6")