

user_input=input("Enter number: ")
user_input = user_input.strip()
user_input = user_input.replace(',',"")
digits=user_input.split()
user_input="".join(digits)


if user_input .isnumeric():
    print("Number is numeric")
else:
    print("It is not a valid number")






