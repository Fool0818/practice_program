# ask the user to input their fullname with spaces at the beginning
full_name = input("Enter your fullname: ")

# remove spaces at the beginning
clean_name = full_name.lstrip()

# print the result
print(clean_name)