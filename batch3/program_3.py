numbers = []  

while True:  # loop until invalid input
    user_input = input("Enter a number (or invalid to stop): ")  # get input

    try:
        num = float(user_input)  # convert to float (supports decimal/negative)
    except:
        break  # stop if invalid input

    if num in numbers:  # check if already entered
        print("Duplicate") 
    else:
        print("Unique")  # first time seen
        numbers.append(num)  # store number