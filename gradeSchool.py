import math

def gradeSchool( x, y ):
  if (len(x) == 1) and (len(y) == 1):
    return [x[0]*y[0]]
  elif (len(x) == 1):
    return [x[0]*]
  n = len(x)
  m = math.floor(n/2)
  xL = x[0:m]
  xR = x[m:len(x)]
  yL = y[0:m]
  yR = y[m:len(y)]

  p1 = gradeSchool( xL, yL )
  p2 = gradeSchool( xL, yR )
  p3 = gradeSchool( xR, yL )
  p4 = gradeSchool( xR, yR )

  N = p1 + p2 + p3 + p4
  return N
