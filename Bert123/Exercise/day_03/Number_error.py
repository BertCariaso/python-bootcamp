
class NotANumberError(ValueError):
    pass

class NotAPositiveNumberError(ValueError):
    pass

class NotWithinRangeError(ValueError):
    pass
user_input = input("Enter positive number [1,100]: ")

if not user_input.isnumeric() and not user_input[1:].isnumeric():
    raise NotANumberError

number=int(user_input)
if number <0:
    raise NotAPositiveNumberError()

if not(0<= number <=100):
    raise NotWithinRangeError()


