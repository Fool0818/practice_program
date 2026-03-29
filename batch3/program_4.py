numbers = []  

while True:  # continuous input
    user_input = input("Enter a number (or invalid to stop): ")  # ask input

    try:
        num = float(user_input)  # convert to float
        numbers.append(num)  # store number
    except:
        break  # stop if invalid

if len(numbers) > 0:  # check if list not empty
    print("Lowest number:", min(numbers))  # display smallest value
else:
    print("No numbers entered.")  # if no input