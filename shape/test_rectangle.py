'''
Rectangle heeft:
    - init(self, width, height)
    - area(self)
    
Stap 1: teken het UML ClassDiagram

Stap 2: Defineeer class Rectangle in rectangle.py

Stap 3: Maak een Rectangle object aan in testRectangle.py

Stap 4: Pas class Rectangle aan totdat testRectangle werkt  

Stap 5: Maak methode area() aan

Stap 6: Roep vanuit testRectangle.py methode area() van je object aan  

'''

#!/user/bin/env python

from rectangle import Rectangle

rectangle = Rectangle(4, 5)
print(f'The area of the rectangle is: {rectangle.area()}')