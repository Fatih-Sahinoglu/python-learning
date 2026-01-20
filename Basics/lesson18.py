#math module

#import math not necessary----------------------------------
min(5,6)
max(2,6)

abs(-13.23)

pow(2,5) #first to the second

#-----------------------------------------------

#necessary-----------------------------------------
import math

math.fabs(-5.6) #float abs
math.factorial(6)

num=[1,2,3,4]
math.fsum(num) #float parameter shoul be like list
math.prod(num) #multiples all element if parameter empty = 1

#output is radian
math.cos(0)
math.sin(90)
math.tan(45)
#arc trigos
math.acos(0.5)
math.asin(0.5)
math.atan(1)

math.degrees(5) #radian to degree
math.radians(60) #degree to radian

math.ceil(3.00014) #round bigger one if it is not integer (4)
math.floor(3.9999) #round smaller one if it is not integer (3)
math.trunc(5.490) #just ignore float part (5)

math.sqrt(16) 
math.isqrt(16) #get sqrt and round like .floor (4)

math.comb(5,2) #Combination (10)
math.perm(3) #Permutation (6)
math.perm(5,2) #(60)


#distance
#It calculates the Euclidean (linear) distance between two points.
p=[1,2]
q=[4,6]
math.dist(p,q) #5

math.gcd(6,8) 
math.lcm(6,8)

math.hypot(3,4) #Can get more parameter than 2

math.log(8,2) #log(2)8 (3) 
math.log(10) #log(e)10 or ln10
math.log10(10) #log(10)10 or log10
math.log2(4) #log(2)2
