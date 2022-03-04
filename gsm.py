numbers=[]
import random
file=open('Gsm.txt','a+')
Possible_winners=['3032021','2049320','3029101']
user= (input('Enter number'))
end='quit'
while user != 'quit':
    user= (input('Enter number'))
    numbers.append(user)
    if user=='quit':
        numbers.remove('quit')
    Possible_winners.append(numbers)
    print(numbers,Possible_winners)
else:
    winner= random.choice((Possible_winners))
    print('Winner is: ',winner)
    call='Winner is: '
    file.write(call)
    file.write(str(winner))
    