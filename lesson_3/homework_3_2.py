# Enter a number between 1 and 20, save this value to number variable.
# If number is greater than 0 and less than or equal to 7, save the number * 10 to result_1.
# If number is  greater than 7 and less than or equal to 15, save the result of floor division of the number divided by
# 3 to result_1 variable
# If number is  greater than 15 and less than or equal to 20, save the number raised to the power 3 to result_1
# Else save the text "Wrong value" to result_1
# EXERCISE 1

import math

'''number = int(input("Please enter a number between 1 and 20: "))

if number > 0 and number <= 7:
    result = number * 10
elif number > 7 and number <= 15:
    result = math.floor(number/3)
elif number > 15 and number <= 20:
    result = number ** 3
else:
    result = "wrong value"

print(result)'''

# Enter two numbers between 1 and 10, save this values to number_1 variable and number_2 variables.
# If number_1 and number_2 are greater than 0 and less than or equal to 5 save in the product of their multiplication
# to result_2
# If one of the variables (number_1 or number_2) is greater than 5 and less than or equal to 10, but the other isn't,
# then save the sum of the two numbers to result_2
# If both numbers are greater than 5 and less than or equal to 10, multiply their sum by 3 and save it to result_2
# Else save the text "Wrong values, try again" to result_2
# EXERCISE 2

'''number_1 = int(input("Please enter a number between 1 and 10: "))
number_2 = int(input("Please enter another number between 1 and 10: "))

if  (number_1 > 10 or number_2 > 10 or number_1 < 1 or number_2 < 1):
    result_2 = "Wrong Values, try again"
elif number_1 > 0 and number_2 > 0  and number_1 <= 5 and number_2 <= 5:
    result_2 = number_1 * number_2
elif ((number_1 > 5 and number_1 <= 10) and not (number_2 > 5 and number_2 <= 10)) or\
     ((number_2 > 5 and number_2 <= 10) and not (number_1 > 5 and number_1 <= 10)):
    result_2 = number_1 + number_2
else:
    number_1 > 5 and number_1 <= 10 and number_2 > 5 and number_2 <= 10
    result_2 = (number_1 + number_2) * 3

print (result_2)'''

# Enter your first name and save it to first_name variable,
# then Enter last name and save it to last_name
# If first_name or last_name are shorter than 6 characters, save a full name (with a space between) to result_3
# Else save first_name to result_3 as many times as length of last_name value
# EXERCISE 3

'''first_name = "Alia"
last_name = "Saad"

if len(first_name) < 6 or len(last_name) < 6:
    full_name = first_name + " " + last_name
else:
    full_name = first_name * len(last_name)

print(full_name)'''


# Enter a random number. Save this value to random_number variable
# If this number is less 10 or greater than 99, save the text "Please, put in a number between 10 and 99" to result_4
# If a number doesn't meet the first condition, find the remainder of random_value divided by 2.
# If it is 0, save the text "Even number" to result_4 , else save the message "Odd number"
# EXERCISE 4

'''random_number = int(input("Please input a random number between 10 and 99: "))

if random_number < 10 or random_number > 99:
    result_4 = "Please, put in a number between 10 and 99"
elif (random_number >= 10 or random_number <= 99) and (random_number % 2 == 0):
    result_4 = "Even number"
else:
    result_4 = "Odd number"

print(result_4)'''
