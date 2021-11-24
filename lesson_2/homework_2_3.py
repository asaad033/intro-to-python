# Write your first program. Enter the temperature right now in Fahrenheit in temperature_fahrenheit variable as
# a string (e.g. '75') and convert it to Celsius.
# !important you should save only number to result_temperature. Formula (32°F − 32) × 5/9 = 0°C
# type your code here

temp_f = int(input("Please enter any temperature in Fahrenheit \n that you would like converted into Celsius: "))
result_temp = (temp_f - 32) * (5/9)
print (round(result_temp, 2))