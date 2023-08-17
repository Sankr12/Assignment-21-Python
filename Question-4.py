# Write a recursive function to print first N odd natural numbers in reverse order

def odd_n(N):
    if N>0:
        print(2*N-1)
        odd_n(N-1)

num = int(input("Enter a number: "))
odd_n(num)