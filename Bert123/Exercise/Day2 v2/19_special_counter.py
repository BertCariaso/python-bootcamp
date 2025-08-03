string=input("Enter String:  ")
special_count=0
special_char='!@#$%^&*()'

for special_char in string:
    if string in special_char:
        special_count +=1
print(special_count)