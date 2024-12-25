def students(stu_list):
    try:
        print("Student details")
        series = len(stu_list[3])
        print(series)
    except Exception as err:
        print("error", err)
    else:
        try:
            for name in stu_list:
                print(name)
        except Exception as app:
            print("error in else call", app)
    finally:
        print("End of details")
    return

try:
    students(["manoj", "sakthi"])
except Exception as error:
    print("error", error)
    
data = {10, 20}
print(data[10])