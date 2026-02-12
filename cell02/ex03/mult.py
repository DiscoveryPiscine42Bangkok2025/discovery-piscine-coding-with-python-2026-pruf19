a = int(input())
b = int(input())
c = a*b
print(a,"x",b,"=",c)
if c == 0:
    print("the result is positive and negative")
elif c > 0:
    print("the result is positive")
else:
    print("the result is negative")