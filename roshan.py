print("hello")

a=10
b=20
print(a+b)

c=int(input("enter any no"))
d=int(input("enter any no"))
try:
    rem=d/c
    print(rem)
except Exception as e:
    print(e)