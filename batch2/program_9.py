# loop from 0 to 100
for number_value in range(0, 101):

    # check if number does not end in 0 or 5
    if number_value % 10 != 0 and number_value % 10 != 5:
        print(number_value)