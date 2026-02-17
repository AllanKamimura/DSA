class Solution {
    public int[] rotate(int[] nums, int k) {
        /*
        Do not return anything, modify nums in-place instead.
        */

        // this handles the case where k > len(nums)
        int n = nums.length;
        k %= n;

        int currIndex = 0;
        int currValue = nums[currIndex];
        int nextIndex = (currIndex + k) % n;
        int nextValue = nums[nextIndex];
        int count = 0;

        for (int startPoint = 0; startPoint < n; startPoint++){
            if (count >= n) {
                break;
            }

            currIndex = startPoint;
            currValue = nums[currIndex];

            while (nextIndex != startPoint) {
                nextIndex = (currIndex + k) % n;
                nextValue = nums[nextIndex];

                nums[nextIndex] = currValue;
                currValue = nextValue;
                currIndex = nextIndex;

                count++;
            }
        }

        return nums;
    }
}