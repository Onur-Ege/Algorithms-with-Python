"""
    Explanation of failure:

    coins: 8, 15, 3, 7

    player 1 picks 8
    player 2 picks 15
    player 1 picks 7
    player 2 picks 3

    player 1 total = 8 + 7 = 15
    player 2 total = 15 + 3 = 18

    If player 1 pick 7 instead of 8 in the first round, he would score 22 coins

"""


def greedy_algorithm(coins):

    player1_score = 0
    player2_score = 0

    for i in range(len(coins)):
        # compare first element and last element and choose bigger one
        bigger_one = coins.pop(0) if coins[0] >= coins[-1] else coins.pop(-1)
        # Since the first player starts the game, his turn number is always an even number.
        # in 0,2,4th execution of outer for loop player 1 choose a coin
        if i % 2 == 0:
            player1_score += bigger_one
        else:      # in 1,3,5th execution of outer for loop player 1 choose a coin
            player2_score += bigger_one

    return player1_score, player2_score


# initialize coins
list_of_coins = []
# take inputs
try:
    while True:
        a = input()
        # add inputs to the list
        list_of_coins.append(int(a))
except EOFError:
    pass

# pop first input item since it is not coins. it is number of coins
list_of_coins.pop(0)

# execute the algorithm and find greedy solution
score1, score2 = greedy_algorithm(list_of_coins)
# print the solution
print(f"Player 1's total score using greedy strategy: {score1}")
