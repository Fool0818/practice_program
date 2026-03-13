# variable to count odd numbers
odd_count = 0

# loop 10 times
for input_count in range(10):
    
    # ask user for a number
    input_number = float(input("Enter a number: "))
    
    # check if the number is odd
    if input_number % 2 != 0:
        odd_count = odd_count + 1

# print the number of odd values
print("Odd numbers:", odd_count)