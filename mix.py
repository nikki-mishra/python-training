def even(a):
    if a%2==0:
        print("this is even")
    else:
        print("this is not even")
def odd(b):
    if b%2!=0:
        print("this is odd")
    else:
        print("this is not odd")
def prime(c):
    p=0
    j=2
    while j<c:
        if c%j==0:
            p=1
            break
        j=j+1
    if p==0:
        print("this is prime")
    else:
        print("this is not prime")

ch=input("1 for even, 2 for odd,3 for prime")
l=int(input("enter any value"))
if ch=="1":
    even(l)
elif ch=="2":
    odd(l)
elif ch=="3":
    prime(l)
else:
    print("error")








