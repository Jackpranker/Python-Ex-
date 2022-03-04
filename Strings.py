print("welcome to strings")
f_name="ouSman"
l_name="Jack"

first_letter= f_name[0]
first_three_letter= f_name[0:3]
last_letter=f_name[5] # f_name[-1]

print(f_name,l_name, first_letter, first_three_letter, last_letter) 

#strings method
f_name= f_name.upper()
print(f_name, "Upper case")

f_name= f_name.capitalize()
print(f_name, "Capitalize")
f_name= f_name.lower()
print(f_name, 'lowe case')
#f_name.startswith("Alh")
print(f_name * 10, sep='')
#f_name= f_name+ "\n"
#print(f_name*10)
#Email assigning
#mine
Emai=f_name.lower() + l_name.lower()
print(f_name+"."+l_name + "@gmail.com")
#Teacher-work
email= f_name.lower() +"." + l_name.lower() + "@africell.gm"
print(email) 