#write a program to find if the given number is prime no or not

n=int(input("Enter a number : "))
a=0
sqrt_n = int(n**0.5) + 1
for i in range(3, sqrt_n, 2):
    if n % i == 0:
        print(n,"is not a prime number")
        a=1
        break
if not a:
    print(n,"is a prime nimber")
