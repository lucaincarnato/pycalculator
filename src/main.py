import tkinter as tk

window = tk.Tk()
window.geometry("515x400")
window.title("PyCalculator")
window.configure(background="#F8F1FF")
window.resizable(False, False)

icon = tk.PhotoImage(file="/home/lucaincarnato/Scrivania/pycalculator/src/icon.png")
window.iconphoto(False, icon)

#Configuring an array of buttons to create them easily
#The text_buttons array is defined in layers so it is easier to assign a text to its specific button
text_buttons = [["1", "2", "3", "+"], ["4", "5", "6", "-"], ["7", "8", "9", ":"], ["C", "0", "=", "<-"]]
buttons = []
for i in range(4):
    for j in range(4):
        button = tk.Button(window, text=text_buttons[i][j], width=10)
        button.grid(row=i, column=j, pady=10, padx=10)
        buttons.append(button)

#Entry widget to write buttons' content
entry = tk.Text(width=13, height=5)
entry.grid(row=5, padx=10, pady=10)

#Button that makes the calculus be saved in a txt file
save = tk.Button(window, text="Save")
save.grid(row=5, column=1, padx=10, pady=10, sticky="WEN")

if __name__ == "__main__":
    window.mainloop()