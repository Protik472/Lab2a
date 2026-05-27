print("Hello, World!")

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67,32)")

def get_user_input():
    # 1. Read from the terminal console
    user_string = input()
    
    # 2. Split the string into a list of strings based on the comma
    string_list = user_string.split(",")
    
    # 3. Convert the list of strings to a list of floats
    float_list = []
    for item in string_list:
        float_list.append(float(item))
        
    # 4. Return the list of floats
    return float_list

def calc_average_temperature(temperature_list):
    # Calculate the average by dividing the sum by the number of items
    total = sum(temperature_list)
    average = total / len(temperature_list)
    return average

def calc_min_max_temperature(temperature_list):
    # Find the minimum and maximum values
    min_temp = min(temperature_list)
    max_temp = max(temperature_list)
    
    # Table 5 explicitly asks for an "integer list", so we convert them to ints
    return [int(min_temp), int(max_temp)]

def sort_temperature(temperature_list):
    print("sort_temperature")

def calc_median_temperature(temperature_list):
    print("calc_median_temperature")