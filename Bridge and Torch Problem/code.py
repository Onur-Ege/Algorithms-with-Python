"""
    The algorithm uses dynamic programming to minimize bridge crossing time by considering two strategies:
    pairing the fastest or the slowest with others,
    choosing the minimum at each step, and storing results for reuse.

    Analysis:
    Time complexity: O(n)
    Space complexity: O(n)
"""


def min_time(times):
    # length of array
    length = len(times)

    # when we have small group
    if length <= 2:
        return times[length - 1]

    # Initialize the Dynamic programming table
    table_dp = [0] * (length + 1)

    # Base cases
    table_dp[1] = times[0]  # Only one person crosses
    table_dp[2] = times[1]  # Two people cross together

    # Fill the Dynamic programming table
    for i in range(3, length + 1):
        # 2 situation:
        # 1. Fastest two cross, fastest returns, two slowest cross, second fastest returns
        st1 = table_dp[i - 2] + times[1] + times[0] + times[i - 1] + times[1]

        # 2. Fastest and slowest cross, fastest returns, next two slowest cross, fastest returns
        st2 = table_dp[i - 2] + times[i - 1] + times[0] + times[i - 2] + times[0]

        # select min time required situation
        table_dp[i] = min(st1, st2)

    return table_dp[length]


def main():
    # initialize list
    times_list = []
    try:
        while True:
            # take inputs
            line = input()
            # add inputs to the list
            for a in line.split():
                times_list.append(int(a))
    except EOFError:
        pass

    # execute the algorithm and find result
    result = min_time(times_list)
    # print result
    print(f"Minimum total time required: {result}")


if __name__ == "__main__":
    main()