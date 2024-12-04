import data_processing
"""
main method
"""

def main():
    
    headers = []
    data = []
    filename = r"C:\Users\matthew.kim\OneDrive - West Point\Desktop\USMA Academics\AY 25-1\CY 300\Project Folder\SpaceMissions.csv"
    while True:
        print("Menu Options:")
        print("1. Load Data")
        print("2. Display Summary Statistics")
        print("3. Apply Filters")
        print("4. Reset Filters")
        print("5. Generalize Visualizations")
        print("6. Save Data")
        print("E - Exit")
        choice = input("Enter your choice (1 - 6), or E to exit: ")

        if choice == "1":
            data_processing.load_data(filename)
        elif choice == "2":
            data_processing.display_summary_stats()
        elif choice == "3":
           data_processing.apply_filters()
        elif choice == "4":
            data_processing.reset_filters()
        elif choice == "5":
            data_processing.generate_visualizations()
        elif choice == "6":
            data_processing.save_data()
        elif choice == "E" or choice == "e":
            data_processing.exit_program()
        else:
            print("Please choose another options")

if __name__ == "__main__":
    main()