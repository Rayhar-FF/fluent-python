import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector{self.x!r}, {self.y!r}"

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self,scalar):
        return Vector(self.x * scalar, self.y * scalar)


    # Apart from the __init__(self, x, y) method which is implemented regularly in classes.
    # We've implemented five special methods. These methods will be called directly by the python interpreter.
    #
    #Python supports the use of any object as a boolean. So the object x if checked as a boolean would call.
    # x.__bool__() and would use that result. Falls back to __len__ if __bool__ is not implemented.

    # Python has ABCs abstract base classes and does not require concrete classes to inherit from these ABCs.
    # The python language reference lists over 80 special methods that implement arithmetic, bitwise and comparison operators.