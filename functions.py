import random
from tkinter import *
from tkinter import messagebox

solvedSudoku=[2,9,5,7,4,3,8,6,1,4,3,1,8,6,5,9,2,7,8,7,6,1,9,2,5,4,3,
              3,8,7,4,5,9,2,1,6,6,1,2,3,8,7,4,9,5,5,4,9,2,1,6,7,3,8,
              7,6,3,5,3,4,1,8,9,9,2,8,6,7,1,3,5,4,1,5,4,9,3,8,6,7,2]


def setUp(grid,diff,checkButton,forfeitButton):
    checkButton.config(state=ACTIVE)
    forfeitButton.config(state=ACTIVE)
    if diff=="e":
        for i in range(0,len(grid)):
            if int(random.randint(0,1)) == 1:
                grid[i].delete(1.0, END)
                grid[i].insert(INSERT,solvedSudoku[i])
            else:
                grid[i].delete(1.0, END)
    if diff=="m":
        for i in range(0, len(grid)):
            if int(random.randint(0,2)) == 2:
                grid[i].delete(1.0, END)
                grid[i].insert(INSERT, solvedSudoku[i])
            else:
                grid[i].delete(1.0, END)
    if diff=="h":
        for i in range(0, len(grid)):
            if int(random.randint(0, 3)) == 3:
                grid[i].delete(1.0, END)
                grid[i].insert(INSERT, solvedSudoku[i])
            else:
                grid[i].delete(1.0, END)
    if diff=="f":
        for i in range(0, len(grid)):
            grid[i].delete(1.0,END)
            grid[i].insert(INSERT, solvedSudoku[i])

def answerCheck(grid):
    playerAnswers = []
    for i in grid:
        if i.get(1.0,END):
            playerAnswers.append(int(i.get(1.0,END)))
    print(playerAnswers)
    global solvedSudoku
    if playerAnswers==solvedSudoku:
        messagebox.showinfo(title="Sudoku check",message="Congradulations! You solved your sudoku puzzle")
    else:
        messagebox.showinfo(title="Sudoku check",message="There's at least 1 error in your sudoku puzzle")