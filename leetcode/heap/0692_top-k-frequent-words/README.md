# 692. Top K Frequent Words

[🔗 LeetCode Link](https://leetcode.com/problems/top-k-frequent-words/description/)

## Solution

### Counter + Heap

#### Explanation

This problem is pretty straightforward,
and very similar to [451. Sort Characters By Frequency](../../strings/0451_sort-characters-by-frequency/README.md).

The difference is that here,
we don't know the number of unique elements in the list,
so sorting the `counter` can be O(n ⋅ log(n)) in the worst case.

We can instead use a heap.
This solution is O(k ⋅ log(n)), and in the worst case, k=n so we get the same as sorting the counter.

#### Manual Run

skip

#### Time Complexity

- O(k ⋅ log(n)) -> We pop from the heap k times.

#### Space Complexity

- O(n) -> In the worst case, the heap has n words.
