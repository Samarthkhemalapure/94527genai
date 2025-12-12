import math_utils

# Circle
r = float(input("Enter radius of circle: ")) 
print("\nArea of circle =", math_utils.area_circle(r))

# Rectangle
l = float(input("\nEnter rectangle length: "))
w = float(input("Enter rectangle width: "))
print("\nArea of rectangle =", math_utils.area_rectangle(l, w))

# Triangle
b = float(input("\nEnter base of triangle: "))
h = float(input("Enter height of triangle: "))
print("\nArea of triangle =", math_utils.area_triangle(b, h))

#square
h = float(input("\nEnter side of square : "))
print("area of square =",math_utils.area_of_square(h))