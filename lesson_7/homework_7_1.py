# Enter a country and save it to variable your_choice_country. Write find_index_by_value function which will check
# if the tuple countries contains a country of your choice. If your_choice_country is in the tuple, return its
# index, otherwise return a -1 value

countries = ('USA', 'Canada', 'United Kingdom', 'Mexico', 'Brazil', 'Argentina', 'Chili', 'South Africa', 'Egypt',
             'Morocco', 'India', 'China', 'Ukraine', 'Spain', 'France', 'Russia')
your_choice_country = 'Germany'

def find_index_by_value(value, tuple):
    for country in tuple:
        if country == value:
            return value
    return -1

# print(find_index_by_value(your_choice_country, countries))

# Change the previous exercise. Enter a random number and save it to variable your_choice_number. Write
# find_value_by_index function which will check if the tuple countries contains a country with this index.
# If there is a value with this index your_choice_number in the tuple, return this value,
# otherwise return a 'No such index' text

your_choice_number = 16

def find_value_by_index(index, tuple):
    if index < len(tuple):
        return tuple[index]
    else:
        return "No such index"

# print (find_value_by_index(your_choice_number, countries))

# Enter a pair of values in variables new_team_name, new_team_city. Then write add_your_own_team function
# to add them to nhl_hockey_teams dictionary, where the name will be the key.

new_team_name = "Wild Russians"
new_team_city = "Moscow"

nhl_hockey_teams = {
    "Canadiens": "Montreal",
    "Maple Leafs": "Toronto",
    "Red Wings": "Detroit",
    "Bruins": "Boston",
    "Blackhawks": "Chicago",
    "Oilers": "Edmonton",
    "Penguins": "Pittsburgh",
    "Islanders": "New York",
    "Rangers": "New York",
    "Devils": "New Jersey",
    "Avalanche": "Colorado",
    "Kings": "Los Angeles",
    "Flyers": "Philadelphia",
    "Ducks": "Anaheim",
    "Flames": "Calgary",
    "Hurricanes": "Carolina",
    "Stars": "Dallas",
    "Blues": "St. Louis",
    "Lightning": "Tampa Bay",
    "Capitals": "Washington"
}

def add_your_own_team(team_name, team_city):
    nhl_hockey_teams[team_name] = team_city
    return nhl_hockey_teams

# print(add_your_own_team(new_team_name,new_team_city))

# Create two dictionaries in dict_1, dict_2 variables. Write a join_dicts function to concatenate the following
# dictionaries to create a new one.

dict_1 = {'Kareem': 13, 'Hannah': 7, 'Haneen': 3}
dict_2 = {'Noor': 2, 'Malik': 1}

def join_dicts(dict1, dict2):
    dict2.update(dict1)
    return dict2

# print(join_dicts(dict_1, dict_2))

# # Enter a random number and save it to number_1 variable. Then write create_numbers_dict function to generate
# a dictionary that contains items with keys from 1 to number_1 and values in format "x": "x**2".

number_1 = 8

def create_numbers_dict(number1):
    my_dict = {}
    for i in range (1, number1+1):
        my_dict[i] = i**2
    return my_dict

# print (create_numbers_dict(number_1))

# Write sum_up_hockey_cups functions to sum all values in a dictionary dict_3.

dict_3 = {
    "Montreal Canadiens": 24,
    "Toronto Maple Leafs": 13,
    "Detroit Red Wings": 11,
    "Boston Bruins": 6,
    "Chicago Blackhawks": 6,
    "Edmonton Oilers": 5,
    "Pittsburgh Penguins": 5,
    "New York Islanders": 4,
    "New York Rangers": 4,
    "New Jersey Devils": 3,
    "Colorado Avalanche": 2,
    "Los Angeles Kings": 2,
    "Philadelphia Flyers": 2,
    "Anaheim Ducks": 1,
    "Calgary Flames": 1,
    "Carolina Hurricanes": 1,
    "Dallas Stars": 1,
    "St. Louis Blues": 1,
    "Tampa Bay Lightning": 1,
    "Washington Capitals": 1
}

def sum_up_hockey_cups(teams_dict, result = 0):
    for i in teams_dict:
        result += teams_dict[i]
    return result

# print (sum_up_hockey_cups(dict_3))

# Write remove_item_by_key function to remove a key True from dict_4 dictionary.

dict_4 = {
    "a": 231,
    "b": 'hello',
    True: False,
    42: 'answer'
}

def remove_item_by_key(dict1):
    dict1.pop(True)
    return dict1

# print(remove_item_by_key(dict_4))


dict_5 = {
    "Cyprus": 1207359,
    "Czechia": 10708981,
    "Democratic Republic of the Congo": 89561403,
    "Denmark": 5792202,
    "Djibouti": 988000,
    "Dominica": 71986,
    "Dominican Republic": 10847910,
    "Ecuador": 17643054,
    "Egypt": 102334404,
    "El Salvador": 6486205,
    "Equatorial Guinea": 1402985,
    "Eritrea": 3546421,
    "Estonia": 1326535,
    "Eswatini": 1160164,
    "Ethiopia": 114963588,
    "Fiji": 896445,
}

def find_min_max(dict1):
    all_values = dict1.values()
    return min(all_values), max(all_values)

# print(find_min_max(dict_5))


# Write remove_duplicates functions to remove duplicates from dictionary dict_6.

dict_6 = {
    "Lessie": "collie",
    "Marlie": "labrador",
    "Spike": "boxer",
    "Buddy": "labrador",
    "Milo": "labrador",
    "Archie": "corgi",
    "Tobby": "pit bull",
    "Jack": "poodle",
    "Lucy": "german shepherd",
    "Bailey": "labrador"
}


def remove_duplicate_values(dictionary):
    val_list = []
    result_dict = {}
    for key, val in dictionary.items():
        if val not in val_list:
            val_list.append(val)
            result_dict[key] = val
    return result_dict

# print(remove_duplicate_values(dict_6))

