import math

def gradeSchool( x, y ):
  if x.bit_length() == y.bit_length == 1:
    return x*y
  n = x.bit_length()
  m = math.floor(n/2)
  x = bin(x)[2:] # Remove first two chars
  y = bin(y)[2:]
  xL = x[0:m]
  xR = x[m+1:len(x)]
  yL = y[0:m]
  yR = y[m+1:len(y)]
  print( int(x) )
  print( int(y) )
  print( n )
  print( m )
  print( xL )
  # p1 = gradeSchool( int(xL, 2), int(yL, 2) )
  # p2 = gradeSchool( xL, yR )
  # p3 = gradeSchool( xR, yL )
  # p4 = gradeSchool( xR, yR )
  # print (p1 * 2**n + (p2 + p3) * 2**(n/2) + p4) + '\n'
  # return p1 * 2**n + (p2 + p3) * 2**(n/2) + p4
