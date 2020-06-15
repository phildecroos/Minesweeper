import random

board = [
    ["", "", "", "", "", "", "", "", "", "", ""],
    [" ", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", ""],
    [" ", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", ""],
    [" ", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", ""],
    [" ", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", ""],
    [" ", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", ""],
    [" ", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", ""],
    [" ", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", ""],
    [" ", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", ""],
    [" ", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", ""],
    [" ", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", ""],
    ["", "", "", "", "", "", "", "", "", "", ""]
]

cells = [
    [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9],
    [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9],
    [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6], [3, 7], [3, 8], [3, 9],
    [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7], [4, 8], [4, 9],
    [5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9],
    [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6], [6, 7], [6, 8], [6, 9],
    [7, 1], [7, 2], [7, 3], [7, 4], [7, 5], [7, 6], [7, 7], [7, 8], [7, 9],
    [8, 1], [8, 2], [8, 3], [8, 4], [8, 5], [8, 6], [8, 7], [8, 8], [8, 9],
    [9, 1], [9, 2], [9, 3], [9, 4], [9, 5], [9, 6], [9, 7], [9, 8], [9, 9],
]

mines = [random.choice(cells), random.choice(cells), random.choice(cells), random.choice(cells), random.choice(cells),
         random.choice(cells), random.choice(cells), random.choice(cells), random.choice(cells), random.choice(cells)]


def show_board():
    print("   1  2  3  4  5  6  7  8  9")
    print(" 1" + board[1][1] + board[1][2] + board[1][3] + board[1][4] + board[1][5] + board[1][6] + board[1][7] +
          board[1][8] + board[1][9])
    print(" 2" + board[2][1] + board[2][2] + board[2][3] + board[2][4] + board[2][5] + board[2][6] + board[2][7] +
          board[2][8] + board[2][9])
    print(" 3" + board[3][1] + board[3][2] + board[3][3] + board[3][4] + board[3][5] + board[3][6] + board[3][7] +
          board[3][8] + board[3][9])
    print(" 4" + board[4][1] + board[4][2] + board[4][3] + board[4][4] + board[4][5] + board[4][6] + board[4][7] +
          board[4][8] + board[4][9])
    print(" 5" + board[5][1] + board[5][2] + board[5][3] + board[5][4] + board[5][5] + board[5][6] + board[5][7] +
          board[5][8] + board[5][9])
    print(" 6" + board[6][1] + board[6][2] + board[6][3] + board[6][4] + board[6][5] + board[6][6] + board[6][7] +
          board[6][8] + board[6][9])
    print(" 7" + board[7][1] + board[7][2] + board[7][3] + board[7][4] + board[7][5] + board[7][6] + board[7][7] +
          board[7][8] + board[7][9])
    print(" 8" + board[8][1] + board[8][2] + board[8][3] + board[8][4] + board[8][5] + board[8][6] + board[8][7] +
          board[8][8] + board[8][9])
    print(" 9" + board[9][1] + board[9][2] + board[9][3] + board[9][4] + board[9][5] + board[9][6] + board[9][7] +
          board[9][8] + board[9][9])


def exists(exists_yx):
    y = exists_yx[0]
    x = exists_yx[1]
    if y in range(1, 10) and x in range(1, 10):
        return True
    else:
        return False


def near_mines(near_mines_yx):
    num = 0
    y = near_mines_yx[0]
    x = near_mines_yx[1]

    a = [y - 1, x - 1]
    b = [y - 1, x]
    c = [y - 1, x + 1]
    d = [y, x - 1]
    e = [y, x + 1]
    f = [y + 1, x - 1]
    g = [y + 1, x]
    h = [y + 1, x + 1]

    if a in mines:
        num += 1
    if b in mines:
        num += 1
    if c in mines:
        num += 1
    if d in mines:
        num += 1
    if e in mines:
        num += 1
    if f in mines:
        num += 1
    if g in mines:
        num += 1
    if h in mines:
        num += 1
    board[y][x] = "[" + str(num) + "]"


def clear_near(clear_near_yx):
    y = clear_near_yx[0]
    x = clear_near_yx[1]

    a = [y - 1, x - 1]
    b = [y - 1, x]
    c = [y - 1, x + 1]
    d = [y, x - 1]
    e = [y, x + 1]
    f = [y + 1, x - 1]
    g = [y + 1, x]
    h = [y + 1, x + 1]

    cell_a = board[a[0]][a[1]]
    cell_b = board[b[0]][b[1]]
    cell_c = board[c[0]][c[1]]
    cell_d = board[d[0]][d[1]]
    cell_e = board[e[0]][e[1]]
    cell_f = board[f[0]][f[1]]
    cell_g = board[g[0]][g[1]]
    cell_h = board[h[0]][h[1]]

    if board[y][x] == "[0]":
        # yes, this could be done with less code if i made lists of the cells and co-ordinates and used for loops
        if a not in mines and cell_a == "[ ]":
            near_mines(a)
            if exists(a):
                clear_near(a)
        if b not in mines and cell_b == "[ ]":
            near_mines(b)
            if exists(b):
                clear_near(b)
        if c not in mines and cell_c == "[ ]":
            near_mines(c)
            if exists(c):
                clear_near(c)
        if d not in mines and cell_d == "[ ]":
            near_mines(d)
            if exists(d):
                clear_near(d)
        if e not in mines and cell_e == "[ ]":
            near_mines(e)
            if exists(e):
                clear_near(e)
        if f not in mines and cell_f == "[ ]":
            near_mines(f)
            if exists(f):
                clear_near(f)
        if g not in mines and cell_g == "[ ]":
            near_mines(g)
            if exists(g):
                clear_near(g)
        if h not in mines and cell_h == "[ ]":
            near_mines(h)
            if exists(h):
                clear_near(h)


def good_input(test_input):
    if len(test_input) != 8 and len(test_input) != 4:
        return False
    bad_input = 0
    if not test_input[0:2].isdigit():
        bad_input += 1
    if not test_input[2] == " ":
        bad_input += 1
    if len(test_input) == 8:
        if test_input[3:8] != "sweep":
            bad_input += 1
    if len(test_input) == 4:
        if test_input[3] != "!":
            bad_input += 1
    if bad_input != 0:
        return False
    else:
        return True


print("\n***Tutorial***\nHere is the minefield, there are about 10 mines.\nTo do an action, enter the co-ordinates of "
      "the square you want and the action you would like to do.\nActions:\n   Flag or unflag a square as a mine -> '!'"
      "\n   Sweep a square -> 'sweep'\nNote: You must format your action exactly like this -> '12 sweep'\n(do not type "
      "the quotation marks)\nThe co-ordinates are across then down.\nYou win when you have flagged all of the mines.\n"
      "You lose if you sweep a square that has a mine on it\n ")
show_board()

while True:
    user_input = input("\nDo an action: ")
    if good_input(user_input):
        input_yx = [int(user_input[1]), int(user_input[0])]
        if user_input[3:] == "sweep":
            if input_yx in mines:
                board[input_yx[0]][input_yx[1]] = "[X]"
                show_board()
                print("KABOOM! You lost.")
                break
            else:
                near_mines(input_yx)
                clear_near(input_yx)
        elif user_input[3] == "!":
            if board[input_yx[0]][input_yx[1]] == "[!]":
                board[input_yx[0]][input_yx[1]] = "[ ]"
            else:
                board[input_yx[0]][input_yx[1]] = "[!]"

        stop_var = 0
        for x in mines:
            if board[x[0]][x[1]] == "[!]":
                stop_var += 1
        if stop_var == len(mines):
            show_board()
            print("Congrats! You won!")
            break

        show_board()
    else:
        print("Invalid input, please try again with the correct formatting.")
