# variable to count even numbers
even_count = 0

# ask user to input 10 numbers
for input_count in range(10):
    input_number = int(input("Enter a number: "))
    
    # check if the number is even
    if input_number % 2 == 0:
        even_count = even_count + 1

# display the total even numbers
print("Even numbers:", even_count)