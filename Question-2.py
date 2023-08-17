# Write a recursive function to print N natural numbers in reverse order

def reverse_n(n):
    if n>0:
        print(n)
        reverse_n(n-1)

num = int(input("Enter a number: "))
reverse_n(num)