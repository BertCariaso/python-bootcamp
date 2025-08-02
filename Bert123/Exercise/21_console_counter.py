count=0
running=True
while running:
    choice=input("Provide command: ")
    if choice=="A":
        count=count+1
        print(count)
    elif choice=="S":
        count=count-1
        print(count)
    elif choice=="D":
        count=count*2
        print(count)
    elif choice=="exit":
        running=False

