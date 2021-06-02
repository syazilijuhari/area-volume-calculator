# define a function for calculating
# the area of a shapes
def calculate_volume(name):\

    # converting all characters
    # into lower cases
    name = name.lower()

    if name == "cylinder":
        height = float(input("Enter cylinder's height: "))
        rad = float(input("Enter cylinder's radius: "))
        pi = 3.14

        cyl_vol = pi * rad * rad * height
        print(f"The area of rectangle is {cyl_vol}.")

    elif name == "sphere":
        rad = float(input("Enter sphere's radius: "))
        pi = 3.14

        sphere_vol = 1.33 * pi * rad * rad * rad
        print(f"The area of rectangle is {sphere_vol}.")

    elif name == "cone":
        height = float(input("Enter "))
        rad = float(input("Enter sphere's radius: "))
        pi = 3.14

        cone_vol = 0.33 * pi * rad * rad * height
        print(f"The area of rectangle is {cone_vol}.")
    
    else:
        print("Sorry! This solid is not available")

if __name__ == "__main__":
    print("Calculate Volume of Solids")
    solid_name = input("Enter the type of solid: ")

    calculate_volume(solid_name)
