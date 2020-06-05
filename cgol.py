"""
Samuel Hohenshell
06/03/2020

Conway's Game of Life
"""

import csv
import time
import curses
from curses import textpad

from timestep import inc_time

def main(stdscr, csvpath, n):
    # Creating/initializing our grid as an n x n 2D list
    # Grid is n x n going 0 -> n-1 for each row/col
    grid = [[False for i in range(n)] for j in range(n)]

    # Reading the csv, storing in grid, then automatically closing it
    with open(csvpath, encoding='utf-8-sig') as csvfile:
        read_csv = csv.reader(csvfile, delimiter=',')
        for i, r in enumerate(read_csv):
            for j, elem in enumerate(r):
                if (elem == "1"):
                    grid[i][j] = True
                else:
                    grid[i][j] = False

    # Initializing curses
    curses.curs_set(0)          # Makes it so curser won't blink
    sh, sw = stdscr.getmaxyx()  # Getting max x and y coordinates for window
    gamebox = [[0,0],[n+1,n+1]]
    try:
        # Drawing the outline gamepad
        textpad.rectangle(stdscr, gamebox[0][0], gamebox[0][1],
                                  gamebox[1][0], gamebox[1][1])
    except curses.error:
        pass   
    stdscr.refresh()

    # Drawing initial state of board
    draw_board(grid, n, stdscr)

    # Main loop for the game
    while True:
        #time.sleep(2)                # Waiting a short bit before each change
        # Going to the next step if user presses right arrow key
        while True:
            key = stdscr.getch()
            if (key == curses.KEY_RIGHT):
                break
        grid = inc_time(grid, n)     # Making changes to the grid
        draw_board(grid, n, stdscr)  # Redrawing the grid


# Draws board 
def draw_board(grid, n, screen):
    for r in range(n):
        for c in range(n):
            if (grid[r][c]):
                try:
                    screen.addstr(r+1, c+1, "X")
                except curses.error:
                    pass          
            else:
                try:
                    screen.addstr(r+1, c+1, "-")
                except curses.error:
                    pass
    screen.refresh()



##############################################################################
if __name__ == '__main__':
    # Introduction and gathering user input
    print("\n********************************\n")
    print("Welcome to Conway's Game of Life\n")
    print("********************************")
    print("This will read a *.csv file, filled with 1's and 0's as "\
        "the initial state (seed) of the game.")
    csvpath = input("Please enter the name of the *.csv file "
        "(should be in current directory): ")
    n = int(input("Please enter how many rows/columns there will be in the "\
        "game's (square) grid: "))

    # Calling main() but it'll reset any curses changes made automatically
    curses.wrapper(main, csvpath, n)

