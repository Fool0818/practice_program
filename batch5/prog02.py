# ask the user to input a number
input_number = int(input("Enter a number (0-1000): "))

# convert number into 6 digit format with leading zeros
formatted_number = str(input_number).zfill(6)

# print the result
print(formatted_number)