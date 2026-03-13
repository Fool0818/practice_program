# ask the user to input their fullname
full_name = input("Enter your fullname: ")

# convert to lowercase and replace spaces with underscore
snake_case_name = full_name.lower().replace(" ", "_")

# print the result
print(snake_case_name)