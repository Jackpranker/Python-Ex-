# # # # # # # # # import math
# # # # # # # # # print(math.sqrt(25))
# # # # # # # # # x=["jack"]
# # # # # # # # # y=["ousman"]
# # # # # # # # # x.append(y)
# # # # # # # # # print(x)

# # # # # # # # nu=2
# # # # # # # # nii=3
# # # # # # # # n= sum ([nu,nii])
# # # # # # # # print(2 *'6' )

# # # # # # # # a= 2/3
# # # # # # # # print(a)

# # # # # # # # def print_name_10_times():
# # # # # # # #     print('Ousman \n '* 12  )

# # # # # # # # print_name_10_times()

# # # # # # # def print_name_10_times():

# # # # # # #     sname = input('please enter a name : ')
# # # # # # #     print_name_10_times()

# # # # # # # # sname = input('please enter a name : ')

# # # # # # # print_name_10_times()

# # # # # # # def print_name_n_times(students_name,word):
# # # # # # #     for i in range(n):
# # # # # # #         print("hello  "+str(i)+ students_name)     
# # # # # # # print_name_n_times("j",6)

# # # # # # def enter(name, address,age,birth):
# # # # # #     print("welocme user" + name,address,age,birth)

# # # # # # enter('OUSMAN','eno town',12,'banjul')

# # # # # def print_name_n_times(students_name,n):
# # # # #     for i in range(n):
# # # # #         #inpu= input('Name') 
# # # # #         print("hello  "+str(n)+ students_name)    
      
# # # # # #     # print("hello "+ students_name)
# # # # # #     # print("hello " +students_name)
# # # # # #     # print("hello " +students_name)
# # # # # #     # print("hello " +students_name)
# # # # # #     # print("hello " +students_name)
# # # # # #     # print("hello " +students_name)
# # # # # #     # print("hello " +students_name)
# # # # # #     # print("hello " +students_name)
# # # # # #     # print("hello " +students_name)
# # # # # #     # print("hello " +students_name)
# # # # # # #     print("print is done")
# # # # # print_name_n_times("jack",9)

# # # # # d={'Gambia': 'Banjul','Senegal':'Dakar'}
# # # # # search= input('enter ')
# # # # # search1= search.capitalize()
# # # # # if search1=='Gambia':
# # # # #     print(d['Gambia'])
# # # # # elif search1=='Senegal':
# # # # #     print(d['Senegal'])

# # # # Information=open('Data.txt', 'r')
# # # # r= input('Enter')
# # # # if r in Information.readlines():
# # # #    Information.remove(r)
# # # #    print(Information.readlines)
# # # import sys
# # # test= sys.stdout
# # # l=['k','i','uu']
# # # sys.stdout.write(str(l) +'\n')
# # # test.write(str(l) +'\n')

# # # Mam=open('code','w')
# # # ask=input('Enter')
# # # Mam.write(ask)
# # Mam=open('code','r')
# # print(Mam.readline())
# import os #os.system('copy ' + Application+ ' ' + Back_up+'')
# os.system('copy ' +"C:/Users/JackPranker/Documents/New Folder" + ' '+ "C:/Users/JackPranker/Downloads/new Fontss" +'' )

print('welcome to input ordering /n Here we goes ')
data= input("type anything u to be written")
d=data.capitalize()
list=[]
end="Quit" or "quit"
while d != end:
    list.append(d.capitalize())
    d= input("type anything u to be written")
    print(list)
else:

    print(sorted(list))




