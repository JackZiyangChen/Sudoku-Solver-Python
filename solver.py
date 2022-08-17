



board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

# board = [
#         [7, 8, 0],
#         [6, 0, 0],
#         [0, 0, 0]
# ]
#
# board = [
#     [4, 6, 7, 0, 0, 5, 0, 0, 0],
#     [0, 5, 0, 1, 0, 0, 7, 0, 0],
#     [0, 0, 0, 0, 4, 7, 0, 3, 6],
#     [9, 1, 0, 2, 0, 6, 0, 5, 0],
#     [0, 0, 8, 4, 0, 9, 3, 0, 0],
#     [0, 7, 0, 3, 0, 8, 0, 9, 2],
#     [7, 9, 0, 5, 8, 0, 0, 0, 0],
#     [0, 0, 2, 0, 0, 3, 0, 7, 0],
#     [0, 0, 0, 7, 0, 0, 1, 6, 9]
# ]

def get_solution():
    return solve_one_square(find_empty())

def is_valid(loc, num):
    '''
    :param loc: [i,j] where i,j represents board[i][j] (row, col)
    :param num: input number
    :return: a boolean representing whether or not the number can be entered
    '''
    row, col = loc
    # check row
    for j in range(len(board[row])):
        if j!=col and board[row][j]==num:
            return False

    # check col
    for i in range(len(board)):
        if i!=row and board[i][col]==num:
            return False

    # check big square
    big_row, big_col = row//3, col//3
    for i in range(big_row*3, big_row*3+3):
        for j in range(big_col*3, big_col*3+3):
            if i!=row and j!=col and board[i][j]==num:
                return False

    return True

def find_empty():
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return [i,j]
    return None

def solve_one_square(loc):
    if loc:
        row,col = loc
        find = False
        for i in range(1,10):
            print(f'{loc} - {i}')
            if is_valid(loc, i):
                board[row][col] = i
                if solve_one_square(find_empty()):
                    return True
        if find:
            return True
        else:
            board[row][col] = 0
            return False
    else:
        return True


if __name__=='__main__':
    print(get_solution())
    print(board)


