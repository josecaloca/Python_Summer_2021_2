'''
INSTRUCTIONS: Please use the Shape structures (https://github.com/prubach/Python_OO/blob/master/Shapes.py) and extend it by:
1. adding a Triangle and EquilateralTriangle - they may inherit from each other
2. adding perimeter calculation to every structure
3. adding a Square that inherits from Rectangle and uses its calc_surface implementation
4. providing some code that tests the new functionality and structures
'''

class Shape:
    def __init__(self, a=10, b=6):
        self.set_params(a, b)

    def set_params(self, a, par_b):
        self._a = a
        self.b = par_b

    def get_a(self):
        return self._a

    def __repr__(self):
        return self.__class__.__name__ + "[" + str(self._a) + " by " + str(self.b) + "] at " + str(hex(id(self)))

class Rectangle(Shape):
    def calc_surface(self):
        return self._a * self.b

    def calc_perimeter(self):
        return self._a * 2 + self.b * 2

    def swap_sides(self):
        a = self._a
        b = self.b
        self._a = b
        self.b = a

import math

class Circle(Shape):
    def __init__(self, a):
        super().__init__(a, 0)

    def calc_surface(self):
        return math.pi * self._a ** 2

    def calc_perimeter(self):
        return self._a * 2 * math.pi

    def __repr__(self):
        return self.__class__.__name__ + "[r=" + str(self._a) + "] at " + str(hex(id(self)))

class Triangle():
    def __init__(self, a=1, b=2, c=3):
        if a>b+c: pass
        elif b>a+c: pass
        elif c>a+b: pass
        else:
            self.a = a
            self.b = b
            self.c = c

    def calc_perimeter(self):
        return self.a + self.b + self.c

    def __repr__(self):
        return self.__class__.__name__ + "[" + str(self.a) + ", " + str(self.b) + ", " + \
               str(self.c)+ "] at " +str(hex(id(self)))

class EquilateralTriangle(Triangle):
    def __init__(self, a):
        super().__init__(a, a, a)

class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)

    def __repr__(self):
        return self.__class__.__name__ + "[" + str(self._a) + "] at " + str(hex(id(self)))

r = Rectangle(5, 6)
print(r)
print('Surface: ' + str(r.calc_surface()))
print('Perimeter: ' + str(r.calc_perimeter()) + '\n')

c = Circle(7)
print(c)
print('Surface: ' + str(c.calc_surface()))
print('Perimeter: ' + str(c.calc_perimeter()) + '\n')

t=Triangle(10,7,5)
print(t)
print('Perimeter: ' + str(t.calc_perimeter()) + '\n')

t2=EquilateralTriangle(5)
print(t2)
print('Perimeter: ' + str(t2.calc_perimeter()) + '\n')

s = Square(11)
print(s)
print('Surface: ' + str(s.calc_surface()))
print('Perimeter: ' + str(s.calc_perimeter()))