"""Ousman Jack NHD2"""
print(" Hello user Welcome to Quadratic Eqn Solver using the formular method")
print(" The  Eqn Writes ax^2+bx+c=0 ")
print (" My program will ask to enter one value at a time ")

a=input("Enter the a value ")
b=input("Enter the b value ")
c=input("Enter the c value ")
print(" The values u entered are "+ a,b,c)
print(" which maps to "+ a +"x^2 +" +b +"x +" +c +"=0")

power= pow( int(b), 2)- 4*int(a)*int(c)
under= (2* int(a))


if int(power)>0:
	import math
	square_root= math.isqrt(power)
	root1= (-int(b) - square_root)/ (under)
	root2= (-int(b) + square_root)/ (under) 
	print("The roots of the Eqn are ")
	print(root1,root2   )
else:
	import math
	square_root= math.isqrt(-power)	
	root1= (-int(b) - square_root)/( under)
	root2= (-int(b) + square_root)/ (under)
	print("The roots of the Eqn are ")
	print(root1,root2 )
 
