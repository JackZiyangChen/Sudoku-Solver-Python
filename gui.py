import pygame
import time
pygame.font.init()


class Board:
    class Square:

        def __init__(self, val, row, col, width, height):
            self.value = val
            self.row = row
            self.col = col
            self.width = width
            self.height = height

            self.selected = False

        def draw(self, win, anchor):
            fnt = pygame.font.SysFont("comicsans", 40)
            ax, ay = anchor

            gap = self.width / 9
            x = self.col * gap
            y = self.row * gap

            if self.temp != 0 and self.value == 0:
                text = fnt.render(str(self.temp), 1, (128, 128, 128))
                win.blit(text, (x + 5, y + 5))
            elif not (self.value == 0):
                text = fnt.render(str(self.value), 1, (0, 0, 0))
                win.blit(text, (x + (gap / 2 - text.get_width() / 2), y + (gap / 2 - text.get_height() / 2)))

            if self.selected:
                pygame.draw.rect(win, (255, 0, 0), (x, y, gap, gap), 3)



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

    def __init__(self, rows, cols, width, height, win, anchor):
        self.posx, self.posy = anchor
        self.rows = rows
        self.cols = cols
        # self.cubes = [[Cube(self.board[i][j], i, j, width, height) for j in range(cols)] for i in range(rows)]
        self.width = width
        self.height = height
        self.model = None
        # self.update_model()
        self.selected = None
        self.win = win

        self.squares = [[self.Square(self.board[i][j], i, j, width, height) for j in range(cols)] for i in range(rows)]

    def get_solution(self):
        return self.solve_one_square(self.find_empty())

    def is_valid(self, loc, num):
        '''
        :param loc: [i,j] where i,j represents board[i][j] (row, col)
        :param num: input number
        :return: a boolean representing whether or not the number can be entered
        '''
        row, col = loc
        # check row
        for j in range(len(self.board[row])):
            if j != col and self.board[row][j] == num:
                return False

        # check col
        for i in range(len(self.board)):
            if i != row and self.board[i][col] == num:
                return False

        # check big square
        big_row, big_col = row // 3, col // 3
        for i in range(big_row * 3, big_row * 3 + 3):
            for j in range(big_col * 3, big_col * 3 + 3):
                if i != row and j != col and self.board[i][j] == num:
                    return False

        return True

    def find_empty(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 0:
                    return [i, j]
        return None

    def solve_one_square(self,loc):
        if loc:
            row, col = loc
            find = False
            for i in range(1, 10):
                print(f'{loc} - {i}')
                if self.is_valid(loc, i):
                    self.board[row][col] = i
                    if self.solve_one_square(self.find_empty()):
                        return True
            if find:
                return True
            else:
                self.board[row][col] = 0
                return False
        else:
            return True

    def draw(self):
        # Draw Grid Lines
        gap = self.width / 9
        for i in range(self.rows+1):
            if i % 3 == 0:
                thick = 4
            else:
                thick = 1
            pygame.draw.line(self.win, (0,0,0), (self.posy, i*gap+self.posx), (self.width+self.posy, i*gap+self.posx), thick) # horizontal
            pygame.draw.line(self.win, (0, 0, 0), (i * gap+self.posy, self.posx), (i * gap+self.posy, self.height+self.posx), thick) # vertical

        # Draw Cubes
        # for i in range(self.rows):
        #     for j in range(self.cols):
        #         self.cubes[i][j].draw(self.win)


def redraw_window(win, board, time, strikes):
    win.fill((255,255,255))
    # Draw time
    fnt = pygame.font.SysFont("comicsans", 40)
    text = fnt.render("Time: " + str(time), 1, (0,0,0))
    win.blit(text, (600, 560))
    # Draw Strikes
    # text = fnt.render("X " * strikes, 1, (255, 0, 0))
    # win.blit(text, (20, 560))
    # Draw grid and board
    board.draw()


def main():
    win = pygame.display.set_mode((800,800))
    pygame.display.set_caption("Sudoku")
    board = Board(9, 9, 540, 540, win, (50,50))
    key = None
    run = True
    start = time.time()
    strikes = 0
    while run:

        play_time = round(time.time() - start)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_KP1:
                    key = 1
                if event.key == pygame.K_KP2:
                    key = 2
                if event.key == pygame.K_KP3:
                    key = 3
                if event.key == pygame.K_KP4:
                    key = 4
                if event.key == pygame.K_KP5:
                    key = 5
                if event.key == pygame.K_KP6:
                    key = 6
                if event.key == pygame.K_KP7:
                    key = 7
                if event.key == pygame.K_KP8:
                    key = 8
                if event.key == pygame.K_KP9:
                    key = 9
                # if event.key == pygame.K_DELETE:
                #     board.clear()
                #     key = None
                #
                # if event.key == pygame.K_SPACE:
                #     board.solve_gui()

                # if event.key == pygame.K_RETURN:
                #     i, j = board.selected
                #     if board.cubes[i][j].temp != 0:
                #         if board.place(board.cubes[i][j].temp):
                #             print("Success")
                #         else:
                #             print("Wrong")
                #             strikes += 1
                #         key = None
                #
                #         if board.is_finished():
                #             print("Game over")

            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     pos = pygame.mouse.get_pos()
            #     clicked = board.click(pos)
            #     if clicked:
            #         board.select(clicked[0], clicked[1])
            #         key = None

        # if board.selected and key != None:
        #     board.sketch(key)
        #
        redraw_window(win, board, play_time, strikes)
        pygame.display.update()


if __name__ == '__main__':
    main()
    pygame.quit()

