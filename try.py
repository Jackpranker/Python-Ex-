print("Welcome to my listing App")
team=[]
start= input("Start listing unless u type  quick to end ")
quick= 'end'
while start != "end":
    team.append(start)
    start= input("Start listing unless u type  quick to end")
    print(team)
else:
    print(team)