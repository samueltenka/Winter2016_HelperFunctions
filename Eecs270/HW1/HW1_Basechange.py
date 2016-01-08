def gcd(a,b):
   while a and b:
     if a<=b: b%=a
     elif b<=a: a%=b
   return a+b #one of em is 0

def summarize_periodic(denom, string, base):
    #take log to find #digits needed to repeat before certain of repetition:
    state_size = 0; base = Rational(base, 1)
    power = Rational(1,1)
    while power < Rational(denom,1):
        power = power*base
        state_size += 1
    #print("###",state_size)

    ngrams = []; repeat_start, repeat_end= None, None
    for i in range(0,len(string)-state_size):
        ng = string[i:i+state_size]
        if ng in ngrams:
            repeat_start=ngrams.index(ng)
            repeat_end = i
            break
        ngrams.append(ng)
    if repeat_start is not None:
       return '%s\\overline{%s}' % \
          (string[:repeat_start],string[repeat_start:repeat_end])
    return string

class Rational:
   def __init__(self, p,q): self.p,self.q = p,q
   def copy(self, other): self.p,self.q=other.p,other.q
   def __float__(self): return float(self.p)/self.q
   def __eq__(self, other): return self.p*other.q == self.q*other.p
   def __gt__(self, other): return self.p*other.q > self.q*other.p
   def __ge__(self, other): return self.p*other.q >= self.q*other.p
   def __lt__(self, other): return self.p*other.q < self.q*other.p
   def __le__(self, other): return self.p*other.q <= self.q*other.p
   def __add__(self, other):
       return Rational(self.p*other.q + other.p*self.q, self.q*other.q)
   def __sub__(self, other):
       return Rational(self.p*other.q - other.p*self.q, self.q*other.q)
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

   def to_base(self, base, maxlen=128):
      self.simplify()
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
      if '.' in string:
         s1,s2 = string.split('.')
         string = s1 + '.' + summarize_periodic(self.q, s2, base.p//base.q)
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
