"""Ousman Jack"""
First_Name_list=[]
Last_Name_list=[]
Full_Name_list=[]
Email_list=[]
Details_dict={}
Details_list=[]
First_Name= input("Please Enter your first Name \n")
Last_Name= input("Please Enter your last Name \n ")
Full_Name= First_Name + "" + Last_Name
Email= Full_Name + "@xyz.com"
print(First_Name.lower(), Last_Name.lower(), Full_Name.upper(), Email.lower() )
loop= input("Select Yes or NO for the continue of the program \n")

if loop=='yes':
    stop ="Quick"
    while loop != "Quick":
        
        First_Name= input("Please Enter your first Name \n ")
        First_Name_list.append(First_Name)
        Last_Name= input("Please Enter your last Name \n ")
        Last_Name_list.append(Last_Name)
        Full_Name_list.append(Full_Name)
        Full_Name= First_Name + Last_Name
        Email= Full_Name +  "@xyz.com" 
        Email_list.append(Email)
        Details= First_Name.lower()+ " "+ Last_Name.lower()+" "+ Full_Name.upper()+" "+ Email.lower()
        #print(Details)
        Details_dict={'First Name':First_Name.lower(),'Last Name':Last_Name.lower(),
        'Full Name':Full_Name.upper(),'Email':Email.lower()}
        Details_list.append(Details_dict)
        #print(First_Name.lower(), Last_Name.lower(), Full_Name.upper(), Email.lower() )
        print(Details_dict)
        loop= input("Select Yes for the continue of the program or or Quick \n")
        
    else:
        #print(First_Name_list,Last_Name_list,Full_Name_list,Email_list)
        print(Details_list)
        print("Welcome to the search and updates part \n")
        Search=input("Search")
        for name in Details_list:
           if name['First Name']== Search:
            print("search found " ,name)
        else:
            print("Thank you for using my Program")
            # print("Welcome to updates part \n")
            # updates= input('Enter the updates name')
            # Details_dict['First Name']= updates
            # print('Updates completed ',Student_dict)