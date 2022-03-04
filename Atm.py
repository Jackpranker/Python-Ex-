print('Welcome to Pranker ATM Banking System')
Start= int(input('Press 1_Login and 2_Creates a New Account \n'))
my_atm=open('atm.txt','a+')
Accont_dict={}

if Start==1:
    print('welcome to the log in section')
    username= input('Enter your username ')
    if username  in my_atm==open('atm.txt','r+'):
        print('Welcome user')
    print('&&&&&&')
    
if Start==2:
    print('Hi user Sing-up for New Accont ') 
    username= input('Enter your Username Details \n')
    pincode= int(input('Creates a  Pincode \n'))
    re_pincode= int(input('Re-enter  Pincode \n '))
    if int(re_pincode != int(pincode)):
        print('Invalid  Pincode')
    i=0
    while int(re_pincode != int(pincode)):
        re_pincode= int(input(' Pincode  do not match \n Rewrite Pincode \n') )
    else:
     None
    initial_deposit= int(input('Enter the intial deposit not more than D500.00 \n'))
    if initial_deposit>500:
        print('Invalid Deposit')
    i=0
    while initial_deposit > int(500):
        initial_deposit= int(input(' Plz Enter the intial deposit not more than D500.00 \n'))
    else:
     None
    Dalasi= "D" + str(initial_deposit)
    Accont_dict={'Username':username,'Pincode':pincode,'initial deposit': Dalasi}
    print('Account created ',Accont_dict)
    print('We thank you for your service ')
    my_atm.write( '\n' +str(Accont_dict))
