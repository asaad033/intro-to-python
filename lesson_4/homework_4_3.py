# WHILE LOOPS EXERCISES

# Enter a random string in the variable string_1, then enter a character and save it in the variable char_1.
# Write code, which will count how many times your character is included in your string.
# Save result to result_1 variable

string_1 = 'abbcccdddd'
char_1 = 'b'
result_1 = 0

for i in range (0, len(string_1)):
    if char_1 == string_1[i]:
        result_1 += 1
print(result_1)


# Enter a random number and save it in variable number_1. Then create code to multiply all the digits together
# and save result in the result_2 variable.

number_1 = '1234'
result_2 = 1

for i in range (0, len(number_1)):
    result_2 = result_2 * int(number_1[i])
print(result_2)


# Enter a random number and save it in variable number_2. Then create code which will return
# a number with digits of number_1 in reverse order. Save it in result_3 variable

number_2 = '456'
result_3 = ''

for i in range(len(number_2)-1, -1, -1):
    result_3 += number_2[i]
print(result_3)