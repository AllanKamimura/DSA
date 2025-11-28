# 1472. Design Browser History

[🔗 LeetCode Link](https://leetcode.com/problems/design-browser-history/description/)

## Solution

### Stack

#### Explanation

We can use 2 stacks,
one to keep track of back pages, when we visit a new page,
one to keep track of forward pages, when we use the back button.

#### Manual Run



#### Time Complexity

- O(n) -> We transverse the array a single time.

#### Space Complexity

- O(1) -> We only create integer variables.
