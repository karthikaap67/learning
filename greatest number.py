a=input("enter number 1=")
b=input("enter number 2=")
print("METHOD 1")
if a>b:
    print(a)
else:
    print(b)
print("METHOD 2")
maximum=max(a,b)
print(maximum)
print("METHOD 3")
def maximum(a,b):
    if a>b:
        return a
    else:
        return b
print(maximum(a,b))