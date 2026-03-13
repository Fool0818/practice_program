# ask the user to input the first number and second number
first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))

# check which number is bigger
if first_number > second_number:
    print("Bigger number:", first_number)
elif first_number == second_number : # check if both numbers are equal
	print("Both numbers are equal")
else:
    print("Bigger number:", second_number)