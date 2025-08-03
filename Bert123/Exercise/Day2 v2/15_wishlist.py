items=[{
    "shoes": "footwear",
    "nike":5_000
},{"phone": "mobile phone",
    "samsung":8_000},{"shir": "T-shirt",
    "Addidas":800
}]

for item in items:
    for key,value in item.items():
        print(key,value)

"""
print(items.item())
"""