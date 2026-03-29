numbers = []  
unique_numbers = [] 

# input 10 integers
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))  # get integer
    numbers.append(num)  # store

# keep only first occurrence
for num in numbers:
    if num not in unique_numbers:  # if not yet added
        unique_numbers.append(num)  # store unique

print("Numbers without duplicate repeats:")  

# display result
for num in unique_numbers:
    print(num)