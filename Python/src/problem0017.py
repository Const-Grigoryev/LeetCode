# 17. Letter Combinations of a Phone Number
# -----------------------------------------
#
# Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could
# represent. Return the answer in **any order**.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any
# letters.
#
#     [1     ] [2 abc] [3  def]
#     [4  ghi] [5 jkl] [6  mno]
#     [7 pqrs] [8 tuv] [9 wxyz]
#
# ### Constraints:
#
#   * `0 <= digits.length <= 4`
#   * `digits[i]` is a digit in the range `['2', '9']`.

from typing import List
import itertools

MAP = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits:
            return list(
                ''.join(ltr)
                for ltr in itertools.product(*(MAP[d] for d in digits))
            )
        else:
            return []


if __name__ == '__main__':
    s = Solution()

    # Example 1:
    #
    # Input: digits = "23"
    # Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    print(f"{s.letterCombinations('23')} == ['ad','ae','af','bd','be','bf','cd','ce','cf']")

    # Example 2:
    #
    # Input: digits = ""
    # Output: []
    print(f"{s.letterCombinations('')} == []")

    # Example 3:
    #
    # Input: digits = "2"
    # Output: ["a","b","c"]
    print(f"{s.letterCombinations('2')} == ['a','b','c']")