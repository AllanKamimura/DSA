from collections import Counter
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        counter = Counter(nums)
        sorted_keys = sorted(counter)
        results = set()

        for i, x in enumerate(sorted_keys):
            target = -x

            for y in sorted_keys[i:]:
                z = target - y

                if z < y:  # maintain order x <= y <= z
                    continue
                if z not in counter:
                    continue

                if z == x and z == y:
                    if counter[z] > 2:
                        results.add(tuple((x, y, z)))
                elif z == x or z == y:
                    if counter[z] > 1:
                        results.add(tuple((x, y, z)))
                elif x == y:
                    if counter[x] > 1:
                        results.add(tuple((x, y, z)))
                else:
                    results.add(tuple((x, y, z)))

        return [list(triplet) for triplet in results]
