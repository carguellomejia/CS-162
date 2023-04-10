def rect_area(length, width):
    area = length * width
    return area

length = float(input('Enter the length of the rectangle: '))
width = float(input('Enter the width of the rectangle: '))

area = rect_area(length, width)

print("Length = ", length, "Width = ", width)
print("Area =", area)