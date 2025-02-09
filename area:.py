def area_of_circle(r):
    import math
    return math.pi * r ** 2
r=int(input("Enter radius:"))
print("Area of Circle with radius",r,":", area_of_circle(r))