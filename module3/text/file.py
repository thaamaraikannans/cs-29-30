# task = open("F:\\IMS\\CyberSecurity\\offline\\cs-29-30\\task.md", "r")
# value = task.read()
# print(value)

# # for data in value:
# #     print(data)

# for num in range(2):
#     response = open(f"aws{num}.txt", "a")
#     response.write(f"\nhello aws {num}")
#     response.close()


# name = open("file.txt")
# second = name.read()
# third = open(second).read()
# fourth = open(third).read()
# print(fourth)

with open("file.txt") as name:
    f = name.read()
    print(f)
    with open(f) as k:
        v = k.read()
        print(v)
        with open(v) as m:
            print(m.read())