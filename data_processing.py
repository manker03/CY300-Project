#Project 1 CY300 
#CDT Matthew Kim and CDT Rhemmy Chen
#Outline, Notes, Etc
import csv
"""
General To Do list:
TODO: Create a "column" object?
TODO: Create a "cell" object
"""
"""
These first five  functions serve as the basic summary statistic
functions. Each wil return a float calcualted from a given column
TODO: Implement math for each function
TODO: Fiure out what kind of datatype/object each column should be (strig? its own object?)
"""
#get the mean of a certain column
def get_mean(column) -> float:
    #For cell in column, total += cell, mean  = total / count
    pass

#get the median of a certain column
def get_median(column) -> float:
    pass

#get the mode of a certain column
def get_mode(column) -> float:
    pass

#get the max of a certain column
def get_max(column) -> float:
    pass

#get the min of a certain column
def get_min(column) -> float:
    pass

"""
The next methods will handle data collection and usage as it pertains
to plotting and graphing it
"""
#create the plot and display it to the user from two columns (lists)
def create_plot(column1, column2):
    pass

"""
The following helper methods will be used to handle any irregularities
in the data such as a null cell, a non-standard cell datatype, or anything
else unexpected
"""
#filters out the null values in a column, and returns a new column that only includes non-null cells
def filter_null(column) : #returns a column?
    pass

#Converts time values from a XX:XX format to a total minutes format for easier calculations
def standardize_time(cell):
    pass

#Converts date values from XX-MON-XX format to a standardized XX-XX-XX format
def standardize_date(cell):
    pass
"""
Core Functions for the project
"""
#get the two columns (lists) of data to plot against 
def load_data(filename:str) -> list:
    with open (filename, 'r') as f:
        csvreader = csv.reader(f)
        headers = next(csvreader)
        data = [row for row in csvreader]
        print(f"{headers}")
        print(f"{data}")

#display summary statistics
def display_summary_stats():
    print(f"Summary Stats - PLACEHOLDER")

#apply filters
def apply_filters():
    print("Filters Applied - PLACEHOLDER")

#Reset filters
def reset_filters():
    print("Filters Reset - PLACEHOLDER")

#Generate Visualizations
def generate_visualizations():
    print("Visualizations Generated - PLACEHOLDER")

#Saving data
def save_data():
    print("Data saved - PLACEHOLDER")

#Exit program
def exit_program():
    print("Exiting - PLACEHOLDER")