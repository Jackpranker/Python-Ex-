"""print("welcome to python listing")
list1=['ousman', 'omar', 'jack', 'Pranker']
print(list1)
print(list1[1:3])"""

l_student=["Lamin",'kalifa','jalamba','baba','Ousman','Mam baye']
first_student= l_student[0]
last_student= l_student[-1]
first_three_student=last_student[0:3]
l_student[0]='Omar'
l_student.append("Haruna")
n_student= len(l_student)
#l_student.reverse()
print(l_student,'all students')
print(first_student, 'first student')
print(last_student, 'last student')
print(first_three_student, 'first_three_student')
print(n_student, "number of student")

i=0
while i< n_student:
    print(l_student[i])
    i= i+1