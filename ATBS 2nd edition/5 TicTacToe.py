# copied
# the one TicTacToe game with horrible controls and no conventional rules

the_board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
             'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
             'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def print_board(board):
    print(f"""{board['top-L']}|{board['top-M']}|{board['top-R']}
-+-+-
{board['mid-L']}|{board['mid-M']}|{board['mid-R']}
-+-+-
{board['low-L']}|{board['low-M']}|{board['low-R']}""")


turn = 'X'  # feel free to put your 'x' on your opponents 'o'
for i in range(9):
    print_board(the_board)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    the_board[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

print_board(the_board)
