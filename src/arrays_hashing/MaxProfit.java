/**
 * @lc id=121
 * @lc title=Best Time to Buy and Sell Stock
 * @lc difficulty=Easy
 * @lc time=O(n)
 * @lc space=O(1)
 */
package arrays_hashing;

public class MaxProfit {
    public int maxProfit(int[] prices) {
        int minPrice = Integer.MAX_VALUE; //10000000
        int maxProfit = 0;

        for (int i = 0; i < prices.length; i++) {
            if (prices[i] < minPrice) {
                minPrice = prices[i];
            }
            if((prices[i] - minPrice) > maxProfit){
            maxProfit = prices[i] - minPrice;
            }
        }
        return maxProfit;
    }

    public static void main(String[] args) {
        MaxProfit maxProfit = new MaxProfit();

        int[] array = {9, 2, 6, 7, 1, 12}; //0,1,2,3,4,5
        int maxProf = maxProfit.maxProfit(array);
        System.out.println(maxProf);
    }
}
