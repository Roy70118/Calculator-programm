
class Calculator:
    def add(self, a, b):
        return a+b

    def subtract(self, a, b):
        return a-b

    def multiply(self, a, b):
        return a*b

    def divide(self, a, b):
        return a/b


my_cal = Calculator()

while True:

    print("1.Add")
    print("2.Subatract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Exit")

    user_input = int(input("Enter the operation: "))

    # make sure user have entered the correct option
    if user_input in (1, 2, 3, 4, 5):

        # First check user want to exit
        if (user_input == 5):
            break

        #  if not then ask to the input to call the appropriate methods
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))

        if (user_input == 1):
            print(a, "+", b, "=", my_cal.add(a, b))

        elif (user_input == 2):
            print(a, "-", b, "=", my_cal.subtract(a, b))

        elif (user_input == 3):
            print(a, "*", b, "=", my_cal.multiply(a, b))

        elif (user_input == 4):
            print(a, "/", b, "=", my_cal.divide(a, b))

    else:
        print("Invalid input")
