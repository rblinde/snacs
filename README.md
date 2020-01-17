# SNACS
Checking accuracy of communtiy detection algorithms against ground truth.

## Method
For each pair of nodes, we check if they belong in the same community or not. We do this for both the grount truth and the results from the algorithm. If they match (both in the same community _or_ both different) we increment a `score` variable by 1. At the end we divide this by 1/2 * (N^2 - N), because:
- Checking all possible combinations: `N^2`
- Not checking against itself: `N^2 - N`
- Not checking duplicates: `0.5 * (N^2 - N)`

## Observations
- When accuracy is low, one giant component usually exists with other nodes having community size of one

## Todos
- [x] Create test case with small `n`
- [x] Create code for test case
- [x] Run code against first three datasets
- [ ] Run code against last two datasets

## Document
- [x] Rewrite Section 2.2
- [ ] Add table with number of found communities to Section 6.3
- [ ] Try to check why the results are so low in some cases
- [ ] Update Table 2 with new values
- [ ] Investigate observations
- [ ] Investigate runtime of BC algorithm
- [ ] Check if document is still valid after changes

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
```
