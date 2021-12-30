#TODO give all the buttons their role


import tkinter as tk
from calc import Calc

#Importation from other file
c = Calc()

class App():
    def __init__(self, name, window):
        self.name = name
        self.window = window
        window.geometry("515x400")
        window.title("PyCalculator")
        window.configure(background="#F8F1FF")
        window.resizable(False, False)

        icon = tk.PhotoImage(file="/home/lucaincarnato/Scrivania/pycalculator/src/icon.png")
        window.iconphoto(False, icon)

        #Configuring an array of buttons to create them easily
        #The text_buttons array is defined in layers so it is easier to assign a text to its specific button
        text_buttons = [["1", "2", "3", "+"], ["4", "5", "6", "-"], ["7", "8", "9", ":"], ["<-", "0", "=", "*"]]
        #The values_buttons contains the functions that will be inserted in the command= attribute relative to the value of buttons
        values_buttons = [[c.one, c.two, c.three, c.sum], [c.four, c.five, c.six, c.sub], [c.seven, c.eight, c.nine, c.div], [False, c.zero, False, c.mul]]
        buttons = []
        for i in range(4):
            for j in range(4):
                button = tk.Button(window, text=text_buttons[i][j], width=10, command=values_buttons[i][j])
                button.grid(row=i, column=j, pady=10, padx=10)
                buttons.append(button)
                #? Add the script to insert in the entry

        #Entry widget to write buttons' content
        entry = tk.Text(width=13, height=5)
        entry.grid(row=5, padx=10, pady=10)

        #Button that makes the calculus be saved in a txt file
        save = tk.Button(window, text="Save")
        save.grid(row=5, column=1, padx=10, pady=10, sticky="WEN")

        #Button that delete the operation
        save = tk.Button(window, text="Cancel")
        save.grid(row=5, column=2, padx=10, pady=10, sticky="WEN")

    def start(self):
        if __name__ != "__main__": return
        self.window.mainloop()

#Initialized with app name and app window
calculator = App("calculator", tk.Tk())
calculator.start()