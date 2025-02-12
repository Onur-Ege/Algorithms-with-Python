def min_time(boards, k):
    """
    Employing dynamic programming, determine the shortest duration necessary to paint all the boards with a team of k painters.

    The algorithm uses dynamic programming to minimize the maximum time a painter spends.
    It calculates the best way to divide boards among painters, using a table to store results.
    The solution is found by trying all possible ways to split the boards and taking the minimum time.

    Time Complexity = O(n*n*k)
    Space Complexity = O(n*k)
    """
    length = len(boards)

    # Create a dynamic programming table to store the minimum time required
    dp_table = [[float('inf')] * (k + 1) for _ in range(length + 1)]

    # Prefix sum array to calculate sum of boards easily
    pre_sum = [0] * (length + 1)
    i = 1
    # Precompute the prefix sum for efficient board segment sums calculation
    while i <= length:
        pre_sum[i] = pre_sum[i - 1] + boards[i - 1]
        i += 1

    # Base case: If there is only one painter, the sum of the first i boards is the time
    i = 1
    while i <= length:
        dp_table[i][1] = pre_sum[i]
        i += 1

    # Filling the Dynamic programming table for several painters (from 2 to k)
    i = 1
    while i <= length:
        j = 2
        # Iterate over the number of painters (from 2 to k)
        while j <= k:
            p = 1
            # Iterate over possible split points (p represents the split between the painters)
            while p <= i:

                a = dp_table[i][j]          # Current value in dp_table[i][j]
                b = dp_table[p][j - 1]      # Previous painter's result
                c = pre_sum[i] - pre_sum[p] # Time required for the current painter to paint their boards

                # Calculate the minimum time by considering the worst-case scenario (maximum time for a painter)
                dp_table[i][j] = min(a, max(b, c))

                p += 1
            j += 1
        i += 1

    return dp_table[length][k]


def main():
    # initialize list
    boards = []
    try:
        while True:
            # take inputs
            line = input()
            # add inputs to the list
            for a in line.split():
                boards.append(int(a))
    except EOFError:
        pass

    k = boards[-1]
    n = len(boards)
    boards = boards[0:n]

    # execute the algorithm and find result
    result = min_time(boards, k)
    print(f"Minimum time required: {result}")


if __name__ == "__main__":
    main()
