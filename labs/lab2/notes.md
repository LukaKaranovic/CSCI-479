# Lab2 - Discretization Methods

## Equal-width

- Each interval/bin should have the same range (using mean)
- Take (min + max) / (number of bins) for each interval

## Equal-depth

- Split values based on # of data items in each interval (using median)
- Each interval/bin should have roughly the same number of data items

## Information Based

- Split values into bins based on the % of items having the same target attribute
  - Ex. Find a threshold such that 80% below that threshold are in one category

- Find threshold, split into S1 and S2.
- Look at entropy of S1 and S2 target values

Inefficient Implementation:

- For each set S1, S2, do a count for number of items under each category

Efficient Implementation:

- Sort all data items based on the cotinuous attribute value
- Keep track of number of items under each category for S1 and S2
- Move threshold down a number: Update existing category counts by adding/subtracts (like a rolling count)


For threshold candidates:

- Choose every possible threshold value that will partition the dataset into two sets differently

