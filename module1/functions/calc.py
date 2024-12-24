def add(num1, num2, val1="hello"):
    print(val1)
    data = num1+num2
    return data

def sub(num1, num2):
    data = num1-num2
    return data

def mul(num1, num2):
    data = num1*num2
    return data

def div(num1, num2):
    data = num1/num2
    return data

def calc():
    print("welcome to calculator !!!!")
    do_perform_next = True
    while do_perform_next:
        a = int(input("enter a number 1: "))
        b = int(input("enter a number 2: "))
        user_inp = input("enter a operation (+ - * /): ")
        if user_inp == "+":
            print("addition value is ",add(b,a, "c"))
        elif user_inp == "-":
            print("subtraction value is ",sub(a, b))
        elif user_inp == "*":
            print("multiplication value is ",mul(a, b))
        elif user_inp == "/":
            print("division value is ",div(a, b))
        else:
            print("Invalid operation")
        next_operation = input("do you want run another calulation? (Y/N)")
        if next_operation == "N":
            do_perform_next = False
            print("Thanks")
    return

calc()