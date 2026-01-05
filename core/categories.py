CATEGORIES = [
    "Academic",
    "Administrative",
    "Hostel",
    "Library",
    "Laboratory",
    "Sports",
    "Canteen",
    "Parking",
    "Garden",
    "Other"
]

def choose_category():
    print("\n=== Choose Category ===")
    for i, cat in enumerate(CATEGORIES, start=1):
        print(f"{i}. {cat}")

    choice = input("Enter option number: ").strip()

    if not choice.isdigit():
        return None, "Invalid number."

    choice = int(choice)

    if not (1 <= choice <= len(CATEGORIES)):
        return None, "Option out of range."

    category = CATEGORIES[choice - 1]

    if category == "Other":
        custom = input("Enter custom category: ").strip()
        if not custom:
            return None, "Custom category cannot be empty."
        return custom, ""

    return category, ""
