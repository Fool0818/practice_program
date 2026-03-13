# ask the user to input their fullname
full_name = input("Enter your fullname: ")

# convert to proper case then remove spaces
pascal_case_name = full_name.title().replace(" ", "")

# print the result
print(pascal_case_name)