#write a program to find the factorial of a nummber

n=int(input("Enter a number : "))
s=2
if n<2:
    print(1)
else:
    for i in range(3,n+1):
        s*=i
    print(s)
    
