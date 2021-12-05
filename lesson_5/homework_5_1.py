# FUNCTIONS

# Difference
# Write a function, which will calculate the difference of these two numbers

def difference(num_1, num_2):
    return num_1 - num_2
    print(difference(5, 2))

# Division
# Write a function, which will divide these two numbers

def division(num_1, num_2):
    if num_2 == 0:
        return "Division by 0 is forbidden"
    else:
        return num_1 / num_2
        print (division(5, 2))


# Function gets random number. If this number is more than ten, return the difference between 100 and this number,
# otherwise return this number multiplied by 10

def function_1(number):
    if number > 10:
        return number - 100
    else:
        return number * 10
        print(function_1(50))


# Your function temperature_converter gets the temperature in Fahrenheit, convert it to Celsius and return.
# Formula (32°F − 32) × 5/9 = 0°C

def temp_converter(fahrenheit_degree):
    return round((fahrenheit_degree - 32)*(5/9), 2)
    print(temp_converter(98))


# Taxi Fare
# In a particular jurisdiction, taxi fares consist of a base fare of $4.00, plus $0.25 for every 140 meters travelled.
# Write a function that takes the distance travelled (in kilometers) as its only parameter and returns the total fare
# as its only result rounded by 2 digits. Write a program that demonstrates the function.

def taxi_fare(distance_km):
    total_fare = 4 + (distance_km * 1000 / 140) * 0.25
    return round(total_fare, 2)
    print(taxi_fare(10))

# examples of usage:
# taxi_fare(10) #21.86