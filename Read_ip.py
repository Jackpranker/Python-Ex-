My_file=open('token', 'r')
print(My_file.readline())
while My_file.readline():
    print(My_file.readline())
My_file.close()