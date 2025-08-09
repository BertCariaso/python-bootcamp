import tkinter

root=tkinter.Tk()

instruction=tkinter.Label(root,text="Enter your Password: ")
instruction.pack()



entry=tkinter.Entry(root)
entry.pack()

password="password"

user_input=tkinter.StringVar(value="Please enter your password  ")
label=tkinter.Label(root,textvariable=user_input)
label.pack()


'''when press enter'''
def show_input(event):
        given_text=entry.get()

        label.pack()
        if given_text==password:
            user_input.set("Access granted")
        else:
            user_input.set("Access denied")


root.bind("<Return>",show_input)

root.mainloop()


