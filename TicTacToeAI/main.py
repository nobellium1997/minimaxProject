from operator import itemgetter


def game():
    board = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]

    humanPlayer = "X"
    aiPlayer = "O"

    while True:
        draw(board)
        humanMoveRow = int(input("Enter row number: "))
        humanMoveCol = int(input("Enter col number: "))

        rank = humanMoveRow * 3 + humanMoveCol

        if rank > 8 or board[rank] == "X" or board[rank] == "O":
            print("invalid input try again")
            continue

        board[rank] = "X"

        aiMove = minimax(board, aiPlayer)[0]
        board[aiMove] = "O"

        if winning(board, humanPlayer):
            draw(board)
            print("WINNER YAY")
            break
        elif winning(board, aiPlayer):
            draw(board)
            print("lmao idiot you lost")
            break
        elif len(emptySpaces(board)) == 0:
            draw(board)
            print("it is a tie")
            break


def minimax(newBoard, player):
    availSpots = emptySpaces(newBoard)

    if winning(newBoard, "X"):
        return 0, -10
    elif winning(newBoard, "O"):
        return 0, 10
    elif len(availSpots) == 0:
        return 0, 0

    availMoves = []

    for i in availSpots:
        moveIndex = int(i)

        newBoard[moveIndex] = player

        if player == "O":
            score = minimax(newBoard, "X")[1]
            availMoves.append((moveIndex, score))
        elif player == "X":
            score = minimax(newBoard, "O")[1]
            availMoves.append((moveIndex, score))

        newBoard[moveIndex] = moveIndex

    if player == "X":
        return min(availMoves, key=itemgetter(1))
    elif player == "O":
        return max(availMoves, key=itemgetter(1))


def draw(board):
    print("\t", end="")

    for i in range(3):
        print(i, "\t\t", end="")
    print()

    counter = 0
    for i in range(3):
        print(i, "\t", end="")
        for j in range(3):
            if board[counter] == "X" or board[counter] == "O":
                print(board[counter], "\t|\t", end="")
            else:
                print(" \t|\t", end="")
            counter += 1
        print()
        if i != 2:
            print("\t---------------------------------------------")


def winning(board, player):
    if (board[0] == player and board[1] == player and board[2] == player or
            board[3] == player and board[4] == player and board[5] == player or
            board[6] == player and board[7] == player and board[8] == player or
            board[0] == player and board[3] == player and board[6] == player or
            board[1] == player and board[4] == player and board[7] == player or
            board[2] == player and board[5] == player and board[8] == player or
            board[0] == player and board[4] == player and board[8] == player or
            board[2] == player and board[4] == player and board[6] == player):
        return True
    else:
        return False


def emptySpaces(board):
    return list(filter(lambda elem: (elem != "X" and elem != "O"), board))


if __name__ == '__main__':
    game()
