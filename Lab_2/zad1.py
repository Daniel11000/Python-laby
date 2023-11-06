class Complex(object):

    def __init__(self, real, imag=0.0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return (Complex(self.real + other.real, self.imag + other.imag))

    def __sub__(self, other):
        return (Complex(self.real - other.real, self.imag - other.imag))

    def __str__(self):
        return str(self.real + self.imag)

    def print_complex(self):
        return str(self.real + self.imag)
        #   NIE może być - print(self.real + self.imag)  -- bo przy takim wywołaniu jak poniżej metoda była by wywoływana przed "z1 = ", a kończyła by się po


# addition , subtraction


z1 = Complex(2, 10j)
z2 = Complex(3, 5j)

print("z1 = ", z1.print_complex())
print("z2 = ", z2.print_complex())

# Add
# i + k
i = z1 + z2
print("\ni = z1+z2")
print("i = ", i.print_complex())
# Subtract
# i - k
k = z1 - z2
print("\nk = z1 - z2")
print("k = ", k.print_complex())

z3 = Complex(1, 2j)
print("\nz3 = ", z3.print_complex())
l = z3 - z1
print("\tl = z3-z1")
print(l)
print("l = ", l.print_complex())
