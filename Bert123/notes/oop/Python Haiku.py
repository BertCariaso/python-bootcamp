import tkinter

root=tkinter.Tk()
root.title("Python Haiku")
root.geometry("500x500")

label=tkinter.Label(root,text=""" 
Loops within loops spin,
A silient function returns,
The logic is clear.
""")

label.pack()
root.mainloop()