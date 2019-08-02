# !/usr/bin/python3
import functions
from tkinter import *
grid = []
root = Tk()

root.title("Sudoku")
root.geometry("450x545")
for h in range(2,11):
    for i in range(0,9):
        newText = Text(insertborderwidth=2, height=50, width=50, bd=1, bg="grey", fg="brown",
                       font=("helvetica",32,"bold"), highlightbackground="black")
        newText.place(x=50*i,y=50*h)
        grid.append(newText)

easyButton = Button(root,text = "EASY",command= lambda: functions.setUp(grid,"e",checkButton,forfeitButton))
easyButton.place(x = 90 , y = 0)

mediumButton = Button(root,text = "MEDIUM",command= lambda: functions.setUp(grid,"m",checkButton,forfeitButton))
mediumButton.place(x = 180 , y = 0)

hardButton = Button(root,text = "HARD",command= lambda: functions.setUp(grid,"h",checkButton,forfeitButton))
hardButton.place(x = 270 , y = 0)

checkButton = Button(root,text = "CHECK YOUR ANSWERS", state=DISABLED, command= lambda: functions.answerCheck(grid))
checkButton.place(x = 30 , y = 40)

forfeitButton = Button(root,text = "FORFEIT - SEE ANSWERS", state=DISABLED, command= lambda: functions.setUp(grid,"f",checkButton,forfeitButton))
forfeitButton.place(x = 240 , y = 40)

root.mainloop()