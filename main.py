text = 'Roma' [::-1]
print(text)

a = int(input("a: "))# 10
b = int(input("b: "))# 5

if a < b:
   for i in range(a, b + 1):
    print(i)
if a > b:
    for i in range(a, b - 1, -1):
        print(i)

a = int(input("a: "))# 5
b = int(input("b: "))# 10

if a < b:
   for i in range(a, b + 1):
        print(i)

a = "*****"
x = 0

for i in a:
    x = x + 1
    print(a[0:x])

for i in a:
    x = x - 1
    print(a[0:x])































