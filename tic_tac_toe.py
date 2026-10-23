import random
board = [1, 2, 3, 4, 'X', 6, 7, 8, 9,]
def display_board(board):
    print("+-------+-------+-------+")
    print("|       |       |        |")
    print(f"|    {board[0]}  |   {board[1]}   |  {board[2]}    |")
    print("|       |       |        |")
    print("+2-------+-------+--------+")
    print("|       |       |        |")
    print(f"|    {board[3]}  |   {board[4]}   |  {board[5]}    |")
    print("|       |       |        |")
    print("+-------+-------+-------+")
    print("|       |       |        |")
    print(f"|    {board[6]}  |   {board[7]}   |  {board[8]}    |")
    print("|       |       |        |")
    print("+-------+-------+-------+}")
display_board(board)
def enter_move(board):
    while True:
        move = input("Сделайте ход (введите номер клетки от 1 до 9.): ")

        if not move.isdigit():
            print("Ошибка! Введите именно число от 1 до 9.")
            continue 

        move = int(move)

        if move <1 or move >9:
            print("ошибка! Число должно быть от 1 до 9. ")
            continue

        index = move - 1

        if board[index] in ['X', '0']:
            print("Эта кклетка уже занята! Выибирите свободную.")
            continue
        board[index] = 'O'
        break   
def make_computer_move(board):

    free_cells = [i for i in range(9) if board[i] not in ['X','O' ]]
    if free_cells:
        random_index = random.choice(free_cells)
        board[random_index] = 'X'

def check_victory(board, sign):
    win_coord = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
    ]
    for each in win_coord:
        if board[each[0]] == sign and board[each[1]] == sign and board[each[2]] == sign:
            return sign
    return False 
display_board(board)

while True:
    enter_move(board)
    display_board(board)

    if check_victory(board, 'O'):
        print("Поздравляем, вы выиграли!")
        break

    if all(isinstance(x, str) for x in board):
        print("Ничья!")
        break

    print("Ход копьютера...")
    make_computer_move(board)
    display_board(board)

    if check_victory(board, 'X'):
        print("Копьютер выиграл!")
        break
    if all(isinstance(x, str) for x in board):
        print("Ничья!")
        break