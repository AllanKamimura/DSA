from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left = 0
        right = n - 1

        while True:
            sum = numbers[left] + numbers[right]

            if sum == target:
                break
            elif sum > target:
                right -= 1
            elif sum < target:
                left += 1

        return [left + 1, right + 1]
