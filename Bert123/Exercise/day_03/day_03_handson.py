import tkinter
import json
root=tkinter.Tk()

label=tkinter.Label(root,text="name")
label.pack()
name_var=tkinter.StringVar()
name_enter=tkinter.Entry(root,textvariable=name_var
)
name_enter.pack()

label=tkinter.Label(root,text="age")
label.pack()
age_var=tkinter.StringVar()
age_enter=tkinter.Entry(root,textvariable=age_var
)
age_enter.pack()

label=tkinter.Label(root,text="Preferred Theme")
label.pack()

radio_var = tkinter.StringVar(value="Light")
radio1 = tkinter.Radiobutton(
root, text="Light",variable=radio_var, value="Light")
radio1.pack()

radio2 = tkinter.Radiobutton(
root, text="Dark",variable=radio_var, value="Dark")
radio2.pack()

check_value = tkinter.BooleanVar()
checkbox = tkinter.Checkbutton(
root,
text="Subscribe to newsletter",
variable=check_value)
checkbox.pack()

slider_value = tkinter.IntVar(value=0)
slider = tkinter.Scale(
root,
from_=0,
to=3,
orient="horizontal",
variable=slider_value
)
slider.pack()


def submit():
    data={
        "Name": name_var.get(),
        "Age": age_var.get(),
        "Theme": radio_var.get(),
        "Subscribe": check_value.get(),
        "Rating": slider_value.get()
    }
    with open("user.json","w")as file:
            json.dump(data,file)
button = tkinter.Button(root, text="Submit", command=submit)
button.pack()

root.mainloop()


'''
def show_input():
    given_text = entry.get()
    user_input.set(given_text)
root.mainloop()
'''








