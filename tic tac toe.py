from tkinter import *
import random

def next_turn(row, col):
    global player

    if arr[row][col]['text'] == "" and check_winner() is False:

        if player == players[0]:

            arr[row][col]['text'] = player

            if check_winner() is False:
                player = players[1]
                label.config(text=("Turn: "+players[1]))

            elif check_winner() is True:
                label.config(text=(players[0]+" wins!"))

            elif check_winner() == "Tie":
                label.config(text="Tie!")

        else:

            arr[row][col]['text'] = player

            if check_winner() is False:
                player = players[0]
                label.config(text=("Turn: "+players[0]))

            elif check_winner() is True:
                label.config(text=(players[1]+" wins!"))

            elif check_winner() == "Tie":
                label.config(text="Tie!")


def check_winner():
    for row in range(3):
        if arr[row][0]['text'] == arr[row][1]['text'] == arr[row][2]['text'] != "":
            arr[row][0].config(bg="#F04ADB")
            arr[row][1].config(bg="#F04ADB")
            arr[row][2].config(bg="#F04ADB")
            return True

    for column in range(3):
        if arr[0][column]['text'] == arr[1][column]['text'] == arr[2][column]['text'] != "":
            arr[0][column].config(bg="#F04ADB")
            arr[1][column].config(bg="#F04ADB")
            arr[2][column].config(bg="#F04ADB")
            return True

    if arr[0][0]['text'] == arr[1][1]['text'] == arr[2][2]['text'] != "":
        arr[0][0].config(bg="#F04ADB")
        arr[1][1].config(bg="#F04ADB")
        arr[2][2].config(bg="#F04ADB")
        return True

    elif arr[0][2]['text'] == arr[1][1]['text'] == arr[2][0]['text'] != "":
        arr[0][2].config(bg="#F04ADB")
        arr[1][1].config(bg="#F04ADB")
        arr[2][0].config(bg="#F04ADB")
        return True

    elif empty_spaces() is False:

        for row in range(3):
            for column in range(3):
                arr[row][column].config(bg="#F7F44F")
        return "Tie"

    else:
        return False
def empty_spaces():
    spaces = 9
    for row in range(3):
        for column in range(3):
            if arr[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True
def new_game():
    global player

    player = random.choice(players)

    label.config(text="Turn: "+player)

    for row in range(3):
        for column in range(3):
            arr[row][column].config(text="",bg="pink")

window = Tk()
window.geometry("500x400")
window.title("Tic Tac Toe")
window.minsize(300,400)
window.maxsize(500,400)
players =["X","O"]
player=random.choice(players)
arr= [[0,0,0],
      [0,0,0],
      [0,0,0]]
label = Label(text="Turn: "+player,font=("consolas",20))
label.pack(side="top")
reset_button= Button(text="reset",font=("consolas",15),command=new_game,bg="#E5AFA3")
reset_button.place(x=350,y=320)
f=Frame(window)
f.pack()
for row in range(3):
    for col in range(3):
        arr[row][col]=Button(f,text="",font=("consolas",20),width=5,height=2,
        command= lambda row=row, column=col: next_turn(row,column),bg="pink")
        arr[row][col].grid(row=row,column=col)


window.mainloop()