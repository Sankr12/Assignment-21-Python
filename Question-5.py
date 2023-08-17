# Write a recursive function to print first N even natural numbers 

def even_n(N):
    if N>0:
        even_n(N-1)
        print(2*N)

num = int(input("Enter a number: "))
even_n(num)