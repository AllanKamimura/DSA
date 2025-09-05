# 227. Basic Calculator Ii

[🔗 LeetCode Link](https://leetcode.com/problems/basic-calculator-ii/description/)

## Solution

### Stack

#### Explanation

Using a similar approach from [150. Evaluate Reverse Polish Notation](../0150_evaluate-reverse-polish-notation/),
we do 2 passes, one evaluating the products and the second for the sums.

There's some traps in test cases, like extra spaces, so we need to preprocess the string.

#### Manual Run

```python
Input: s = "3+2*2"

# preprocess
stack = ["3", "+", "2", "*", "2"]

# do_product
stack = ["3", "+", "4"]

# do_sum
stack = ["7"]

return stack[-1] = 7
```

#### Time Complexity

- O(n) -> We transverse the string 3 times.

#### Space Complexity

- O(n) -> In the worst case, we have ~ n/2 elements in the stack.
