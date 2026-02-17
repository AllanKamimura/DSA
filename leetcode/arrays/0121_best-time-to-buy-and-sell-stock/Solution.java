class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0;

        int left = 0;
        int right = 1;

        while (right < prices.length){
            int leftValue = prices[left];
            int rightValue = prices[right];

            int currProfit = rightValue - leftValue;

            if (profit < currProfit) {
                profit = currProfit;
            }

            if (currProfit < 0) {
                left = right;
            }

            right++;
        }

        return profit;
    }
}