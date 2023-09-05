from math import pi

def circumference(r):
  return 2*pi*r

def area(r):
  return pi*(r**2)

radius = int(input("Radius: "))
print(f"Circumference:{round(circumference(radius), 2)}")
print(f"Area:{round(area(radius), 2)}")
