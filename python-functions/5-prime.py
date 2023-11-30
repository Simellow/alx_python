def is_prime(number):
    # number has to be greater than 1
    number > 1
    # divide numbers starting from 2 to number inputted 
    for x in range (2, number):
        if number % x == 0:
            False
    #stop loop if condition is met
            break
        else: 
            True

