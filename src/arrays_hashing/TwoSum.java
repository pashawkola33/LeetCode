package arrays_hashing;

import java.util.HashMap;

public class TwoSum {
    public static void main(String[] args) {
        HashMap<Integer, Integer> nums = new HashMap<>();
        int[] array = {3, 2, 4};
        Integer target = 6;

        for (int i = 0; i < array.length; i++) {
            int compliment = target - array[i];

            if (nums.containsKey(compliment)) {
                System.out.println(nums.get(compliment) + " " + i);
            } else {
                nums.put(array[i], i);
            }
        }
    }
}
