side1 = 5
side2 = 8
side3 = 4

perimeter = side1 + side2 + side3
s = perimeter/2
area = (s*(s-side1)*(s-side2)*(s-side3))**0.5
print("Perimeter: ",format(perimeter,'.2f'),"Area: ",format(area,'.2f'))
