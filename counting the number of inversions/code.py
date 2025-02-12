# The algorithm leverages merge sort's divide-and-conquer strategy
# Inversions are counted during the merge step by comparing elements from two sorted sub arrays

# Time Complexity: O(n log n)
# Space Complexity: O(n)

# this function find number inversions recursively
def count_inversions(array, left, right):
    # Base case: if array or subarray have 1 or fewer elements
    if left >= right:
        return 0

    # find midpoint. we will use midpoint while dividing array
    midpoint = (left + right)//2

    # find the number of left and right inversion recursively
    number_of_left_inversions = count_inversions(array, left, midpoint)
    number_of_right_inversions = count_inversions(array, midpoint+1, right)

    # merge and find number of inversions across two subarray
    cross_inversions = count_and_merge_inversions(array, left, midpoint, right)

    # return number of total inversions
    return number_of_left_inversions + number_of_right_inversions + cross_inversions


# count and merge inversion across the sub arrays
def count_and_merge_inversions(array, left, midpoint, right):
    # temporary arrays
    left_subarray = array[left:midpoint+1]
    right_subarray = array[midpoint+1:right+1]

    i = 0               # index of left subarray
    j = 0               # index of right subarray
    k = left            # index of original subarray
    inversion = 0       # number of inversions

    while i < len(left_subarray) and j < len(right_subarray):
        # No inversion
        if left_subarray[i] <= right_subarray[j]:
            array[k] = left_subarray[i]
            i += 1
        # inversion is found
        else:
            array[k] = right_subarray[j]
            j += 1
            # Count inversions: remaining elements in left subarray are greater than current right subarray element
            inversion += len(left_subarray) - i

        k += 1

    # Copy remaining elements of left_subarray, if any
    while i < len(left_subarray):
        array[k] = left_subarray[i]
        i += 1
        k += 1

    # Copy remaining elements of right_subarray, if any
    while j < len(right_subarray):
        array[k] = right_subarray[j]
        j += 1
        k += 1

    # return the number of inversions
    return inversion


test_cases = [
    [1, 3, 5, 2, 4, 6],  # Mixed inversions
    [2, 4, 1, 3, 5],     # Multiple inversions
    [1, 2, 3, 4, 5, 6],     # No inversions (sorted)
    [6, 5, 4, 3, 2, 1]      # Maximum inversions (reverse sorted)
]

# Run test cases
for arr in test_cases:
    print(f"Array {arr}: Inversions = {count_inversions(arr, 0, len(arr) - 1)}")
