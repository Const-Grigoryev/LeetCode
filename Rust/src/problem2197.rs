/**
 * 2197. Replace Non-Coprime Numbers in Array
 * ------------------------------------------
 *
 * You are given an array of integers `nums`. Perform the following steps:
 *
 *   1. Find any two adjacent numbers in `nums` that are **non-coprime**.
 *   2. If no such numbers are found, stop the process.
 *   3. Otherwise, delete the two numbers and replace them with their **LCM (Least Common Multiple)**.
 *   4. Repeat this process as long as you keep finding two adjacent non-coprime numbers.
 *
 * Return *the **final** modified array*. It can be shown that replacing adjacent non-coprime numbers in any
 * arbitrary order will lead to the same result.
 *
 * The test cases are generated such that the values in the final array are less than or equal to `10^8`.
 *
 * Two values `x` and `y` are non-coprime if `GCD(x, y) > 1` where `GCD(x, y)` is the **Greatest Common Divisor**
 * of `x` and `y`.
 *
 * ### Constraints:
 *
 *   * `1 <= nums.length <= 10^5`
 *   * `1 <= nums[i] <= 10^5`
 *   * The test cases are generated such that the values in the final array are **less than or equal** to `10^8`.
 *
 * Source: https://leetcode.com/problems/replace-non-coprime-numbers-in-array/
 */

struct Solution;

impl Solution {
	pub fn replace_non_coprimes(nums: Vec<i32>) -> Vec<i32> {
		nums.iter().copied()
			.fold(Vec::new(), |mut ans, mut x| {
                while let Some(d) = ans.last()
                    .map(|&y| gcd(y, x))
                    .filter(|&d| d != 1)
                {
                    x *= ans.pop().unwrap() / d;
                }
                ans.push(x);
                ans
            })
	}
}

fn gcd(mut a: i32, mut b: i32) -> i32 {
    let parity = (a | b).trailing_zeros();
    a >>= a.trailing_zeros();
    while b != 0 && a != 1 {
        b >>= b.trailing_zeros();
        (a, b) = (i32::min(a, b), i32::abs_diff(a, b) as i32);
    }
    a << parity
}

fn main() {
	// Example 1:
	//
	// Input: nums = [6,4,3,2,7,6,2]
	// Output: [12,7,6]
	// Explanation:
	// - (6, 4) are non-coprime with LCM(6, 4) = 12. Now, nums = [12,3,2,7,6,2].
	// - (12, 3) are non-coprime with LCM(12, 3) = 12. Now, nums = [12,2,7,6,2].
	// - (12, 2) are non-coprime with LCM(12, 2) = 12. Now, nums = [12,7,6,2].
	// - (6, 2) are non-coprime with LCM(6, 2) = 6. Now, nums = [12,7,6].
	// There are no more adjacent non-coprime numbers in nums.
	// Note that there are other ways to obtain the same resultant array.
	println!("{:?} == [12, 7, 6]", Solution::replace_non_coprimes(vec![6, 4, 3, 2, 7, 6, 2]));

	// Example 2:
	//
	// Input: nums = [2,2,1,1,3,3,3]
	// Output: [2,1,1,3]
	// Explanation:
	// - (3, 3) are non-coprime with LCM(3, 3) = 3. Now, nums = [2,2,1,1,3,3].
	// - (3, 3) are non-coprime with LCM(3, 3) = 3. Now, nums = [2,2,1,1,3].
	// - (2, 2) are non-coprime with LCM(2, 2) = 2. Now, nums = [2,1,1,3].
	// There are no more adjacent non-coprime numbers in nums.
	// Note that there are other ways to obtain the same resultant array.
	println!("{:?} == [2, 1, 1, 3]", Solution::replace_non_coprimes(vec![2, 2, 1, 1, 3, 3, 3]));
}
