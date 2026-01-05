class Validator:

    @staticmethod
    def validate_location_name(name):
        if not isinstance(name, str):
            return False, "Name must be a string"
        if name.strip() == "":
            return False, "Name cannot be empty"
        if any(c in "!@#$%^&*()" for c in name):
            return False, "Invalid characters in name"
        return True, ""

    @staticmethod
    def validate_coordinates(coords):
        if not isinstance(coords, tuple) or len(coords) != 2:
            return False, "Coordinates must be a tuple (x, y)"
        x, y = coords
        if not (0 <= x <= 5000 and 0 <= y <= 5000):
            return False, "Coordinates out of range"
        return True, ""
    
    @staticmethod
    def validate_speed(speed):
        try:
            speed = float(speed)
            if speed <= 0:
                return False, "Speed must be > 0"
            if speed > 10:
                return False, "Speed too high"
            return True, ""
        except:
            return False, "Invalid speed input"

    @staticmethod
    def validate_route_input(start, end):
        if not isinstance(start, str) or not isinstance(end, str):
            return False, "Route locations must be strings"
        if start.strip() == "" or end.strip() == "":
            return False, "Route locations cannot be empty"
        if start == end:
            return False, "Start and end locations must be different"
        return True, ""
