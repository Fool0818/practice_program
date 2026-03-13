# ask the user to input a complete statement
input_statement = input("Enter a statement: ")

# split the statement into words
word_list = input_statement.split()

# count the number of words
word_count = len(word_list)

# print the result
print(word_count)