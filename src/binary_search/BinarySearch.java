/**
 * @lc id=704
 * @lc title=Binary Search
 * @lc difficulty=Easy
 * @lc time=O(log n)
 * @lc space=O(1)
 */
package binary_search;

public class BinarySearch {

    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if(nums[mid] == target){
                return mid;
            }
            if(nums[mid] < target){
                left = mid + 1;
            }
            else {
                right = mid + 1;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        BinarySearch search = new BinarySearch();

        int[] array = {-1, 0, 3, 5, 9, 12};
        int target = 9;

        int bSearch = search.search(array, target);
        System.out.println(bSearch);
    }
}
