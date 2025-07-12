# 11. Container With Most Water

[🔗 LeetCode Link](https://leetcode.com/problems/container-with-most-water/description/)

## Solution

### Two pointers approach

#### Explanation

To get the intuition to solve this problem,
the first thing to notice is that,
"the water spills over the shorter wall",
in another words, the shorter wall limits the height of the area.

A = min(h1,h2) * width

So we start 2 pointers, left and right at the start and end of the array,
we compare the heights, and move inwards the pointer with the shorter height.

Since we are taking the min height for the area,
the only way to get a bigger area is by increasing the width.

Therefore, any pair formed by the shortest height
and a future pointer is bound to be smaller than the current area.

Also, we create a max_area to track the biggest so far.

#### Manual Run

```python
height = [1,8,6,2,5,4,8,3,7]
```

left | left_value | right | right_value | curr_area | max_area
---| --- | --- | --- | --- | ---
0 | 1 | 8 | 7 | 8 | 8 
1 | 8 | 8 | 7 | 49 | 49
1 | 8 | 7 | 3 | 18 | 49
1 | 8 | 6 | 8 | 40 | 49
1 | 8 | 5 | 4 | 16 | 49
1 | 8 | 4 | 5 | 15 | 49
1 | 8 | 3 | 2 | 4 | 49
1 | 8 | 2 | 6 | 6 | 49

```python
return max_area = 49
```

#### Time Complexity

- O(n) -> We transverse the array a single time.

#### Space Complexity

- O(1) -> We only create integer variables.
