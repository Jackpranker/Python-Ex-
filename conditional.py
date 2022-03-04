full_name = input( "what is your name? ")
year_born= input(" which year where you born ")
nationality = input("where were you born ")
age =2021- int(year_born)

if int(age) >=18 and nationality == "Gambia" :
	print( "Dear " + full_name + " you can vote" )
elif int(age) >=18 and nationality != "Gambia" :
	print("sorry " + full_name + " you have the eligible age  but " + " You are not a Gambia")	
else:
	print( "Dear " + full_name + " You are under age and cant vote ")