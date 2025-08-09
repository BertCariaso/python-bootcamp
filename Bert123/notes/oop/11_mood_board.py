import tkinter
root=tkinter.Tk()

left=tkinter.Label(root,text=":) Happy",padx=5,
    font=("Chiller",14,"italic"),
    fg="red",
    bg="black"
)
left.pack(side="left")

right=tkinter.Label(root,text=":( Sad",padx=5,
    font=("Chiller",14,"italic"),
    fg="red",
    bg="blue"
                    )
left.pack(side="right")




root.mainloop()