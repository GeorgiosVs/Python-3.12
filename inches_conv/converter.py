class Converter:
    @staticmethod
    def feet_and_inches_to_cm(feet, inches):
        cm_per_inch = 2.54
        inches_per_foot = 12
        total_inches = feet * inches_per_foot + inches
        total_cm = total_inches * cm_per_inch
        return total_cm

    @staticmethod
    def print_conversion(feet, inches, cm):
        print(f"{feet} feet and {inches} inches is equal to {cm:.2f} centimeters")