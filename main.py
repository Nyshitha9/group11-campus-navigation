from core.file_handler import FileHandler

def main():
    FileHandler.load_map()

    while True:
        print("\n=== CAMPUS NAVIGATION SYSTEM ===")
        print("1. Add Location")
        print("2. Remove Location")
        print("3. Update Location")
        print("4. Add Path")
        print("5. Remove Path")
        print("6. List All Locations")
        print("7. Search Location by Name")
        print("8. Search by Category")
        print("9. Validate Connectivity")
        print("10. Shortest Route")
        print("11. Fastest Route")
        print("12. Alternative Routes")
        print("13. Save Preferences")
        print("14. Load Preferences")
        print("15. Backup Map")
        print("16. Show ASCII Map")
        print("17. Exit")

        choice = input("Choice: ").strip()
        if choice == "17":
            break
