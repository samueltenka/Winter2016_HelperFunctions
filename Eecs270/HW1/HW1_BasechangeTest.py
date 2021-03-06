from HW1_Basechange import gcd, summarize_periodic, Rational
print('checking gcd...',end='')
assert(gcd(45,45)==45)
assert(gcd(9,45)==9)
assert(gcd(9,6)==3)
assert(gcd(3,1234)==1)
assert(gcd(1,0)==1)
assert(gcd(0,0)==0)
print('gcd passed!')

print('checking summarize_periodic...',end='')
assert(summarize_periodic(100, '1212121212', 10)=='\\overline{12}')
assert(summarize_periodic(99, '1212121212', 10)=='\\overline{12}')
assert(summarize_periodic(101, '1212121212', 10)=='\\overline{12}')
assert(summarize_periodic(100, '45612312312', 10)=='456\\overline{123}')
print('summarize_periodic passed!')

print('checking to_base...',end='')
assert(Rational(8,1).to_base(2)=='1000')
assert(Rational(1,3).to_base(2)=='0.\\overline{01}')
assert(Rational(25,1).to_base(2)=='11001')
assert(Rational(25,1).to_base(8)=='31')
assert(Rational(25,1).to_base(16)=='19')
assert(Rational(7,15).to_base(2)=='0.\\overline{0111}')
assert(Rational(21,22).to_base(2)=='0.1\\overline{1110100010}')
print('to_base passed!')

print('checking from_base...',end='')
s = Rational(0,1)
assert(s.from_base('1000',2)==Rational(8,1))
assert(s.from_base('0.23',5)==Rational(13,25))
assert(s.from_base('ff',16)==Rational(255,1))
print('from_base passed!')
