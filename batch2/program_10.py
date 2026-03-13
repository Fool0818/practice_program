# ask user to input the first number and second number
first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

# find the smaller and larger number
if first_number < second_number:
    start_number = first_number
    end_number = second_number
else:
    start_number = second_number
    end_number = first_number

# print numbers between them
for number_value in range(start_number + 1, end_number):
    print(number_value)