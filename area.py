# define a function for calculating
# the area of a shapes
def calculate_area(name):\
    
  # converting all characters
  # into lower cases
  name = name.lower()
    
  # check for the conditions
  if name == "rectangle":
    height = float(input("Enter rectangle's height: "))
    width = float(input("Enter rectangle's width: "))
      
    # calculate area of rectangle
    rect_area = height * width
    print(f"The area of rectangle is {rect_area}.")
    
  elif name == "square":
    height = float(input("Enter square's height: "))
        
    # calculate area of square
    sq_area = height * height
    print(f"The area of square is {sq_area}.")
  
  elif name == "triangle":
    height = float(input("Enter triangle's height: "))
    width = float(input("Enter triangle's width: "))
        
    # calculate area of triangle
    tri_area = 0.5 * width * height
    print(f"The area of triangle is {tri_area}.")
  
  elif name == "circle":
    rad = float(input("Enter circle's radius: "))
    pi = 3.14
          
    # calculate area of circle
    circ_area = pi * rad * rad
    print(f"The area of circle is {circ_area}.")
      
  else:
    print("Sorry! This shape is not available")
  
# driver code
if __name__ == "__main__" :
    
  print("Calculate Shape Area")
  shape_name = input("Enter the type of shape: ")
    
  # function calling
  calculate_area(shape_name)