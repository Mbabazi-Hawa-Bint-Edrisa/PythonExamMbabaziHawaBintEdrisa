#area of a triangle
base = int(input('Enter the base of the triangle: '))
height = int(input('Enter the height of the triangle: '))

def area_of_triangle(b,h):

    area = (1/2) * b * h

    print(area)

area_of_triangle(base,height)