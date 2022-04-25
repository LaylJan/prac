from email import message
from tkinter import *
from tkinter import ttk
import tkinter as tk
from click import command

from pip import main


root = tk.Tk()

def clicklog():
    print("button click")

root.title("My Gui")
root.geometry("600x600+50+30")
root.resizable(False, False) 
root.iconbitmap('th.ico')

tk.Label(root, text='Classic Label').pack()
ttk.Label(root, text='Themed Label').pack()

btn = ttk.Button(root, text = "click", command=clicklog)
exit_btn = ttk.Button(root, text = "Exit", command=root.quit )

exit_btn.pack()
btn.pack()

message = tk.Label(root, text = "My Gui")
message.pack()
    
root.mainloop()
print("Line")
