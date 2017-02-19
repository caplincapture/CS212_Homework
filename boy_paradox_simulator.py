

import itertools
from fractions import Fraction #

sex = 'BG'

def product(*variables):
	"the cartesian product (as a str) of the possibilities for each variable"
	return map(''.join, itertools.product(*variables)) # ''.join creates list of the combinations

two_kids = product(sex, sex)

one_boy = [s for s in two_kids if 'B' in s]

def two_boys(s): return s.count('B') == 2

def condP(predicate, event):
	pred = [s for s in event if predicate(s)]
	return Fraction(len(pred), len(event))

print condP(two_boys, one_boy)

day = 'SMTWtFs'

two_kids_days = product(sex, day, sex, day)
print two_kids_days
boy_tuesday = [s for s in two_kids_days if 'BT' in s]

print condP(two_boys, boy_tuesday)

