import module
import sys

a = int(input("1: add\n2: sub\n3: multiply\n4: divide\n5: stop\n:"))
if a == 5:
    exit()

num1 = int(input("num1:"))
num2 = int(input("num2:"))

if a == 1:
    print(module.add(num1, num2))
elif a == 2:
    print(module.sub(num1, num2))
elif a == 3:
    print(module.mul(num1, num2))
else:
    print(module.div(num1, num2))
