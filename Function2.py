import math
def Volume_of_Cylinder(r,h):
    v= (math.pi*r*r*h)/3
    return v
    #print(v)
print('Volume of a Cylinder is :',Volume_of_Cylinder(14,9))

def Volume_of_rectangle(l,b,h):
    v1=l*b*h
    return v1
print('Volume of a Recatangle is :',Volume_of_rectangle(2,6,8))

def root_of_the_eqn(a,b,c):
    x1= (-b + math.sqrt( (b*b -(4*a*c) ) )) / (2*a)
    x2= (-b - math.sqrt((b*b-(4*a*c)))) /(2*a)
    print('Roots of the Eqn are:' ,x1,x2)
(root_of_the_eqn(1,-1,-6))