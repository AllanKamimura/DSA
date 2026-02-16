class Solution {
    public int[] moveZeroes(int[] nums) {
        int i = 0;
        int j = 0;

        while (j < nums.length){
            int firstValue = nums[i];
            int secondValue = nums[j];

            if (secondValue != 0){
                nums[i] = secondValue;
                nums[j] = firstValue;
                i++;
            }

            j++;
        }

        return nums;
    }
}