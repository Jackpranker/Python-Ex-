My_file=open('Ip_list.txt','w')  
My_file.write("I am working with files \n")
My_file.write("musa in now a Programmer ")


for i in range (0,255):
    for j in range (0,255):
	    ip_address= " 196.46." + str(i) +'.'+ str(j) +" \n"
	    print(ip_address)
    My_file.write(ip_address)  

       