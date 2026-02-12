a = [2, 8, 9, 48, 8, 22, -12, 2]
b = set()
for i in a:
    if i > 5:
        b.add(i + 2)
print(a)
print(b)