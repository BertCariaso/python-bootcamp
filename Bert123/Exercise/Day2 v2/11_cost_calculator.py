


expenses=0
cost=0
current_expenses=0

def spend(expenses):
    new_expense=int(input("new_expense "))
    expenses.append(new_expense)
    print(new_expense)
    print(expenses)

def refund(expenses):
    remove =expenses.pop(-1)
    print(remove)
def show(expenses):
    print(expenses)

def save(expenses, ):
    filepath=input("filepath")
    with open(filepath,"w")as file:
        for expense in expenses:
            file.write(str(expense)+"\n")

def main():
    current_expenses=[]
    command=input("Command:  ",)
    while command:
        if command =="spend":
            spend(current_expenses)
        elif command =="refund":
            refund(current_expenses)
        elif command =="show":
            show(current_expenses)
        elif command =="save":
            save(current_expenses)
        command = input("command:_")

main()





