# Write a recursive function to print first N even natural numbers in reverse order

def even_n(N):
    if N>0:
        print(2*N)
        even_n(N-1)
        
num = int(input("Enter a number: "))
even_n(num)