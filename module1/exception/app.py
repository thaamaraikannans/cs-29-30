
try:
    val1 = 10
    val2 = 2
    print(val1/val2)
except TypeError:
    print("Type error")
    val2 = int(val2)
    print(val1/val2)
except ZeroDivisionError:
    print("can't divide by zero")
except KeyError:
    print("index out range / no valid key")
except NameError:
    print("check namings")
else:
    print("No error found")
finally:
    print("program end")