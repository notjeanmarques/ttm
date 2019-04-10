import sys


class Vector2():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vector2):
            raise TypeError(f"[!] bad type : { other.__name__ } must be type 'Vector2'")
        return Vector2(self.x + other.x, self.y + other.y)
    
    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if not isinstance(other, Vector2):
            raise TypeError(f"[!] bad type : { other.__name__ } must be type 'Vector2'")
        return Vector2(self.x - other.x, self.y - other.y)
    
    def __rsub__(self, other):
        return self.__sub__(other)

    def __mul__(self, number):
        if type(number) == int or type(number) == float:
            return Vector2(number * self.x, number * self.y)
        else:
            raise TypeError(f"[!] bad type : { other.__name__ } must be type 'int' or 'float'")
    
    def __rmul__(self, number):
        return self.__mul__(number)
    
    def __truediv__(self, number):
        if number == 0:
            raise ZeroDivisionError("[!] zero division error")
        return self.__mul__(1 / number)
    
    def __rtruediv__(self, number):
        return self.__truediv__(number)

    ###########################################################
    #linear algebra methods 

    def scalar_prod(self, other):
        if not isinstance(other, Vector2):
            raise TypeError(f"[!] bad type : { other.__name__ } must be type 'Vector2'")
        return self.x * other.x + self.y * other.y
    
    def modulus(self):
        return (self.x ** 2 + self.y ** 2) ** (1 / 2)
    
    def unitary(self):
        return self / self.modulus()
    
    def project(self, other):
        if not isinstance(other, Vector2):
            raise TypeError(f"[!] bad type : { other.__name__ } must be type 'Vector2'")

        return self.scalar_prod(other) * other / (other.modulus()) ** 2

    ################################################################
    #text methods 

    def __str__(self):
        return f"<x : { self.x }  y : { self.y }>"









    