print('welcome to  Python class registration program')
student_list=[]
i=1
nuber_of_student= int(input('How many student did u wana register?'))
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
    #print(student_list)
    matchfound= 'no'
    while matchfound != 'yes':
        search= input('Enter the name to search')
        for student in student_list:
            if student['First_Name']== search:
                print('Match found')
                print(student)
                matchfound= 'yes'
                break