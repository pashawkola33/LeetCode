/**
 * @lc id=3
 * @lc title=Longest Substring Without Repeating Characters
 * @lc difficulty=Medium
 * @lc time=O(n)
 * @lc space=O(k)
 */
package sliding_window;

import java.util.HashSet;

public class LongestSubstringWithoutRepeatingCharacters {
    public int lengthOfLongestSubstring(String s) {
        int left = 0;
        int max = 0;

        HashSet<Character> memorySet = new HashSet<>();


        for (int c = 0; c < s.length(); c++) {
            if (memorySet.add(s.charAt(c))) {
            } else {
                while (memorySet.contains(s.charAt(c))) {
                    memorySet.remove(s.charAt(left));
                    left++;
                }
                memorySet.add(s.charAt(c));
            }
            max = Math.max(max, c - left + 1);
        }
        return max;
    }
}
