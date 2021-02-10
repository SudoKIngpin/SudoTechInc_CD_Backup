#Question3

def feet_to_inch(feet):
    inch=feet*12
    return inch

def display_feet(__feet):
    return(__feet)
    
def _inch(inches):
    print(inches)
feet_input=int(input("Enter number of feet: "))
calc_inches=feet_to_inch(feet_input)
print("No of inches in  {} feet  => {} ".format(feet_input,calc_inches))
