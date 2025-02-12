"""
    Determine the maximum possible amount of money a player can guarantee to win.

    Time Complexity:  𝑂(𝑛^2)
    Space Complexity: O(𝑛^2)
"""


def collect_max(coins):
    a = len(coins)

    # Create a 2D DP table where dp[i][j] represents the max coin a player can collect
    dp = [[0] * a for _ in range(a)]

    # Fill the table for subproblems of size 1 (single coin)
    for i in range(a):
        dp[i][i] = coins[i]

    # Fill the table for subproblems of increasing size
    for length in range(2, a + 1):  # length is the size of the subproblem
        for i in range(a - length + 1):
            j = i + length - 1  # Ending index of the subproblem

            x = 0
            if i + 2 <= j:
                x = dp[i + 2][j]

            y = 0
            if i + 1 <= j - 1:
                y = dp[i + 1][j - 1]

            z = 0
            if i <= j - 2:
                z = dp[i][j - 2]

            # If the player takes the ith coin:
            pick_i = coins[i] + min(
                x,  # other player takes (i+1)
                y   # other player takes (j)
            )

            # If the player takes the jth coin:
            pick_j = coins[j] + min(
                z,  # other player takes (j-1)
                y   # other player takes (i)
            )

            # Take the max of both situations
            dp[i][j] = max(pick_i, pick_j)

    # The result for the entire row of coins is stored in dp[0][n-1]
    return dp[0][a - 1]


def main():
    # initialize coins
    list_of_coins = []
    try:
        while True:
            # take inputs
            a = input()
            # add inputs to the list
            list_of_coins.append(int(a))
    except EOFError:
        pass
        
    # pop first input item since it is not coins. it is number of coins
    list_of_coins.pop(0)

    # find the maximum amount of coin the first player can collect
    score = collect_max(list_of_coins)

    # Output the result
    print(f"Maximum amount of Player 1: {score}")


if __name__ == "__main__":
    main()
