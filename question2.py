# find if the given number is a palindrome or not

n=list(input("Enter a number : "))
if n[::-1]==n:
    print("It is a palindrome number")
else:
    print("It is not a palindrome number")
