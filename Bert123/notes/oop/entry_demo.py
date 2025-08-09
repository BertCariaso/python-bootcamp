import tkinter

root=tkinter.Tk()

entry=tkinter.Entry(root)
entry.pack()


user_input=tkinter.StringVar(value="Plese enter any input  ")
label=tkinter.Label(root,textvariable=user_input)
label.pack()


'''when press enter'''
def show_input(event):
        given_text=entry.get()
        label=tkinter.Label(root,text=given_text)
        label.pack()


root.bind("<Return>",show_input)

root.mainloop()



