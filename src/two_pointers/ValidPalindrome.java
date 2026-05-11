/**
 * @lc id=125
 * @lc title=Valid Palindrome
 * @lc difficulty=Easy
 * @lc time=O(n)
 * @lc space=O(1)
 */
package two_pointers;

import java.util.Locale;

public class ValidPalindrome {
    public boolean isPalindrome(String s) {
        int left = 0;
        int right = s.length() - 1;

        while (left < right) {
            char leftChar = s.charAt(left);
            char rightChar = s.charAt(right);

            if (!Character.isLetterOrDigit(leftChar)) {
                left++;
            } else if (!Character.isLetterOrDigit(rightChar)) {
                right--;
            } else {
                // Сюда мы попадем, только если оба символа — буквы/цифры
                if (Character.toLowerCase(leftChar) != Character.toLowerCase(rightChar)) {
                    return false;
                }
                left++;
                right--;
            }
        }
        return true;
    }

    public static void main(String args[]) {

    }
}
