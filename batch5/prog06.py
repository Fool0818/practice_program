# ask the user to input their fullname
full_name = input("Enter your fullname: ")

# variable to store reversed casing
reversed_case_name = ""

# loop through each character
for character_value in full_name:

    # check if character is lowercase
    if character_value.islower():
        reversed_case_name = reversed_case_name + character_value.upper()

    # check if character is uppercase
    elif character_value.isupper():
        reversed_case_name = reversed_case_name + character_value.lower()

    else:
        reversed_case_name = reversed_case_name + character_value

# print the result
print(reversed_case_name)