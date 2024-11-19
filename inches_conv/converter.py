class Converter:
    def feet_and_inches_to_cm(self, feet, inches):
        cm_per_inch = 2.54
        inches_per_foot = 12
        total_inches = feet * inches_per_foot + inches
        total_cm = total_inches * cm_per_inch
        return total_cm

    def print_conversion(self, feet, inches, cm):
        print(f"{feet} feet and {inches} inches is equal to {cm:.2f} centimeters")
        pass