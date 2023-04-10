#Surface area was done by Cristian
def rect_solid_area(l, w, h):
    surface_area = 2 * l * h + 2 * w * h + 2 * w * l
    return surface_area
#implemented surface area equation to return values
l = float(input("Enter the length of the object as in integer: "))
w = float(input("Enter the width of the object as in integer: "))
h = float(input("Enter the height of the object as in integer: "))

surface_area = rect_solid_area(l, w, h)

print("Length = ", l, "Width = ", w, "Height = ", h)
print("Surface Area =", surface_area)
