# CY30O-Project
Project for CY300

Project Title: Space Mission Analysis
-------------------------------------------
Authors: Cadet Rhemmy Chen, Cadet Gabriel Harrison, Cadet Matthew Kim
Date: December 13, 2024

1. Overview
-----------
This command-line application allows users to explore a dataset of space flights 
from different space companies, along with their respective attributes.
Users can perform the following tasks:
- Load all data.
- View 5 summary statistics for the main 7 variables (e.g., Temperature (Â° F),
Wind speed (MPH), Humidity (%), Liftoff Thrust (kN), Payload to Orbit (kg),
Rocket Height (m), Fairing Diameter (m)).
	- Mean, median, mode, max, min.
- Apply variable filters to view specific subsets of the data, inclusive to all
variables in the dataset (e.g., Launch Time, Mission Status, Payload Orbit).
- Reset all filters made previously.
- Generate visualizations of the data depicting variable relationships using 
Matplotlib (e.g., Rocket Height(m) vs Fairing Diameter(m) and
Liftoff Trhust(kN) vs Payload to Orbit(kg))
- Save filtered data to a new file.
- Show all existing headers.

2. Files
--------
- `main.py`: The main script to run the program, containing the menu and program
flow.
- `data_processing.py`: A module with functions for data loading, filtering, and
calculations.
- `SpaceMissions.csv`: The dataset used in this project.
- `filtered_data.csv`: CSV file that contains user-requested filtered data.
- `README.txt`: Instructions for running and using the program (this file).
- -Ensure that the folder containing `main.py`, `data_processing.py`, and `SpaceMissions.csv` is opened in the editor - not a higher folder
3. Running the Program
----------------------
To run the program:
1. Open a terminal or command prompt.
2. Input a number in the terminal in relation to the associated data in the displayed
menu until requested data is shown. 
3. Press 'E' to exit.
No additional arguments are required.

4. Dependencies
---------------
The program requires Python 3.7 or higher. Ensure the following libraries are
installed:
- `csv` (built-in)
- `data_processing` (built-in)
- `sys` (built-in)
- `matplotlib`
To install Matplotlib, use: pip install matplotlib

5. Input
--------
The program reads the dataset `SpaceMissions.csv` by default. No user-provided input
files are required.

6. Output
---------
The filtered data that is created by the user can be saved to a new file, specified by
the user during the program's execution. The output will be in CSV format.

7. Contact
----------
If you encounter issues running the program, please contact Cadet Matthew Kim at
matthew.kim@westpoint.edu.
