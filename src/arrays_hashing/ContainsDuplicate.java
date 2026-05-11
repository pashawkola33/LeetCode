/**
 * @lc id=217
 * @lc title=Contains Duplicate
 * @lc difficulty=Easy
 * @lc time=O(n)
 * @lc space=O(n)
 */
package arrays_hashing;

import java.util.HashSet;

public class ContainsDuplicate {


    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> noDuplicates = new HashSet<>();
        for (int i = 0; i < nums.length; i++) {
            if (!noDuplicates.add(nums[i])) {
                return true;
            }
        }
        return false;
    }


    public static void main(String[] args) {
        int[] array = {1, 1, 2, 3, 4, 5};


        ContainsDuplicate solution = new ContainsDuplicate();



        boolean hasDup = solution.containsDuplicate(array);
        System.out.println(hasDup);
    }
}
