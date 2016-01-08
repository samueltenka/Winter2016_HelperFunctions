from HW1_Basechange import Rational

print('Eecs 270')
print('.HW 1')

def solve(strings, start_base, end_bases):
   r = Rational(0,1)
   for s in strings:
      r.from_base(s,start_base)
      print(' = '.join('%s_{%d}' % (r.to_base(b),b) for b in end_bases))


print('..Problem 1')
solve(['57','69421','97.33','4027.6'], 10, [10, 2, 8, 16])
print('..Problem 2')
solve(['100110111','1101.1011','110110.11'], 2, [2, 10, 8, 16])
print('..Problem 3')
solve(['9a4','caf.e','fa.ce'], 16, [16, 10, 2, 8])
