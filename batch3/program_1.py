numbers = []  

# input exactly 10 integers
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))  # get integer input
    numbers.append(num)  # store number

# check each number
for num in numbers:
    if numbers.count(num) == 1:  # appears only once
        print(num)  # display numbers with no duplicates