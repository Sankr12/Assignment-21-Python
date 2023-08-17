# Write a recursive python function to print squares of first N natural numbers 

def square(n):
    if n>0:
        square(n-1)
        print(n*n)

num = int(input("Enter the number: "))
square(num)