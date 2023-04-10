# will take 2 parameters - length and width.
def rect_area(length, width):
    area = length * width
    return area
# Write a second function named "rect_surface_area" that calls the first function -
# "rect_area" - three times to compute the surface area of a rectangular solid.  This
# function will take three parameters - length, width and height.
def rect_surface_area(length, width, height):
    sa = 2 * (rect_area(length, width) + rect_area(width, height) + rect_area(length, height))
    print('Length =', length, 'Width =', width, 'Height = ', height)
    return sa
length1 = float(input('Enter length here: '))
width1 = float(input('Enter width here: '))
height1 = float(input('Enter height here: '))
surface_area = rect_surface_area(length1, width1, height1)
print('Total surface area =', surface_area)

# The main program will call the "rect_surface_area" with three parameters length, width
# and height.

# The user input to the program will be three integers - length, width and height of a
# rectangular solid.

# The program will print the length, width and height as input and the surface area of
# the entire rectangular solid.
