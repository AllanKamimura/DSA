# 151. Reverse Words In A String

[🔗 LeetCode Link](https://leetcode.com/problems/reverse-words-in-a-string/description/)

## Solution

### Remove extra spaces

#### Explanation

We need to remove leading, trailing and multiple spaces.

Removing the trailing spaces is the easiest,
we iterate over the array until we find the first non space character.
at the end of the first loop,
the index `i` is going to point to the first non space character.

To remove the multiple spaces, we create the write_to variable
to keep track of the last written index.

So we rewrite (move to the start) all non space values,
and rewrite the spaces only if the last written value is not a space.

To remove the trailing spaces,
we do a similar approach to the leading spaces.

### Double reversal

#### Explanation

When reversing the order of elements, the double reserve approach is used.

The first reversal is applied to the whole list,
with this all the words are going to be in the reversed order,
but the characters are backwards.

Then, we iterate over each word, and apply the reverse only to the word.
So that each word is correctly spelled.

Effectively, this is going to reverse the order of words.

### Two pointers approach

#### Explanation

Since we cleaned up the extra spaces, we know for sure that.
There is no leading or trailing spaces,
and there is only 1 space between words.

So we start 2 pointer, 
`first` to keep track of the start of word 
and `second` to look for the end of the word.

If either second finds an space of is at the end of the list,
we reverse the word using the first:second range.

#### Manual Run

```python
s = "  hello    world  "

# Remove spaces
i = 0, value = " "
i = 1, value = " "
i = 2, value = "h" -> start of the words

i = 2, value = "h", write_to = 0, string = "h hello    world  "
i = 3, value = "e", write_to = 1, string = "hehello    world  "
i = 4, value = "l", write_to = 2, string = "helello    world  "
i = 5, value = "l", write_to = 3, string = "hellllo    world  "
i = 6, value = "o", write_to = 4, string = "hellolo    world  "
i = 7, value = " ", write_to = 5, string = "hello o    world  " -> write space
i = 8, value = " ", write_to = 5, string = "hello o    world  "
i = 9, value = " ", write_to = 5, string = "hello o    world  "
i = 10, value = " ", write_to = 5, string = "hello o    world  "
i = 11, value = "w", write_to = 6, string = "hello w    world  "
i = 12, value = "o", write_to = 7, string = "hello wo   world  "
i = 13, value = "r", write_to = 8, string = "hello wor  world  "
i = 14, value = "l", write_to = 9, string = "hello worl world  "
i = 15, value = "d", write_to = 10, string = "hello world  world  "
i = 16, value = " ", write_to = 11, string = "hello world  world  "
i = 17, value = " ", write_to = 11, string = "hello world  world  "

end = 10, value = "d" -> break

string[: end + 1] = "hello world"
n = 11
s_list.reverse() = "dlrow olleh"

first = 0, second = 1, value2 = "l"
first = 0, second = 2, value2 = "r"
first = 0, second = 3, value2 = "o"
first = 0, second = 4, value2 = "w"
first = 0, second = 5, value2 = " " -> reverse
string = "world olleh"
first = 6, second = 6, value2 = "o"
first = 6, second = 7, value2 = "l"
first = 6, second = 8, value2 = "l"
first = 6, second = 9, value2 = "e"
first = 6, second = 10, value2 = "h"
first = 6, second = 11, value2 = ? -> reverse
string = "world hello"

We take advantage of the short-circuit or evaluation,
so s_list[second] is never evaluated when second == n
```

#### Time Complexity

- O(n) -> We transverse the array 2 time.

#### Space Complexity

- O(1) -> We only create integer variables.
  - The output array is used for inplace operations
