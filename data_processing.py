#Project 1 CY300 
#CDT Matthew Kim and CDT Rhemmy Chen
#Outline, Notes, Etc
import csv
import sys
from matplotlib import pyplot as plt 
import numpy as np
"""
These first five  functions serve as the basic summary statistic
functions. Each wil return a float calcualted from a given column
"""
summary_stats_columns = [
    "Temperature (Â° F)",
    "Wind speed (MPH)",
    "Humidity (%)",
    "Liftoff Thrust (kN)",
    "Payload to Orbit (kg)",
    "Rocket Height (m)",
    "Fairing Diameter (m)"
    ]
"""
Calculates and returns the mean of a given colun
Parameters:
    column: column or list of numbers
Returns: the mean as a float
"""
def get_mean(column:list) -> float:
    mean = sum(column) / len(column)
    return round(mean, 2)

"""
Calculates and returns the median of a given column
Parameters:
    column: column or list of numbers
Returns: the median as a float
"""
def get_median(column:list) -> float:
    column.sort()
    length = len(column)
    middle = length // 2

    if length % 2 == 0:
        return round((column[middle - 1] + column[middle]) / 2, 2)
    else:
        return column[middle]

"""
Calculates and returns the mode of a given column
Parameters:
    column: column or list of numbers
Returns: the mode as a float
"""
def get_mode(column:list) -> float:
    count = {}  #Dictionary matches the values in a column with how many times they each show up
    for val in column:
        if val in count:
            count[val] += 1
        else:
            count[val] = 1

    mode = 0 #the answer
    max_count = 0 #shows up the most
    for val, count in count.items(): #Traverse through count.items. If the count of that item is higher than what's currently in max count, it becomes max count. mode changes accordingly. 
        if count > max_count:
            max_count = count
            mode = val
    return mode
        
"""
Calculates and returns the max of a given column
Parameters:
    column: column or list of numbers
Returns: the max as a float
"""
def get_max(column:list) -> float:
    return max(column)

"""
Calculates and returns min median of a given column
Parameters:
    column: column or list of numbers
Returns: the min as a float
"""
def get_min(column:list) -> float:
    return min(column)

#core functions for the program

"""
Loads data from a CSV file and prints the headers and rows.
Parameters:
    filename: a string representing the name of the CSV file
Returns:
    A list of rows from the file
"""
def load_data(filename:str) -> list:
    with open (filename, 'r') as f:
        csvreader = csv.reader(f)
        headers = next(csvreader)
        data = [row for row in csvreader]
        print(f"{headers}")
        print(f"{data}")

def show_headers(filename:str) -> list:
    with open (filename, 'r') as f:
        csvreader = csv.reader(f)
        headers = next(csvreader)
        print("Headers:")
        for pos, header in enumerate(headers, start = 1):
            print(f"{pos}. {header}")
        return headers
"""
Loads data from a column in a csv file
Parameters:
    filename: a string representing the name of the CSV file
    colname: the name of the column we want data from
Returns:
    the data as a list 
"""
def get_col_data(filename, colname) -> list:
    data = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            value = row.get(colname, 'NA')
            if value not in ['NA', ''] and value.replace('.', '', 1).isdigit():
                data.append(float(value))
            elif value not in ['NA', '']:
                data.append(value)
    return data

"""
Displays a summary of calculated statistics for the dataset.
Parameters:
    filename: a string representing the filename
Returns:
    None
"""
def display_summary_stats(filename:str) -> None:
    print("Options:")
    for pos, col_name in enumerate(summary_stats_columns, start = 1):
        print(f"{pos}. {col_name}")
    
    choice = input(f"Select a column to get it summary statistics (1 - 7)")
    if choice == "1":
        column_name = "Temperature (Â° F)"
    elif choice == "2":
        column_name = "Wind speed (MPH)"
    elif choice == "3":
        column_name = "Humidity (%)"
    elif choice == "4":
        column_name = "Liftoff Thrust (kN)"
    elif choice == "5":
        column_name = "Payload to Orbit (kg)"
    elif choice == "6":
        column_name = "Rocket Height (m)"
    elif choice == "7":
        column_name = "Fairing Diameter (m)"
    else:
        print("Invalid selection. Returning to main menu.")

    data = get_col_data(filename, column_name)
    print(f"\nSummary Statistics for {column_name}:")
    print(f"Mean: {get_mean(data)}")
    print(f"Median: {get_median(data)}")
    print(f"Mode: {get_mode(data)}")
    print(f"Max: {get_max(data)}")
    print(f"Min: {get_min(data)}")
"""
Applies filters to the dataset as specified by the user.
Parameters:
    None
Returns:
    None
"""
def apply_filters(filename:str, wanted_headers:str) -> None:
    wanted_headers_list = []
    idx_and_header_dict = dict()
    headers_list = []
    filtered_data = []
    with open('SpaceMissions.csv', mode='r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        for header in headers:
            headers_list.append(header)
        wanted_headers_list = [int(x.strip()) for x in wanted_headers.split(',')]
        for num in wanted_headers_list:
            if 1 <= num <= len(headers_list):
                idx_and_header_dict[num] = headers_list[num-1]
        print(f"{idx_and_header_dict}")

        for colname in idx_and_header_dict.values():
            print(colname)
            data = get_col_data(filename, colname)
            filtered_data.append(data)
        
        print(wanted_headers_list)
        print(filtered_data)
        fieldnames = wanted_headers_list
        with open('filtered_data.csv', mode= "w") as fout:
            writer = csv.writer(fout)
            
            writer.writerows(filtered_data)
"""
Resets all applied filters on the dataset.
Parameters:
    None
Returns:
    None
"""
def reset_filters() -> None:
    print("File emptied")
    with open('filtered_data.csv', mode= "w") as fout:
        writer = csv.writer(fout)
"""
Generates visualizations for the dataset based on selected columns.
Parameters:
    None
Returns:
    None
"""
def generate_visualizations(filename, col_x, col_y):
    #Empty lists for 2 columns
    x_data = []
    y_data = []

    with open(filename, 'r') as f:
        csvreader = csv.DictReader(f)
        for row in csvreader:
            x_val = row.get(col_x, '')
            y_val = row.get(col_y, '')
            if x_val not in ['NA', ''] and y_val not in ['NA', '']:
                x_data.append(float(x_val))
                y_data.append(float(y_val))

    # Plot the data
    plt.scatter(x_data, y_data, color='blue', label='Data Points')
    plt.xlabel(col_x)
    plt.ylabel(col_y)
    plt.title(f"{col_x} vs {col_y}")
    plt.show()


"""
Exits the program.
Parameters:
    None
Returns:
    None
"""
def exit_program():
    print("Exiting")  
    sys.exit()
