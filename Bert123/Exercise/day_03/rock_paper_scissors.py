
class InvalidChoiceError(ValueError):
    pass


choices=("Rock","Paper","Scissors")
user_input=input("Enter your choice:  ")


if user_choice not in options:
    raise InvalidChoiceError()