# 706. Design Hashmap

[🔗 LeetCode Link](https://leetcode.com/problems/design-hashmap/description/)

## Solution

### Hashmap

#### Explanation

So, the hashmap has 2 basic components, the hash and the map.

The map, in this case, is just a commonplace list,
in which we get values by index.

The hash is a method to generate unique index for each key.
Since all keys are numeric, we could direcly use these values as index.

But here we are going to use the hashing function followed by a modulo operator.

#### Time Complexity

- O(1) -> To put, retrieve and remove a value for the list is just a simple look-up.

#### Space Complexity

- O(n) -> We need to initialize an array big enought for all keys.
