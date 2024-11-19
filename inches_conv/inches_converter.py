from inches_conv.converter import Converter

converter = Converter()

feet = 5
inches = 8

# Call the instance methods on the converter instance
cm = converter.feet_and_inches_to_cm(feet, inches)
converter.print_conversion(feet, inches, cm)