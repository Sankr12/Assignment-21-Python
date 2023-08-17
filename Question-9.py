# Write a recursive python function to print first N multiples of a given number

def N_multiples(N):
    num = 9
    if N>0:
        N_multiples(N-1)
        print(num*N)

num = int(input("Enter a number for multiplying 9: "))
N_multiples(num)
