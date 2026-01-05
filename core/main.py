from core.map_manager import MapManager
from core.path_manager import PathManager
from core.route_engine import RouteEngine
from core.preferences import PreferenceManager
from core.validator import Validator
from core.version_control import VersionControl
from core.categories import choose_category
from core.utils import success, error, info, warn, ascii_map
from core.logger import Logger


# ==========================================================
#  UNIVERSAL LOCATION PICKER (Number-based selection)
# ==========================================================
def choose_location(prompt="Select a location"):
    locs = MapManager.list_all_locations()
    if not locs:
        print(error("No locations available."))
        return None

    print("\n=== Available Locations ===")
    for i, loc in enumerate(locs, start=1):
        print(f"{i}. {loc}")

    choice = input(f"{prompt} (enter number): ").strip()

    if not choice.isdigit():
        print(error("Invalid input. Please enter a number."))
        return None

    choice = int(choice)

    if not (1 <= choice <= len(locs)):
        print(error("Choice out of range."))
        return None

    return locs[choice - 1]


# ==========================================================
#  MAIN APPLICATION LOOP
# ==========================================================
def main():
    while True:
        print(info("\n=== CAMPUS NAVIGATION SYSTEM ==="))
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

        # =============================
        # 1. ADD LOCATION
        # =============================
        if choice == "1":
            name = input("Enter Location Name: ").strip()

            category, msg = choose_category()
            if category is None:
                print(error(msg))
                continue

            try:
                x = int(input("X coordinate: "))
                y = int(input("Y coordinate: "))
            except ValueError:
                print(error("Coordinates must be integers."))
                continue

            ok, msg = MapManager.add_location(name, category, (x, y))
            print(msg)

        # =============================
        # 2. REMOVE LOCATION
        # =============================
        elif choice == "2":
            loc = choose_location("Select location to REMOVE")
            if loc:
                ok, msg = MapManager.remove_location(loc)
                print(msg)

        # =============================
        # 3. UPDATE LOCATION
        # =============================
        elif choice == "3":
            loc = choose_location("Select location to UPDATE")
            if not loc:
                continue

            print(info("Choose new category (or Other):"))
            new_cat, msg = choose_category()
            if new_cat is None:
                new_cat = None  # category unchanged

            x = input("New X (blank = skip): ").strip()
            y = input("New Y (blank = skip): ").strip()

            coords = (int(x), int(y)) if x and y else None

            ok, msg = MapManager.update_location(loc, new_cat, coords)
            print(msg)

        # =============================
        # 4. ADD PATH
        # =============================
        elif choice == "4":
            a = choose_location("Select Location A")
            b = choose_location("Select Location B")
            if a and b:
                ok, msg = PathManager.add_path(a, b)
                print(msg)

        # =============================
        # 5. REMOVE PATH
        # =============================
        elif choice == "5":
            a = choose_location("Select Location A")
            b = choose_location("Select Location B")
            if a and b:
                ok, msg = PathManager.remove_path(a, b)
                print(msg)

        # =============================
        # 6. LIST ALL LOCATIONS
        # =============================
        elif choice == "6":
            print(info(str(MapManager.list_all_locations())))

        # =============================
        # 7. SEARCH BY NAME
        # =============================
        elif choice == "7":
            q = input("Search Name: ").strip()
            print(info(str(MapManager.search_by_name(q))))

        # =============================
        # 8. SEARCH BY CATEGORY
        # =============================
        elif choice == "8":
            cat, msg = choose_category()
            if cat:
                print(info(str(MapManager.search_by_category(cat))))
            else:
                print(error(msg))

        # =============================
        # 9. VALIDATE CONNECTIVITY
        # =============================
        elif choice == "9":
            print(info(str(PathManager.validate_connectivity())))

        # =============================
        # 10. SHORTEST PATH
        # =============================
        elif choice == "10":
            start = choose_location("Start Location")
            end = choose_location("End Location")
            if start and end:
                print(info(str(RouteEngine.shortest_path(start, end))))

        # =============================
        # 11. FASTEST ROUTE
        # =============================
        elif choice == "11":
            start = choose_location("Start Location")
            end = choose_location("End Location")

            speed = input("Walking speed (km/h): ").strip()
            ok, msg = Validator.validate_speed(speed)
            if not ok:
                print(error(msg))
                continue

            speed = float(speed)
            route, t = RouteEngine.fastest_route(start, end, speed)
            print(info(str(route)), info(str(t)))

        # =============================
        # 12. ALTERNATIVE ROUTES
        # =============================
        elif choice == "12":
            start = choose_location("Start Location")
            end = choose_location("End Location")
            print(info(str(RouteEngine.alternative_routes(start, end))))

        # =============================
        # 13. SAVE PREFERENCES
        # =============================
        elif choice == "13":
            speed = input("Walking speed: ").strip()
            ok, msg = Validator.validate_speed(speed)
            if not ok:
                print(error(msg))
                continue

            mode = input("Mode (shortest/fastest): ").strip()
            PreferenceManager.save(float(speed), mode)
            print(success("Preferences saved."))

        # =============================
        # 14. LOAD PREFERENCES
        # =============================
        elif choice == "14":
            print(info(str(PreferenceManager.load())))

        # =============================
        # 15. BACKUP MAP
        # =============================
        elif choice == "15":
            print(success(VersionControl.save_version()))

        # =============================
        # 16. ASCII MAP DISPLAY
        # =============================
        elif choice == "16":
            ascii_map()

        # =============================
        # 17. EXIT
        # =============================
        elif choice == "17":
            break

        else:
            print(error("Invalid menu choice."))

        # Log every action
        Logger.log(f"Menu option chosen: {choice}")


if __name__ == "__main__":
    main()
