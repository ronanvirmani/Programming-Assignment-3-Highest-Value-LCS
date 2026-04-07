# Coding Assignment 3

Ronan Virmani
28617437

## Requirements

- Python 3
- matplotlib (needed for graphing)

## How to Run

```bash
python3 src/highest_value_lcs.py < data/input/example1.in
```

Expected output is in `data/output/example1.out`.

## Generate Runtime Graph

```bash
pip install matplotlib
python3 src/graph.py
```

## Input Format

```
K
x1 v1
x2 v2
...
xK vK
A
B
```

## Output Format

```
<max_value>
<subsequence>
```
## Questions

# 1. Runtime Analysis

![Runtime Graph](runtime_graph.png)

# 2. Recurrence Equation

`dp[i][j]` = max value of a common subsequence of first i chars from A and first j chars from B.

**BC**
```
dp[0][j] = 0  for all j
dp[i][0] = 0  for all i
```
If we have no characters the max subsequence value is 0.

**Recurrence Eq:**
```
dp[i][j] = dp[i-1][j-1] + v(A[i])       if A[i] == B[j]
dp[i][j] = max(dp[i-1][j], dp[i][j-1])  otherwise
```

**Why this is correct:**
- The top case when `A[i] == B[j]`, we can add the best common subsequence of `A[1..i-1]` and `B[1..j-1]` by adding this matching character, we get its value `v(A[i])`.
- Otherwise when `A[i] != B[j]`, the characters can't both be used. We take the max of from either not having `A[i]` using `dp[i-1][j]` or not having `B[j]` using `dp[i][j-1]`.

# 3. Big-Oh

```
HVLCS(A, B, v):
    m = len(A)
    n = len(B)

    dp[0..m][0..n] = 0

    for i = 1 to m:
        for j = 1 to n:
            if A[i] == B[j]:
                dp[i][j] = dp[i-1][j-1] + v(A[i])
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]
```

- We fill an `m × n` table
- O(m * n) time complexity