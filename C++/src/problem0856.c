/* 856. Score of Parentheses
 * -------------------------
 *
 * Given a balanced parentheses string `s`, compute the score of the string based on the following rule:
 *
 *   * () has score 1
 *   * `AB` has score `A + B`, where `A` and `B` are balanced parentheses strings.
 *   * `(A)` has score `2 * A`, where `A` is a balanced parentheses string.
 *
 * ### Note:
 *
 *   1. `s` is a balanced parentheses string, containing only `(` and `)`.
 *   2. `2 <= s.length <= 50`
 *
 * Source: https://leetcode.com/problems/score-of-parentheses/
 */

#include <stdio.h>

int scoreOfParentheses(char *s) {
	int score = 0, bid = 1;
	for (int i = 0, j = 1; s[j]; ++i, ++j) {
		if (s[i] == s[j]) {
			if (s[i] == '(')
				bid <<= 1;
			else
				bid >>= 1;
		}
		else {
			if (s[i] == '(')
				score += bid;
		}
	}
	return score;
}

int main(int argc, char *argv[]) {
	printf("%d == %d\n", scoreOfParentheses("()"), 1);
	printf("%d == %d\n", scoreOfParentheses("(())"), 2);
	printf("%d == %d\n", scoreOfParentheses("()()"), 2);
	printf("%d == %d\n", scoreOfParentheses("(()(()))"), 6);
}