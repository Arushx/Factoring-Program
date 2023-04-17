# Factoring Calculator


#Function to find factors of the C term
def factor(x, y: list):
  n = 1
  x = abs(x)
  while n <= x:
    if x % n == 0:
      y.append(n)
    n += 1

#Create a negative version of the list
def convertListPosToNeg(x: list, y: list):
  for n in x:
    y.append((n * -1))

# this is a embded for loop to do a cross search for factors
def findAddtoMultiply(x: list, y: list, z: list, c: int, b: int):
  if c < 0 or b < 0:
    for n in x:
      num1 = n
      for l in y:
        num2 = l
        if num1 * num2 == c and num1 + num2 == b:
          z.append(num1)
          z.append(num2)
          return z
  else:
    for n in x:
      num1 = n
      for l in x:
        num2 = l
        if num1 * num2 == c and num1 + num2 == b:
          z.append(num1)
          z.append(num2)
          return z

#List intilization
listOfFactorPos = []
listOfFactorNeg = []
pairOfCorrectFactor = []

#Introduction Print
print('''

Welcome to the factoring Program

If you have a simple trinomial 
give the C term and the B term coeffcient (including signs)

Other wise with complex trinomial 
give the A term coeffcient * C term and the B term coeffcient

''')

#Input Retrival
c = int(input("What is c or a*c: "))
b = int(input("what is b: "))


#Calling functions
factor(c, listOfFactorPos)
convertListPosToNeg(listOfFactorPos, listOfFactorNeg)
pairOfCorrectFactor = findAddtoMultiply(listOfFactorPos, listOfFactorNeg, pairOfCorrectFactor, c, b)

#Prints final pairs
print(pairOfCorrectFactor)
