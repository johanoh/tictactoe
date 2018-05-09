import random


def DrawBoard(board):

    print('   |   |')
    print(' ' + (board[6]) + ' | ' + board[7] + ' | ' + board[8])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('   |   |')


def start_game():
    while True:
        answer = input('Do you want to play tic-tac-toe [y/n]?')
        if answer == 'n':
            print('good bye!')
            break
        else:
            answer_1 = input('Do you want to play against AI [y/n]? ')
            if answer_1 == 'y':
                print("let's go!")
                playerOne_name = input('Input player 1 name: ')
                while True:
                    if tictactoe(playerOne_name, playerTwo_name='AI', ai=True):
                        break
            else:
                print("let's go!")
                playerOne_name = input('Input player 1 name: ')
                palyerTwo_name = input('Input player 2 name: ')
                while True:
                    if tictactoe(playerOne_name, palyerTwo_name, ai=False):
                        break


def tictactoe(playerOne_name, playerTwo_name, ai=None):
    board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    ai_move_set = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    DrawBoard(board)
    count = 0
    while True:
        if win_conditions(board):
            if (count % 2) != 0:
                print(playerOne_name + ' is the winner!')
            else:
                print(playerTwo_name + ' is the winner')
            return True
        if (count % 2) == 0:
            print(playerOne_name + "'s" + ' turn')
            move = int(input('Please input move! ')) - 1
            while True:
                if rules(board, move):
                    break
                else:
                    board[move] = 'X'
                    count += 1
                    DrawBoard(board)
                    break

        elif (count % 2) != 0:
            print(playerTwo_name + "'s" + ' turn')
            if ai is False:
                move = int(input('Please input move! ')) - 1
                while True:
                    if rules(board, move):
                        break
                    else:
                        board[move] = 'O'
                        count += 1
                        DrawBoard(board)
                        break
            else:
                print(ai_move_set)
                move = random.choice(ai_move_set) + 1
                while True:
                    if rules(board, move):
                        break
                    else:
                        board[move] = 'O'
                        count += 1
                        DrawBoard(board)
                        ai_move_set.remove(move - 1)
                        break


def win_conditions(board):
    if board[0] == board[1] == board[2]:
        print('winner!')
        return True
    elif board[3] == board[4] == board[5]:
        print('winner!')
        return True
    elif board[6] == board[7] == board[8]:
        print('winner!')
        return True
    elif board[0] == board[3] == board[6]:
        print('winner!')
        return True
    elif board[1] == board[4] == board[7]:
        print('winner!')
        return True
    elif board[2] == board[5] == board[8]:
        print('winner!')
        return True
    elif board[2] == board[4] == board[6]:
        print('winner!')
        return True
    elif board[0] == board[4] == board[8]:
        print('winner!')
        return True


def rules(board, move):
    try:
        if board[move] == 'X':
            print('Already Taken!')
            return True
        elif board[move] == 'O':
            print('Already Taken!')
            return True
        else:
            return False
    except(ValueError, IndexError):
        print('Not a A Valid Move!')
        return True


if __name__ == '__main__':
    start_game()