# 5. Longest Palindromic Substring
# --------------------------------
#
# Given a string `s`, return *the longest palindromic substring* in `s`.
#
# ### Constraints:
#
#   * `1 <= s.length <= 1000`
#   * `s` consist of only digits and English letters (lower-case and/or upper-case),

def gcp(xs, ys):
    n = 0
    for x, y in zip(xs, ys):
        if x == y:
            n += 1
        else:
            break
    return n

class Solution:
    def longestPalindrome(self, s: str) -> str:
        pal = ''
        for k in range(len(s)):
            n = gcp(s[k::-1], s[k:])
            if len(pal) < 2 * n - 1:
                pal = s[(k - n + 1):(k + n)]

            n = gcp(s[k::-1], s[(k + 1):])
            if len(pal) < 2 * n:
                pal = s[(k - n + 1):(k + n + 1)]
        return pal


if __name__ == '__main__':
    s = Solution()

    print(f"{s.longestPalindrome(s='babad')} == 'bab' or 'aba'")
    print(f"{s.longestPalindrome(s='cbbd')} == 'bb'")
    print(f"{s.longestPalindrome(s='a')} == 'a'")