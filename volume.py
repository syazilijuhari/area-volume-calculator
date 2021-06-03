import math
def prt(nama,x):
	return "The area of "+nama+" is "+"{:.3f}".format(x)
# define a function for calculating
# the area of a shapes
def calculate_volume(name):
    # converting all characters
    # into lower cases
    name = name.lower()

    if name == "cylinder":
        height = float(input("Enter cylinder's height: "))
        rad = float(input("Enter cylinder's radius: "))
        cyl_vol = math.pi * (rad**2) * height
	return prt("cylinder",cyl_vol)

    elif name == "sphere":
        rad = float(input("Enter sphere's radius: "))
        sphere_vol = 4/3 * math.pi * (rad**3)
	return prt("sphere",sphere_vol)

    elif name == "cone":
        height = float(input("Enter cone's height: "))
        rad = float(input("Enter sphere's radius: "))
        cone_vol = 1/3 * math.pi *(rad**2)* height
	return prt("cone",cone_vol)
    
    else:
        print("Sorry! This solid is not available")

if __name__ == "__main__":
    print("Calculate Volume of Solids")
    solid_name = input("Enter the type of solid: ")
    print(calculate_volume(solid_name))
