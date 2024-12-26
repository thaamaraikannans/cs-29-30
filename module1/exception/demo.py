# try: -> written a block of code for execution
# except: -> handle the error
# else: -> if no error/ try block executed successfully -> else block will work
# finally: -> run on every time....


try:
    a = 10
    b = 2
    c = a/b[2]
    
# except ZeroDivisionError:
#     print("can't divide by zero")
# except TypeError:
#     print("check type of the data")
except Exception as error:
    print(error)
else:
    print("no error so i am executing")
    print(c)    
finally:
    print("program stopped")