#back sub stitution Pseudo Code
Q*y = b
def Backsub(R,b)

  cA = len(b)# find number of rows in matrix
  rA = len(b[0]) # find the number of columns in matrix
  
  Ccontainer = [[0] * rA for row in range(cA)]

  Ccontainer[cA] = b[cA] / R[cA][cA]

  for i in range(cA -1,0,-1)

    c[i] = b[i]

    for j in range(i +1,cA)

      Ccontainer[i] = Ccontainer[i] - Ccontainer[j]R[j][i]

      Ccontainer[i] = Ccontainer[i]/R[i][i]

  return c