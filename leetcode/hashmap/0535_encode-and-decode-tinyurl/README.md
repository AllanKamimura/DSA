# 535. Encode And Decode Tinyurl

[🔗 LeetCode Link](https://leetcode.com/problems/encode-and-decode-tinyurl/description/)

## Solution

### Hashmap

#### Explanation

The first thing we need to think is how many links are we expecting.
This impacts the 2 main variables.

1. Charset
2. Number of characters

Using only letters and numbers, we have 62 possibilities for each digit.
In another words, we can enconde 62 ^ n links.

n | links
-- | --
1 | 62
2 | 3844
3 | 238328
4 | 14776336
5 | 916132832
6 | 56800235584

So with 6 digits we should be able to encode around 56B links.

To get our 6 digits number:

1. Go in order, this is basically a 62 base number
2. Just get in by random

Then use this 6 digits as a key in a Hashmap and the real url as value

#### Time Complexity

- O(1) -> Hashmap lookup

#### Space Complexity

- O(1) -> The size of the hashmap is contant, given `n` and charset.
