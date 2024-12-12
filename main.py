import data_processing
"""
main method
"""

def main():

    filename = r"SpaceMissions.csv"
    while True:
        #Display the menu
        print("Menu Options:")
        print("1. Load Data")
        print("2. Display Summary Statistics")
        print("3. Apply Filters")
        print("4. Reset Filters")
        print("5. Generalize Visualizations")
        print("6. Show Headers")
        print("E - Exit")
        
        #Get user input
        choice = input("Enter your choice (1 - 7), or E to exit: ")

        #Menu choices
        if choice == "1":
            data_processing.load_data(filename)
        elif choice == "2":
            data_processing.display_summary_stats(filename)
        elif choice == "3":
           data_processing.show_headers(filename)
           data_for_filter = input("Select multiple header names seperated by commas:")
           data_processing.apply_filters(filename, data_for_filter) #Unfinished
        elif choice == "4":
            data_processing.reset_filters() #Unfinished
        elif choice == "5":
            print("Visualization Options:")
            print("1. Rocket Height(m) vs Fairing Diameter(m)")
            print("2. Temperature (F) vs Humidity (%)")
            print("3. Liftoff Trhust(kN) vs Payload to Orbit(kg)")
            vis_choice = input("Select a visualization option (1-3): ")

            if vis_choice == "1":
                data_processing.generate_visualizations(
                    filename, 
                    "Rocket Height (m)", 
                    "Fairing Diameter (m)"
                )
            elif vis_choice == "2":
                data_processing.generate_visualizations(
                    filename, 
                    "Temperature (Â° F)", 
                    "Humidity (%)"
                )
            elif vis_choice == "3":
                data_processing.generate_visualizations(
                    filename, 
                    "Liftoff Thrust (kN)", 
                    "Payload to Orbit (kg)"
                )
            else:
                print("Invalid selection. Returning to main menu.")
        elif choice == "6":
            data_processing.show_headers(filename)
        elif choice == "E" or choice == "e":
            data_processing.exit_program()
        else:
            print("Please choose another options")

if __name__ == "__main__":
    main()