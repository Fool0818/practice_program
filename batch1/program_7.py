# variable to store the total sum
total_sum = 0

# loop 10 times to ask for numbers
for input_count in range(10):
    
    # ask user for a number
    input_number = float(input("Enter a number: "))
    
    # add the number to the total sum
    total_sum = total_sum + input_number

# print the final sum
print("Sum:", total_sum)