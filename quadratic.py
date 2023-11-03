#Ronin Deschamps
#I pledge my honor that I have abided by the Stevens Honor System.

class QuadraticEquation:
    def __init__(self, a, b, c):
        if a == 0:
            raise ValueError("Coefficient 'a' cannot be 0 in a quadratic equation.")
        self.a = a
        self.b = b
        self.c = c

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        self._a = float(value)

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        self._b = float(value)

    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, value):
        self._c = float(value)

    def discriminant(self):
        return self.b**2 - 4*self.a*self.c
    
    def root1(self):
        disc = self.discriminant()
        if disc < 0:
            return None
        else:
            return (-self.b + disc**0.5)/(2*self.a)
        
    def root2(self):
        disc = self.discriminant()
        if disc < 0:
            return None
        else:
            return (-self.b - disc**0.5)/(2*self.a)
        
    def __str__(self):
        a = self.a
        b = self.b
        c = self.c
        eq_str = ""
        if a == -1:
            eq_str += "-x^2"
        elif a == 1:
            eq_str += "x^2"
        else:
            eq_str += f"{a}x^2"
        
        if b != 0:
            if b == 1:
                eq_str += " + x"
            elif b == -1:
                eq_str += " - x"
            elif b < 0:
                eq_str += f" - {abs(b)}x"
            else:
                eq_str += f" + {b}x"
        
        if c != 0:
            if c < 0:
                eq_str += f" - {abs(c)}"
            else:
                eq_str += f" + {c}"
        eq_str += " = 0"
        return eq_str

        
        
    
