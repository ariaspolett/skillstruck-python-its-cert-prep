import math
a = int(input("What is the length of side a?"))
b = int(input("What is the length of side b?"))
asquared = pow(a,2)
bsquared = pow(b,2)
csqaured = asquared + bsquared
c = math.sqrt(csqaured)
final = round(c,2)
print(final)