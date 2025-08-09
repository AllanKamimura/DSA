# 1603. Design Parking System

[🔗 LeetCode Link](https://leetcode.com/problems/design-parking-system/description/)

## Solution

### Hashmap

#### Explanation

Use a hashmap,
with the type of parking slot as key
and current empty spaces as values.

When adding a new car,
check if the current empty spaces is not zero.

#### Manual Run

```python
["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
[[1, 1, 0], [1], [2], [3], [1]]
```

empty_spaces | addCar | can_park
{1: 1, 2: 1, 3: 0} | 1 | True
{1: 0, 2: 1, 3: 0} | 2 | True
{1: 0, 2: 0, 3: 0} | 3 | False
{1: 0, 2: 0, 3: 0} | 1 | False

#### Time Complexity

- O(1) -> Get a value from a hashmap.

#### Space Complexity

- O(1) -> The number of elements in the hashmap is the number of unique parking types.
