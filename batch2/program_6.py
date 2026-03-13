# list to store numbers
number_list = []

# ask user to input 10 numbers
for input_count in range(10):
    input_number = int(input("Enter a number: "))
    number_list.append(input_number)

# start with the first number
result_value = number_list[0]

# subtract the remaining numbers
for stored_number in number_list[1:]:
    result_value = result_value - stored_number

# display the result
print("Result:", result_value)