# # def first_function():
# #     print('Welcome to python function')

#first_function()

# def print_name_10_times(student_name,n):
#     for i in range(11):
#         print('hi' + i + student_name)
    # print('Hi user')
    # print('Hi user')
    # print('Hi user')
    # print('Hi user')
    # print('Hi user')
    # print('Hi user')
    # print('Hi user')
    # print('Hi user')
    # print('Hi user')
    # print('Hi user')

#print_name_10_times(student_name,n)

def convert_input_int():
    user_input= input('Please enter a number')
    user_input= int(user_input)
    return user_input

def convert_input_float():
    user_input1= input('Please enter a number')
    user_input1= float(user_input1)
    return user_input1

# num = convert_input_int()
# num1= convert_input_float()
# print('num',type(num))
# print('num1',type(num1))
# sum= num+ num1
# print( 'Total',type (sum))

def add_two_numbers(num, num1 ):
    sum= num + num1
    print('total is' , sum)
def divide_two_numbers(num, num1 ):
    divide= num / num1
    print('division is' , divide)
def substract_two_numbers(num, num1 ):
    substract= num - num1
    print('substract is' , substract)
def multiply_two_numbers(num, num1 ):
    multiply= num * num1
    print('multiply is' , multiply)

num = convert_input_float()
operator= input('pleasse Enter Operator')
operators=['+','-','*','/']
while operator  not in operators:
    operator= input('pleasse Enter valid Operator')
num1= convert_input_float()

if operator== "+":
    add_two_numbers(num,num1)
elif operator== "-":
   substract_two_numbers(num,num1)
elif operator== "/":
    divide_two_numbers(num,num1)
elif operator== "*":
    multiply_two_numbers(num,num1)
else:
    print('Invalid')




