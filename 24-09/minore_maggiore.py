import random 

a, b, c = [random.randint(1, 6) for _ in range(3)]

if a < b and a < c:
    print(a)
elif b < c:
    print(b)
else:
    print(c)

