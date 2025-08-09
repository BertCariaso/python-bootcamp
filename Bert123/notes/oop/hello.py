import tkinter

root=tkinter.Tk()
root.title("Example Application")
root.geometry("1200x400")

message="""
Hello 
World"""
label=tkinter.Label(
    root,
    text=message,
    font=("Chiller",14,"italic"),
    fg="red",
    bg="black"
)
label.pack()


'''responsible to execute'''

''' responsible for loop '''
root.mainloop()