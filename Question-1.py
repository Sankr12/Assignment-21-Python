# Write a recursive python function to print first N natural numbers.

def print_N(n):
    if n>0:
        print_N(n-1)
        print(n)
    
num = int(input("Enter a number: "))

print_N(num)