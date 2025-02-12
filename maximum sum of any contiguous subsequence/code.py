# this code finds maximum sum of contiguous subsequence using divide and conquer approach
# Time Complexity: O(n log n)
# Space Complexity: O(log n) due to recursive call stack

# find the maximum sum of subarray that crossing midpoint
def max_cross_sum(array, low, middle, high):
    # find maximum summation on left side
    left_side = float("-inf")
    summation = 0
    for i in range(middle, low - 1, -1):
        summation += array[i]
        left_side = max(summation, left_side)

    # find maximum summation on right side
    right_side = float("-inf")
    summation = 0
    for i in range(middle + 1, high + 1):
        summation += array[i]
        right_side = max(summation, right_side)

    # return sum of elements crossing midpoint
    return left_side + right_side


# recursively find maximum subarray sum
def max_sub_array_sum(array, low, high):
    if not array:
        return 0

    # Base case: if array have only one element
    if low == high:
        return array[high]

    # find the midpoint of array
    middle = (low + high)//2

    # recursively find max sum in three possible region
    return max(max_sub_array_sum(array, low, middle),
               max_sub_array_sum(array, middle+1, high),
               max_cross_sum(array, low, middle, high))


# Example inputs
arr1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
arr2 = [1, 2, 3, 4, 5]
arr3 = [-1, -2, -3, -4, -5]

# result of inputs
result1 = max_sub_array_sum(arr1, 0, len(arr1)-1)
result2 = max_sub_array_sum(arr2, 0, len(arr2)-1)
result3 = max_sub_array_sum(arr3, 0, len(arr3)-1)

print(f"The maximum sum of any contiguous subsequence for arr1 is: {result1}")
print(f"The maximum sum of any contiguous subsequence for arr2 is: {result2}")
print(f"The maximum sum of any contiguous subsequence for arr3 is: {result3}")