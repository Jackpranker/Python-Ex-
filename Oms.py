print("Welcome to family statistics Program")
family= input('Enter your family Name \n')
member= int(input('Enter the family member \n'))
age_list=[]
age_dict={}
Details=[]
name_list=[]
file=open('family','a')
#total = 0
i=0
for i in range(member):
    name= input('Enter the family member name \n')
    name_list.append(name)
    age= int(input('Enter the Age \n'))
    #total = total  + age
    age_list.append(age)
    age_dict= {'Member': (i+1),'Name':name,'Age': age}
    Details.append(age_dict)

else:
   print(' All member Names in the family are',name_list)
   print(' All member age in the family are',age_list)
   print('All ages total in the family is ',sum(age_list)) 
   print('General Details of the family are',Details) 
   file.write('\n' + str(Details)  )

   print("Welcome to the Statistics section")
   Demo= int(input('Press 1 for average\'s age calculation \n'
      'Press 4 for Range calculation \n'
      'Press 5 for maxinum age calculation\n'
      'Press 6 for minimum age calculation\n'))

if Demo==1:
    print('Welcome to average math section')
    average=(sum(age_list)/len(age_list))
    print('Average age is', int(average))
    file.write( '\n' + str(average))
if Demo==4:
    print('Welcome to Range math section')
    Range=max(age_list)-min(age_list)
    print(Range)
    file.write('\n' +str(range))
if Demo==5:
    print('Maximum age of the family is',max(age_list))
    file.write('\n' +str(max(age_list)))
if Demo==6:
    print('Mininum age of the family is',min(age_list))
    file.write('\n' +str(min(age_list)))
else:
    None
    print('Welcome to the Search Interface')
    Search= input('Enter the seach name')
    for son in Details:
        if son['Name']==Search:
            print( "Name found",son)
            file.write("Name found" ,str(son))