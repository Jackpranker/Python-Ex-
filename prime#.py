num= int(input(" Please Enter a number"))
isPrime=0
for i in range(num):
	if i<2:
		continue
	else:
		if num % i== 0:
			print(i,num)
			isPrime=1
	if isPrime==0:
		print( f" the number {num} is a prime number")
else:
	print( f" the number {num} is not prime number")

#196.46.232.1 -254

"""for i in range (255):
	if i < 2:
		continue
	else:
		print(" 196.46.232.1." +str(i))"""