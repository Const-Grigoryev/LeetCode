package dev.aspid812.leetcode.problem0048;

/* 48. Rotate Image
 * ----------------
 *
 * You are given an _n_ x _n_ 2D `matrix` representing an image, rotate the image by 90 degrees (clockwise).
 *
 * You have to rotate the image [**in-place**](https://en.wikipedia.org/wiki/In-place_algorithm), which means you
 * have to modify the input 2D matrix directly. **DO NOT** allocate another 2D matrix and do the rotation.
 *
 * ### Constraints:
 *
 *   * `matrix.length == n`
 *   * `matrix[i].length == n`
 *   * `1 <= n <= 20`
 *   * `-1000 <= matrix[i][j] <= 1000`
 *
 * Source: https://leetcode.com/problems/rotate-image/
 */

import java.util.Arrays;

public class Solution {
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        int m = n - 1;
        for (int i = 0; i < n / 2; ++i) {
            for (int j = 0; j <= m / 2; ++j) {
                int a1 = matrix[i][j];
                int a2 = matrix[j][m - i];
                int a3 = matrix[m - i][m - j];
                int a4 = matrix[m - j][i];

                matrix[i][j] = a4;
                matrix[j][m - i] = a1;
                matrix[m - i][m - j] = a2;
                matrix[m - j][i] = a3;
            }
        }
    }

    public static void main(String[] args) {
        var s = new Solution();

        int[][] matrix1 = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        s.rotate(matrix1);
        System.out.println(Arrays.deepToString(matrix1) + " == [[7,4,1],[8,5,2],[9,6,3]]");

        int[][] matrix2 = {{5, 1, 9, 11}, {2, 4, 8, 10}, {13, 3, 6, 7}, {15, 14, 12, 16}};
        s.rotate(matrix2);
        System.out.println(Arrays.deepToString(matrix2) + " == [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]");

        int[][] matrix3 = {{1}};
        s.rotate(matrix3);
        System.out.println(Arrays.deepToString(matrix3) + " == [[1]]");

        int[][] matrix4 = {{1, 2}, {3, 4}};
        s.rotate(matrix4);
        System.out.println(Arrays.deepToString(matrix4) + " == [[3, 1], [4, 2]");
    }
}
