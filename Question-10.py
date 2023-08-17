# Write a recursive python function to print a number in reverse order

def print_reverse(number):
    if number < 10:
        print(number, end="")
    else:
        print(number % 10, end="")
        print_reverse(number // 10)

# Test the function
input_number = int(input("Enter a number: "))
print("Number in reverse:", end=" ")
print_reverse(input_number)
print()  # Print a newline after the reversed number
