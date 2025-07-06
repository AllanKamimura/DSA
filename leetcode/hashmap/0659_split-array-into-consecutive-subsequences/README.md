# 659. Split Array Into Consecutive Subsequences

[🔗 LeetCode Link](https://leetcode.com/problems/split-array-into-consecutive-subsequences/description/)

## Solution

### Counter + Hashmap

#### Explanation

First, we count the number of occurences of each number in a counter.
This is going to keep track of how much of each number we can "spend".

We then create a second dictionary,
to keep track of how many subsequences ends at each number,
this is going to be used to extend the sequence in the next iteration.

So we create 2 main logics:

1. Extend an existing sequence
2. Start a new sequence (using 2 future numbers)
3. If both fails, then we can't split the array into subsequences

One important thing to note is that:
extending an existing sequence takes precedence over starting a new sequence.

This is because starting a new sequence is "more expensive",
since it spends 3 numbers at once,
in another words,
we only create a new sequence when needed.

Also, since we are going to be "spending ahead",
some numbers are spent before we reach them,
so we should just skip past.

#### Manual Run

```python
nums = [1,2,3,3,4,5,5,6,7]
count = Counter({1:1, 2:1, 3:2, 4:1, 5:2, 6:1, 7:1})
end_at = defaultdict({1: 0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0})
```

num | decision | count | end_at
-- | -- | -- | --
1 | new | {1:0, 2:0, 3:1, 4:1, 5:2, 6:1, 7:1} | {1: 0, 2:0, 3:1, 4:0, 5:0, 6:0, 7:0}
2 | skip | {1:0, 2:0, 3:1, 4:1, 5:2, 6:1, 7:1} | {1: 0, 2:0, 3:1, 4:0, 5:0, 6:0, 7:0}
3 | new | {1:0, 2:0, 3:0, 4:0, 5:1, 6:1, 7:1} | {1: 0, 2:0, 3:1, 4:0, 5:1, 6:0, 7:0}
3 | skip | {1:0, 2:0, 3:0, 4:0, 5:1, 6:1, 7:1} | {1: 0, 2:0, 3:1, 4:0, 5:1, 6:0, 7:0}
4 | skip | {1:0, 2:0, 3:0, 4:0, 5:1, 6:1, 7:1} | {1: 0, 2:0, 3:1, 4:0, 5:1, 6:0, 7:0}
5 | new | {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0} | {1: 0, 2:0, 3:1, 4:0, 5:1, 6:0, 7:1}
5 | skip | {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0} | {1: 0, 2:0, 3:1, 4:0, 5:1, 6:0, 7:1}
6 | skip | {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0} | {1: 0, 2:0, 3:1, 4:0, 5:1, 6:0, 7:1}
7 | skip | {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0} | {1: 0, 2:0, 3:1, 4:0, 5:1, 6:0, 7:1}

```python
return True
```

#### Time Complexity

- O(n) -> We transverse the array a single time.

#### Space Complexity

- O(n) -> In the worst case, Counter and end_at has n elemements.

### Heap

#### Explanation

First, we create a dictionary,
to keep track of the length of the subsequences that ends at each number,
the sequence can be extend in future iterations.

So we create 2 main logics:

1. Extend an existing sequence
2. Start a new sequence (without the look-ahead)

One important thing to note is that:
extending an existing sequence takes precedence over starting a new sequence.

This is because starting a new sequence is "more expensive",
since it spends 3 numbers at once,
in another words,
we only create a new sequence when needed.

Since we don't have the look ahead,
We are going to be creating "false" subsequences,
that is, subsequences with less than 3 number.
And we need a logic to prioritize filling those
before the larger sequences.

For this, we use a min-heap with the lengths of sequences,
and always take the shorter sequence.

#### Manual Run

```python
nums = [1,2,3,3,4,5,5,6,7]
end_at = defaultdict({1: [], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[]})
```

num | decision | count | end_at
-- | -- | -- | --
1 | new    | {1: [1], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[]}
2 | extend | {1: [], 2:[2], 3:[], 4:[], 5:[], 6:[], 7:[]}
3 | extend | {1: [], 2:[], 3:[3], 4:[], 5:[], 6:[], 7:[]}
3 | new    | {1: [], 2:[], 3:[1,3], 4:[], 5:[], 6:[], 7:[]}
4 | extend | {1: [], 2:[], 3:[3], 4:[2], 5:[], 6:[], 7:[]}
5 | extend | {1: [], 2:[], 3:[3], 4:[], 5:[3], 6:[], 7:[]}
5 | new    | {1: [], 2:[], 3:[3], 4:[], 5:[1,3], 6:[], 7:[]}
6 | extend | {1: [], 2:[], 3:[3], 4:[], 5:[3], 6:[2], 7:[]}
7 | extend | {1: [], 2:[], 3:[3], 4:[], 5:[3], 6:[], 7:[3]}

```python
all heap[0] >= 3:
return True
```

#### Time Complexity

- O(n * log(k))
  - O(n * log(k)): We transverse the array a single time, each time we heapify (size=num_sequences)
  - O(n): We transverse the heaps dict to check the length

#### Space Complexity

- O(n) -> In the worst case, end_at has n elemements.
