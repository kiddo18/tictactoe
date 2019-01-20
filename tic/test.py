def isWinner(bo, le):
# Given a board and a player’s letter, this function returns True if that player has won.
# We use bo instead of board and le instead of letter so we don’t have to type as much.
    return ((bo[0][0] == le and bo[0][1] == le and bo[0][2] == le) or (bo[1][0] == le and bo[1][1] == le and bo[1][2] == le) or (bo[2][0] == le and bo[2][1] == le and bo[2][2] == le) or (bo[0][0] == le and bo[1][0] == le and bo[2][0] == le) or (bo[0][1] == le and bo[1][1] == le and bo[2][1] == le) or (bo[0][2] == le and bo[1][2] == le and bo[2][2] == le) or (bo[0][0] == le and bo[1][1] == le and bo[2][2] == le) or (bo[0][2] == le and bo[1][1] == le and bo[2][0] == le))


board = [[None, None, None], [None, None, None], [None, None, None]]
print(isWinner(board, "X"))