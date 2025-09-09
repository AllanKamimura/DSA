# 496. Next Greater Element I

[🔗 LeetCode Link](https://leetcode.com/problems/next-greater-element-i/description/)

## Solution

### Hashmap + Stack

#### Explanation

The core idea is to use a hashmap to map each number to it's next greater.

We start iterating nums2, we add the values to a monotonic stack until we find a future greater value.

Each time we find a value that is bigger than the top of the stack,
we unpack the stack and map it using a lookup_table.

With the pre-computed lookup_table, we iterate over nums1.
There is an inefficiency here, because no matter the size of nums1,
we always ends up iterating over all elements in nums2.

#### Manual Run

```python
nums1 = [4,1,2], nums2 = [1,3,4,2]
```

iterate over nums2

num | stack | lookup_table
--- | --- | ----
1 | [1] | {}
3 | [3] | {1:3}
4 | [4] | {1:3, 3:4}
2 | [4,2] | {1:3, 3:4}

unpack the stack

num | stack | lookup_table
--- | --- | ----
2 | [4] | {1:3, 3:4, 2:-1}
4 | [ ] | {1:3, 3:4, 2:-1, 4:-1}

iterate over nums1

num | next
--- | ------
4 | -1
1 | 3
2 | -1

```python
return output = [-1, 3, -1]
```

#### Time Complexity

- O(n1 + n2)
  - O(n2) -> To create the lookup_table.
  - O(n1) -> To iterate over nums1 and get the output from lookup_table.

#### Space Complexity

- O(n2) -> The stack has at most n2 elements.
- O(n2) -> The lookup_table has at most n2 elements.

### Hashmap

#### Explanation

The core idea is to use a hashmap to map each number to it's next greater.

We start iterating nums2 from the end. For each number:

1. If curr_num < prev_number: we found the next greater
2. Otherwise, we compare curr_num with lookup_table[prev_number]
    1. This is valid, since we already know that this is the next greater number.

With the pre-computed lookup_table, we iterate over nums1.
There is an inefficiency here, because no matter the size of nums1,
we always ends up iterating over all elements in nums2.

#### Manual Run 2

```python
nums1 = [4,1,2], nums2 = [1,3,4,2]
lookup_table = {2: inf}
```

iterate over nums2

num | prev_num | lookup_table
--- | ------   | ----
4 | 2 | {2:inf, 4: inf}
3 | 4 | {2:inf, 4: inf, 3: 4}
1 | 3 | {2:inf, 4: inf, 3: 4, 1: 3}

iterate over nums1

num | next
--- | ------
4 | -1
1 | 3
2 | -1

```python
return output = [-1, 3, -1]
```

#### Time Complexity 2

- O(n1 + n2)
  - O(n2) -> To create the lookup_table.
    - We add each value only 1 time to the stack.
    - In the while loop, we remove each element from the stack at most 1 time.
  - O(n1) -> To iterate over nums1 and get the output from lookup_table.

#### Space Complexity

- O(n2) -> The lookup_table has at most n2 elements.
