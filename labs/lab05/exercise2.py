import math 
radius = int(input("Enter the radius of the circle: "))
circle_area = int(math.pi * (radius ** 2))
circle_circumference = int(2 * math.pi * radius)

print("Radius:", radius)
print("Area:", circle_area)
print("Circumference:", circle_circumference)