import math

# Round a off to three decimal places.

a = 10.04789
result_1 = round(a,3)
print(result_1)


# Round up result_2 to greater value.

result_2 = (5 / 2 * 6 + 1.25 - 4)
#print(result_2)
result_2 = math.ceil(result_2)
#print(result_2)


# Round up result_3 to lesser value.

result_3 = 8 / 3 * 5 + 4.75 - 7
print(result_3)
result_3 = math.floor(result_3)
print(result_3)

