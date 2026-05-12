from tkinter import *
from tkinter import messagebox

root=Tk()
root.title('Tic Tac Toe')
root.config(bg="#2c3e50")

playerX=True
count=0 


def players_name():
    try:
        p1=player1_entry.get()
        p2=player2_entry.get()

        if p1.strip()=="" or p2.strip()=="":
            raise ValueError("Please don't leave it blank.")
            
        if not p1.replace(" ","").isalpha() or not p2.replace(" ","").isalpha():
            raise ValueError("NAME MUST ONLY BE LETTERS")

        for b in [b1, b2, b3, b4, b5, b6, b7, b8, b9]:
            b.config(state=NORMAL, bg="#1c2833", fg="white")

        startButton.config(state=DISABLED)
        messagebox.showinfo("Game Ready", f"Match Started: {p1} vs {p2}")

    except ValueError as err:
        messagebox.showwarning("Input Error", err)

name_frame=Frame(root, bg="#2c3e50")
name_frame.grid(row=0, column=0, columnspan=3, pady=10)

Label(name_frame, text="Player X Name:", bg="#2c3e50", fg="white", font=("Arial", 10, "bold")).grid(row=0, column=0)
player1_entry=Entry(name_frame)
player1_entry.grid(row=0, column=1)

Label(name_frame, text="Player O Name:", bg="#2c3e50", fg="white", font=("Arial", 10, "bold")).grid(row=1, column=0)
player2_entry=Entry(name_frame)
player2_entry.grid(row=1, column=1)

startButton=Button(name_frame, text="Start Game", command=players_name, bg="#27ae60", fg="white")
startButton.grid(row=2, column=0, columnspan=2, pady=5)

def save_to_file(winner_text):
    try:
        with open("winners_record.txt", "a") as f:
            f.write(f"Result: {winner_text}\n")
    except Exception as error:
        print("File error:", error)

def disable_other_buttons():
    all_buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
    for button in all_buttons:
        button.config(state=DISABLED)

def reset_game():
    global playerX, count
    playerX = True
    count = 0
    startButton.config(state=NORMAL)
    all_buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
    for button in all_buttons:
        button.config(text=" ", bg="#1c2833", state=DISABLED)

def exit_game():
    root.destroy()

def winnerchecker():
    global winner
    winner = False
    p1=player1_entry.get()
    p2=player2_entry.get()

    if b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X":
        b1.config(bg="#27ae60"); b2.config(bg="#27ae60"); b3.config(bg="#27ae60")
        winner = True
        messagebox.showinfo("Tic Tac Toe", f"Congrats {p1}, you win!!")
        save_to_file(f"{p1} Wins!!!!")
        disable_other_buttons()
    elif b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X":
        b4.config(bg="#27ae60"); b5.config(bg="#27ae60"); b6.config(bg="#27ae60")
        winner = True
        messagebox.showinfo("Tic Tac Toe", f"Congrats {p1}, you win!!")
        save_to_file(f"{p1} Wins!!!!")
        disable_other_buttons()
    elif b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X":
        b7.config(bg="#27ae60"); b8.config(bg="#27ae60"); b9.config(bg="#27ae60")
        winner = True
        messagebox.showinfo("Tic Tac Toe", f"Congrats {p1}, you win!!")
        save_to_file(f"{p1} Wins!!!!")
        disable_other_buttons()
    elif b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X":
        b1.config(bg="#27ae60"); b4.config(bg="#27ae60"); b7.config(bg="#27ae60")
        winner = True
        messagebox.showinfo("Tic Tac Toe", f"Congrats {p1}, you win!!")
        save_to_file(f"{p1} Wins!!!!")
        disable_other_buttons()
    elif b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X":
        b2.config(bg="#27ae60"); b5.config(bg="#27ae60"); b8.config(bg="#27ae60")
        winner = True
        messagebox.showinfo("Tic Tac Toe", f"Congrats {p1}, you win!!")
        save_to_file(f"{p1} Wins!!!!")
        disable_other_buttons()
    elif b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X":
        b3.config(bg="#27ae60"); b6.config(bg="#27ae60"); b9.config(bg="#27ae60")
        winner = True
        messagebox.showinfo("Tic Tac Toe", f"Congrats {p1}, you win!!")
        save_to_file(f"{p1} Wins!!!!")
        disable_other_buttons()
    elif b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X":
        b1.config(bg="#27ae60"); b5.config(bg="#27ae60"); b9.config(bg="#27ae60")
        winner = True
        messagebox.showinfo("Tic Tac Toe", f"Congrats {p1}, you win!!")
        save_to_file(f"{p1} Wins!!!!")
        disable_other_buttons()
    elif b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X":
        b3.config(bg="#27ae60"); b5.config(bg="#27ae60"); b7.config(bg="#27ae60")
        winner = True
        messagebox.showinfo("Tic Tac Toe", f"Congrats {p1}, you win!!")
        save_to_file(f"{p1} Wins!!!!")
        disable_other_buttons()

    elif b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O":
        b1.config(bg="#2980b9"); b2.config(bg="#2980b9"); b3.config(bg="#2980b9")
        winner = True
        messagebox.showinfo("Tic Tac Toe", f"Congrats {p2}, you win!!")
        save_to_file(f"{p2} Wins!!!!")
        disable_other_buttons()
    elif b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="O":
        b4.config(bg="#2980b9"); b5.config(bg="#2980b9"); b6.config(bg="#2980b9")
        winner = True
        messagebox.showinfo("Tic Tac Toe", f"Congrats {p2}, you win!!")
        save_to_file(f"{p2} Wins!!!!")
        disable_other_buttons()
    elif b7["text"]=="O" and b8["text"]=="O" and b9["text"]=="O":
        b7.config(bg="#2980b9"); b8.config(bg="#2980b9"); b9.config(bg="#2980b9")
        winner = True
        messagebox.showinfo("Tic Tac Toe", f"Congrats {p2}, you win!!")
        save_to_file(f"{p2} Wins!!!!")
        disable_other_buttons()
    elif b1["text"]=="O" and b4["text"]=="O" and b7["text"]=="O":
        b1.config(bg="#2980b9"); b4.config(bg="#2980b9"); b7.config(bg="#2980b9")
        winner = True
        messagebox.showinfo("Tic Tac Toe", f"Congrats {p2}, you win!!")
        save_to_file(f"{p2} Wins!!!!")
        disable_other_buttons()
    elif b2["text"]=="O" and b5["text"]=="O" and b8["text"]=="O":
        b2.config(bg="#2980b9"); b5.config(bg="#2980b9"); b8.config(bg="#2980b9")
        winner = True
        messagebox.showinfo("Tic Tac Toe", f"Congrats {p2}, you win!!")
        save_to_file(f"{p2} Wins!!!!")
        disable_other_buttons()
    elif b3["text"]=="O" and b6["text"]=="O" and b9["text"]=="O":
        b3.config(bg="#2980b9"); b6.config(bg="#2980b9"); b9.config(bg="#2980b9")
        winner = True
        messagebox.showinfo("Tic Tac Toe", f"Congrats {p2}, you win!!")
        save_to_file(f"{p2} Wins!!!!")
        disable_other_buttons()
    elif b1["text"]=="O" and b5["text"]=="O" and b9["text"]=="O":
        b1.config(bg="#2980b9"); b5.config(bg="#2980b9"); b9.config(bg="#2980b9")
        winner = True
        messagebox.showinfo("Tic Tac Toe", f"Congrats {p2}, you win!!")
        save_to_file(f"{p2} Wins!!!!")
        disable_other_buttons()
    elif b3["text"]=="O" and b5["text"]=="O" and b7["text"]=="O":
        b3.config(bg="#2980b9"); b5.config(bg="#2980b9"); b7.config(bg="#2980b9")
        winner = True
        messagebox.showinfo("Tic Tac Toe", f"Congrats {p2}, you win!!")
        save_to_file(f"{p2} Wins!!!!")
        disable_other_buttons()
    
    if count == 9 and winner == False:
        messagebox.showinfo("Tic Tac Toe", "It's a Tie!")
        save_to_file("Tie Game")

def b_click(b):
    global playerX, count
    if b["text"]== " " and playerX==True:
        b.config(text="X", fg="#e74c3c")
        playerX=False
        count += 1
        winnerchecker()
    elif b["text"]== " " and playerX==False:
        b.config(text="O", fg="#3498db")
        playerX=True
        count += 1
        winnerchecker()
    else:
        messagebox.showwarning("Tic Tac Toe", "That box has already been selected.")

b1 = Button(root, text=" ", font=("Verdana", 20, "bold"), height=3, width=6, bg="#1c2833", state=DISABLED, command=lambda: b_click(b1))
b2 = Button(root, text=" ", font=("Verdana", 20, "bold"), height=3, width=6, bg="#1c2833", state=DISABLED, command=lambda: b_click(b2))
b3 = Button(root, text=" ", font=("Verdana", 20, "bold"), height=3, width=6, bg="#1c2833", state=DISABLED, command=lambda: b_click(b3))
b4 = Button(root, text=" ", font=("Verdana", 20, "bold"), height=3, width=6, bg="#1c2833", state=DISABLED, command=lambda: b_click(b4))
b5 = Button(root, text=" ", font=("Verdana", 20, "bold"), height=3, width=6, bg="#1c2833", state=DISABLED, command=lambda: b_click(b5))
b6 = Button(root, text=" ", font=("Verdana", 20, "bold"), height=3, width=6, bg="#1c2833", state=DISABLED, command=lambda: b_click(b6))
b7 = Button(root, text=" ", font=("Verdana", 20, "bold"), height=3, width=6, bg="#1c2833", state=DISABLED, command=lambda: b_click(b7))
b8 = Button(root, text=" ", font=("Verdana", 20, "bold"), height=3, width=6, bg="#1c2833", state=DISABLED, command=lambda: b_click(b8))
b9 = Button(root, text=" ", font=("Verdana", 20, "bold"), height=3, width=6, bg="#1c2833", state=DISABLED, command=lambda: b_click(b9))


b1.grid(row=1, column=0); b2.grid(row=1, column=1); b3.grid(row=1, column=2)
b4.grid(row=2, column=0); b5.grid(row=2, column=1); b6.grid(row=2, column=2)
b7.grid(row=3, column=0); b8.grid(row=3, column=1); b9.grid(row=3, column=2)

againButton = Button(root, text="Play Again", command=reset_game, bg="#f1c40f")
againButton.grid(row=4, column=0, pady=10)

exitButton = Button(root, text="Exit Game", command=exit_game, bg="#e67e22")
exitButton.grid(row=4, column=2, pady=10)

root.mainloop()