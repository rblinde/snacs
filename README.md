# SNACS

Checking accuracy of communtiy detection algorithms against ground truth.

## Method

For each pair of nodes, we check if they belong in the same community or not. We do this for both the grount truth and the results from the algorithm. If they match (both in the same community _or_ both different) we increment a `score` variable by 1. At the end we divide this by 1/2 \* (N^2 - N), because:

- Checking all possible combinations: `N^2`
- Not checking against itself: `N^2 - N`
- Not checking duplicates: `0.5 * (N^2 - N)`

## Observations

- When accuracy is low, one giant component usually exists with other nodes having community size of one

## Todos

- [x] Create test case with small `n`
- [x] Create code for test case
- [x] Run code against first three datasets
- [x] Run code against last two datasets

## Document

- [x] Rewrite Section 2.2
- [x] Add table with number of found communities to Section 6.3
- [x] Try to check why the results are so low in some cases
- [x] Update Table 2 with new values
- [x] Investigate observations
- [x] Investigate runtime of BC algorithm
- [x] Check if document is still valid after changes

## Results

```
Accuracy of 'gm' for 'karate': 0.5811
Accuracy of 'gn' for 'karate': 0.5989
Accuracy of 'lpa' for 'karate': 0.6062
Accuracy of 'gm' for 'football': 0.8807
Accuracy of 'gn' for 'football': 0.5732
Accuracy of 'lpa' for 'football': 0.9548
Accuracy of 'gm' for 'email': 0.7683
Accuracy of 'gn' for 'email': 0.0903
Accuracy of 'lpa' for 'email': 0.1380
Accuracy of 'gm' for 'corporate-small': 0.5619
Accuracy of 'gn' for 'corporate-small': 0.1909
Accuracy of 'lpa' for 'corporate-small': 0.5745
Accuracy of 'gm' for 'corporate': 0.91
Accuracy of 'gn' for 'corporate': N/A
Accuracy of 'lpa' for 'corporate': 0.94
```

## Timings

```
Time for lpa on karate: 3.6972 ms
Time for gm on karate: 6.2677 ms
Time for gn on karate: 97.7469 ms
Time for lpa on football: 16.3861 ms
Time for gm on football: 37.1652 ms
Time for gn on football: 5947.0303 ms
Time for lpa on email: 508.3436 ms
Time for gm on email: 3003.0500 ms
Time for gn on email: 146602.3483 ms
Time for lpa on corporate-small: 324.1587 ms
Time for gm on corporate-small: 856.9652 ms
Time for gn on corporate-small: 9306.9723 ms
Time for lpa on corporate: 129840.7383 ms
Time for gm on corporate: 17199643.7194 ms
Time for gn on corporate: N/A
```
