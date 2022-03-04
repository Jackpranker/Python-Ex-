print('=========================================================')
print('LIST OPERATION : MAIN MENU')
print('=========================================================')

from os import sep
import sys
Information=sys.stdout
Data=['Java','C++','SQL','HTML']
Data_sort=sorted(Data, reverse=False)

def Adding_element():
    Information=open('Data.txt','a')
    add_data= input('Add a new data to the information:  ')
    Data.append(add_data)
    print(f'A {add_data} has been added ')
    
def Read_Element():
    Information=open('Data.txt','r')
    print(Information.readlines() )
    print('Read element(s) comfirm')
    
def Delete_element():
    Information=open('Data.txt','r+')
    print(Data)
    Revome_data= str (input('Revome an information:  '))
    Data.remove(Revome_data)
    print(f'{Revome_data} has been remove')

def Sorts_Elements():
    Information=open('Data.txt','r+')
    Data_sort=sorted(Data, reverse=False)
    print(Data_sort)
    print('Data sorted ')
    
def Standard():
    sys.stdout.write(str(Data)+ '\n')
    print('Standard output printed for Added Data')
    sys.stdout.write(str(Data)+ '\n')
    print('Standard output printed for Read data')
    sys.stdout.write(str(Data)+ '\n')
    print('Standard output printed for Delete ata')
    sys.stdout.write(str(Data_sort) + '\n')
    print('Standard output printed for sorted')

def Write_to():
    Information.write(str(Data)+ '\n')
    print(' Added Data written to a file completed')
    print('Delete Data written to a file completed')
    Information.write(str(Data_sort)+'\n')
    print('Data written to a file completed')

def exit_command():
    print('Program terminated')
    sys.exit()
    print('Test d exit command')

num=['1','2','3','4','5','6','7']

print(
    '1. Add new data element to the list \n' 
    '2. Read data elements from a text file \n'
    '3. Delete a dat from te list \n'
    '4. sort data elements in the list \n'
    '5. Display all data elements on standard output \n'
    '6. Write data elements to a text file \n'
    '7. Exit ')
Main_menu= str(input( 'Press: '))    
if Main_menu=='1':  
    Adding_element()
elif Main_menu=='2':
    Read_Element()
elif Main_menu=='3':
    Delete_element()
elif Main_menu=='4':
    Sorts_Elements()
elif Main_menu=='5':
    Standard()
elif Main_menu=='6':
    Write_to()
elif Main_menu=='7':
    exit_command()
elif Main_menu=='quit':
        exit_command()
else:
    if Main_menu not in num:
        print('Enter Valid input')
        Main_menu= str(input( 'Press: '))

end= 'quit'
while Main_menu != 'quit':
    print(
    '1. Add new data element to the list \n' 
    '2. Read data elements from a text file \n'
    '3. Delete a dat from te list \n'
    '4. sort data elements in the list \n'
    '5. Display all data elements on standard output \n'
    '6. Write data elements to a text file \n'
    '7. Exit  ')
    Main_menu= str(input( 'Press: '))
    if Main_menu=='1':  
        Adding_element()
    elif Main_menu=='2':
        Read_Element()
    elif Main_menu=='3':
        Delete_element()
    elif Main_menu=='4':
        Sorts_Elements()
    elif Main_menu=='5':
        Standard()
    elif Main_menu=='6':
        Write_to()
    elif Main_menu=='7':
        exit_command()
    elif Main_menu=='quit':
        exit_command()
    else:
        if Main_menu not in num:
            print('Enter Valid input')
            Main_menu= str(input( 'Press: '))
        








