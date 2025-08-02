
counter=0
number_input =input("Enter Number:")
counter = counter+1
for item in range(1,11):
    product=int(number_input)*item
    print (item, "X", number_input,"=", product)
