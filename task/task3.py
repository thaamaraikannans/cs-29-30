numbers = [12, 47, 18, 42]

num1 = numbers[0]
num2 = numbers[1]
num3 = numbers[2]
num4 = numbers[3]

even = []

if num1%2 == 0:
    even.append(num1)

if num2%2==0:
    even.append(num2)

if num3%2==0:
    even.append(num3)
    
if num4%2==0:
    even.append(num4)

print(even)
even.sort()
even.reverse()

print(even[0], "is the largest even number")
print(max(even), "is the largest even number")