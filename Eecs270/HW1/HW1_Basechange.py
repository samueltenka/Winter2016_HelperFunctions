def gcd(a,b):
   while a and b:
     if a<=b: b%=a
     elif b<=a: a%=b
   return a+b #one of em is 0

class Rational:
   def __init__(self, p,q): self.p,self.q = p,q
   def copy(self, other): self.p,self.q=other.p,other.q
   def __float__(self): return float(self.p)/self.q
   def __eq__(self, other): return self.p*other.q == self.q*other.p
   def __gt__(self, other): return self.p*other.q > self.q*other.p
   def __ge__(self, other): return self.p*other.q >= self.q*other.p
   def __lt__(self, other): return self.p*other.q < self.q*other.p
   def __le__(self, other): return self.p*other.q <= self.q*other.p
   def __add__(self, other): return Rational(self.p*other.q + other.p*self.q, self.q*other.q)
   def __sub__(self, other): return Rational(self.p*other.q - other.p*self.q, self.q*other.q)
   def __mul__(self, other): return Rational(self.p*other.p, self.q*other.q)
   def __truediv__(self, other): return Rational(self.p*other.q, self.q*other.p)
   def simplify(self):
       g = gcd(self.p,self.q)
       self.p //= g; self.q //= g
   def __str__(self):
       self.simplify()
       return "%d/%d" % (self.p,self.q)
   def floor(self):
       return self.p // self.q
   def subfloor(self):
       return (self.p-1) // self.q

   def to_base(self, base, maxlen=32):
      if self < Rational(0,1):
          return '-'+to_base(Rational(0,1)-self, base, maxlen)
      digits = '0123456789abcdefghijklmnopqrstuvwxyz'[:base]

      base = Rational(base,1)
      power = base
      while power <= self:
          power = power*base
      power = power/base; power.simplify()
      remainder = Rational(self.p, self.q)

      string = ''; dot=False
      for i in range(maxlen):
          if dot:
              string += '.'
              dot = False
          dig = (remainder/power).floor()
          remainder = remainder - Rational(dig,1)*power; remainder.simplify()
          string += digits[dig]
          if power==Rational(1,1):
              dot=True
          power = power/base
          if power<Rational(1,1) and remainder==Rational(0,1):
              break
      return string
   def from_base(self,string, base):
       if string[0]=='-':
           self.from_base(string[1:],base)
           self.p = -self.p
           return self

       digits = '0123456789abcdefghijklmnopqrstuvwxyz'[:base]
       self.p,self.q = 0,1
       base = Rational(base,1)
       power = Rational(1,1)

       dot = False
       for d in string:
           if d=='.':
               dot=True
               continue
           dig = digits.find(d); assert(dig != -1)
           self.copy(self*base + Rational(dig,1))
           if dot:
               power = power*base
       self.copy(self/power)
       self.simplify()
       return self
