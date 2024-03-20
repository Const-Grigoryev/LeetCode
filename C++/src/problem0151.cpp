/* 151. Reverse Words in a String
 * ------------------------------
 *
 * Given an input string `s`, reverse the order of the **words**.
 *
 * A **word** is defined as a sequence of non-space characters. The **words** in `s` will be separated by at least
 * one space.
 *
 * Return *a string of the words in reverse order concatenated by a single space*.
 *
 * **Note** that `s` may contain leading or trailing spaces or multiple spaces between two words. The returned string
 * should only have a single space separating the words. Do not include any extra spaces.
 *
 * ### Constraints:
 *
 *   * `1 <= s.length <= 10^4`
 *   * `s` contains English letters (upper-case and lower-case), digits, and spaces `' '`.
 *     There is at least one word in s.
 *
 * **Follow up:** Could you solve it **in-place** with `O(1)` extra space?
 *
 * Source: https://leetcode.com/problems/reverse-words-in-a-string/
 */

#include "common.h"

#include <cctype>
#include <algorithm>
#include <string>

class Solution {
public:
	std::string reverseWords(std::string &s) {
		// Exclude leading and trailing spaces
		auto begin = std::find_if_not(s.begin(), s.end(), isspace);
		auto end = std::find_if_not(s.rbegin(), s.rend(), isspace).base();

		if (begin <= end) {
			// Remove repeating spaces
			end = std::unique(begin, end,
				[](char x, char y) { return isspace(x) && isspace(y); }
			);

			// Reverse the whole string
			std::reverse(begin, end);

			// Detect each particular?? word and reverse it
			auto split = end;
			do {
				auto word_begin = split == end ? begin : split + 1;
				auto word_end = split = std::find_if(word_begin, end, isspace);
				std::reverse(word_begin, word_end);
			} while (split != end);
		}
		else {
			// Treat a corner case, when the string has no words
			begin = end;
		}

		s.assign(begin, end);
		return s;
	}
};

int main() {
	Solution s;
	std::string str;

	str = "the sky is blue";
	std::cout << "\'" << s.reverseWords(str) << "\' == \'blue is sky the\'" << std::endl;

	// Your reversed string should not contain leading or trailing spaces.
	str = "  hello world  ";
	std::cout << "\'" << s.reverseWords(str) << "\' == \'world hello\'" << std::endl;

	// You need to reduce multiple spaces between two words to a single space in the reversed string.
	str = "a good   example";
	std::cout << "\'" << s.reverseWords(str) << "\' == \'example good a\'" << std::endl;

	str = "  Bob    Loves  Alice   ";
	std::cout << "\'" << s.reverseWords(str) << "\' == \'Alice Loves Bob\'" << std::endl;

	str = "Alice does not even like bob";
	std::cout << "\'" << s.reverseWords(str) << "\' == \'bob like even not does Alice\'" << std::endl;
}
