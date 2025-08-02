"""
def brew(drink,extra):

    print(f"I made you{drink} with{extra}")


brew("coffee","sugar")
brew("tea","milk")
"""
def brew(drink,extra=None):
    if extra:
        print(f"I made you{drink} with{extra}")
    else:
        print(f"I made you {drink}")






brew("coffee","sugar")
brew("tea","milk")
