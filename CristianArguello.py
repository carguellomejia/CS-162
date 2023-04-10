def rect_area(l, w):
    area = l * w
    return area
#Surface area was done by Cristian and Johanna
def rect_solid_area(l, w, h):
    surface_area = 2 * (rect_area(l, w) + rect_area(w, h) + rect_area(l, h))
    return surface_area
#implemented surface area equation to return values
l = float(input("Enter the length of the object as in integer: "))
w = float(input("Enter the width of the object as in integer: "))
h = float(input("Enter the height of the object as in integer: "))
#asking for input of integers to calculate surface area
surface_area = rect_solid_area(l, w, h)
print("Length = ", l, "Width = ", w, "Height = ", h)
print("Surface Area =", surface_area)
#program will now calculate three parameters and go off by user input
