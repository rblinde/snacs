# SNACS
Checking accuracy of communtiy detection algorithms against ground truth.

## Method
For each pair of nodes, we check if they belong in the same community or not. We do this for both the grount truth and the results from the algorithm. If they match (both in the same community _or_ both different) we increment a `score` variable by 1. At the end we divide this by 1/2 * (N^2 - N), because:
- Checking all possible combinations: `N^2`
- Not checking against itself: `N^2 - N`
- Not checking duplicates: `0.5 * (N^2 - N)`

# Todos
[x] Create test case with small `n`
[x] Create code for test case
[x] Run code against first three datasets
[ ] Run code against last two datasets

# Document
Add todos for LaTeX document