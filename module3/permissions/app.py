import os

os.chmod("demo.txt", 0o777)

print(os.access("demo.txt", os.W_OK))

with open("demo.txt", "w") as f:
    f.write("welcome 123")