import random
token_list=open("token", 'w')
# token= random.randint(10000000000000000000, 20000000000000000000)
# token= str(token)
# new_token= token[0:4] +' '+ token[4:8] +' '+ token[8:12]  +''+ token[12:16]+' '+ token[16:20]
# print(new_token)
i=20
while  i > 0:
    token= random.randint(10000000000000000000, 20000000000000000000)
    token= str(token)
    new_token= token[0:4] +' '+ token[4:8] +' '+ token[8:12]  +''+ token[12:16]+' '+ token[16:20] + "\n"
    print(i)
    print(new_token)
    token_list.write(new_token)
    i=i-1
