# Enter two numbers. If the first one is greater than the second, save first number in result_1,
# otherwise save the second number to the result_1 variable.
# EXERCISE 1

'''first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

if first_number > second_number:
    result_1 = first_number
else:
    result_1 = second_number
print(result_1)'''

# Enter a random number in number_1 variable. If this number is 20 or
# higher save “Too high” text to result_2, otherwise save “Thank you”.
# EXERCISE 2

'''number_1 = int(input("Please enter a random number: "))

if number_1 >= 20:
    result_2 = "Too high"
else:
    result_2 = "Thank you"
print(result_2)'''

# Enter your first name and last name in first_name and last_name variables. If the length of your first name is under
# five characters, join them together (without a space) and save it to result_3 variable in upper case. If the length
# of the first name is five or more characters, save their first name in lower case in result_3 variable.
# EXERCISE 3

'''first_name = "Alia"
last_name = "Saad"
if len(first_name) < 5:
    result_3 = (first_name + last_name).upper()
else:
    result_3 = first_name.lower()
print(result_3)'''

# Enter a number between 10 and 20 (inclusive) and save number to number_2 variable
# If they enter a number within this range, save a message “Thank you” to result_4, otherwise a
# message “Incorrect answer” to result_4.
# EXERCISE 4

'''number_2 = int(input("Please enter a number between 10 and 20: "))

if number_2 <= 20 and number_2 >= 10:
    result_4 = "Thank you"
else:
    result_4 = "Incorrect, Try again!"
print (result_4)'''

# Enter your age. If you are 18 or over, save the message “You can vote” in result_5,
# if you are aged 17, save the message “You can learn to drive” in result_5 variable,
# if you are 16, save the message “You can buy a lottery ticket” in result_5,
# if you are under 16, save the message “You can go Trick-or-Treating” in result_5 variable.
# EXERCISE 5

'''age = int(input("Enter your age: "))

if age >= 18:
    print("You can vote!")
elif age == 17:
    print("You can learn to drive!")
elif age == 16:
    print ("You can bug a lottery ticket!")
elif age <= 15:
    print ("You can go Trick-or-Treating!")'''

# Enter a number between 1 and 12, save this value to month variable. Find which month is it.
# (January, February, March, April, May, June, Jule, August, September, October, November, December)
# Write answer in result_month in lower case
# EXERCISE 6

''' month = int(input("Please enter a number between 1 and 12: "))

if month == 1:
    print("January")
elif month == 2:
    print ("February")
elif month == 3:
    print ("March")
elif month == 4:
    print ("April")
elif month == 5:
    print ("May")
elif month == 6:
    print ("June")
elif month == 7:
    print ("July")
elif month == 8:
    print ("August")
elif month == 9:
    print ("September")
elif month == 10:
    print ("October")
elif month == 11:
    print ("November")
elif month == 12:
    print ("December")
else:
    print ("Invalid Input") '''