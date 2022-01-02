import tkinter as tk

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

        #This frame will contain all the button, so it is possible to make a larger entry
        frame = tk.Frame(window, background="#F8F1FF")
        frame.grid(column=0, row=0, pady=10, padx=0)

        #Configuring an array of buttons to create them easily
        #The text_buttons array is defined in layers so it is easier to assign a text to its specific button
        text_buttons = [["1", "2", "3", "+"], ["4", "5", "6", "-"], ["7", "8", "9", ":"], ["(", "0", ")", "*"]]
        buttons = [[], [], [], []]

        #Rendering all the buttons, witch texts are defined below
        for i in range(4):
            for j in range(4):
                #The lambda function creates for every i and j an istance that refers to each button, so that onclick the command attribute goes to pick the right text
                button = tk.Button(frame, text=text_buttons[i][j], width=10, command=lambda c=i, d=j: entry.insert(tk.END, text_buttons[c][d]))
                button.grid(row=i, column=j, pady=10, padx=10)
                buttons[i].append(button)
                #! It returns only the last char

        #Entry widget to write buttons' content
        entry = tk.Text(window, width=60, height=5)
        entry.grid(column=0, row=5, padx=10, pady=10)

        #Button to cancel the last character
        deny = tk.Button(frame, text="<-")
        deny.grid(row=5, column=0, padx=10, pady=10, sticky="WEN")

        #Button that makes the calculus be saved in a txt file
        save = tk.Button(frame, text="Save")
        save.grid(row=5, column=1, padx=10, pady=10, sticky="WEN")

        #Button that delete the operation
        cancel = tk.Button(frame, text="Cancel")
        cancel.grid(row=5, column=2, padx=10, pady=10, sticky="WEN")

        #Button to cancel the last character
        solve = tk.Button(frame, text="=")
        solve.grid(row=5, column=3, padx=10, pady=10, sticky="WEN")

    def start(self):
        if __name__ != "__main__": return
        self.window.mainloop()

#Initialized with app name and app window
calculator = App("calculator", tk.Tk())
calculator.start()