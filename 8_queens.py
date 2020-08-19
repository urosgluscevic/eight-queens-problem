board = []

queens = int(input("How many queens? "))

#creates an empty n by n chess board
for i in range(queens):
    new_row = []
    for j in range(queens):
        new_row.append(0)
    board.append(new_row)

#finds all fields when a queen can be placed
def find_empty(board):
    empty = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                empty.append((i, j))
    return empty


#   Adds or removes a queen from the board. 
#   A queen is marked with "*". 
#   An occupied field is marked by a number larger than 0 
def fill(board, row, col, set_to):
    for i in range(queens):
        if board[row][i] != "*":
            board[row][i] += set_to
        if board[i][col] != "*":
            board[i][col] += set_to

    row_iter = row
    col_iter = col

    while row_iter > 0 and col_iter > 0:
        row_iter -= 1
        col_iter -= 1

        board[row_iter][col_iter] += set_to

    row_iter = row
    col_iter = col

    while row_iter > 0 and col_iter < queens - 1:
        row_iter -= 1
        col_iter += 1

        board[row_iter][col_iter] += set_to

    row_iter = row
    col_iter = col

    while row_iter < queens - 1 and col_iter > 0:
        row_iter += 1
        col_iter -= 1

        board[row_iter][col_iter] += set_to
        
    row_iter = row
    col_iter = col

    while row_iter < queens - 1 and col_iter < queens - 1:
        row_iter += 1
        col_iter += 1

        board[row_iter][col_iter] += set_to

    if set_to == 1:
        board[row][col] = "*"
    else:
        board[row][col] = 0
            

#   recursive function that tries to place all n queens on the board '''
def solve(board, queens_to_place):
    if queens_to_place == 0:
        return True
    
    coordinates = find_empty(board)

    if not coordinates:
        return False

    for i in range(len(coordinates)):

        row, col = coordinates[i]
        fill(board, row, col, 1)


        if solve(board, queens_to_place - 1):
            return True

        fill(board, row, col, -1)

    return False

solve(board, queens)

#prints the board
for row in board:
    for i in range(len(row)):
        if row[i] != "*":
            row[i] = "_"
    print(row)