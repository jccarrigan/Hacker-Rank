class Complex(object):
    def __init__(self, real, imaginary):
        self.r = real
        self.i = imaginary
    def __add__(self, no):
        return Complex(self.r + no.r, self.i + no.i)
    def __sub__(self, no):
        return Complex(self.r - no.r, self.i - no.i)
    def __mul__(self, no):
        return Complex(self.r * no.r - self.i * no.i, self.r * no.i + self.i * no.r)
    def __div__(self, no): 
        return Complex(((self.r * no.r) + (self.i * no.i))/((no.r**2) + (no.i**2)),((self.i * no.r) - (self.r * no.i))/((no.r**2) + (no.i**2)))
    def mod(self):
        return Complex(math.sqrt(self.r**2 + self.i**2), 0)
    def __str__(self):
        if self.i == 0:
            result = "%.2f+0.00i" % (self.r)
        elif self.r == 0:
            if self.i >= 0:
                result = "0.00+%.2fi" % (self.i)
            else:
                result = "0.00-%.2fi" % (abs(self.i))
        elif self.i > 0:
            result = "%.2f+%.2fi" % (self.r, self.i)
        else:
            result = "%.2f-%.2fi" % (self.r, abs(self.i))
        return result


########### HACKERRANK CODE LOCKED BELOW ##############

if __name__ == '__main__':
    c = map(float, raw_input().split())
    d = map(float, raw_input().split())
    x = Complex(*c)
    y = Complex(*d)
    print '\n'.join(map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]))
