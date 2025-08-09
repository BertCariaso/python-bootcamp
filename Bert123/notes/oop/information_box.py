import tkinter
from tkinter import messagebox
root = tkinter.Tk()
messagebox.showinfo(
"Information",
"This is an information message."
)
root.mainloop()


'''question box'''
import tkinter
from tkinter import messagebox
root = tkinter.Tk()
# yes or no
response = messagebox.askquestion(
"Question",
"Do you want to continue?"
)
root.mainloop()
