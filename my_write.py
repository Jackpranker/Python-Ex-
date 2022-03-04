print('welcome to  Python class registration program')
student_list=[]
write_to= open('Write1','a+')


i=1
nuber_of_student= int(input('How many student did u wana register?'))
for j in range(nuber_of_student):
    while i <=nuber_of_student:
      
        First_Name= input('plz enter first name')
        Last_Name=  input('plz enter last name')
        Address=    input('plz enter Address')
        Date_of_Birth= input('plz enter  Date of Birth name')
        Gender=    input('plz enter Gender')
        student_record= {'First_Name':First_Name,'Last_Name': Last_Name,'Address': Address,' Date_of_Birth': Date_of_Birth,'Gender':Gender}
        student_list.append(student_record)
        print('Student registered successfully')
        print(student_record)
        i= i+1
    else:
        print(student_list)
        write_to.write(" \n STUDENT" + str(j+1))
        write_to.write('\n'+str(student_list )) 
        print(write_to.readlines( ))