list_of_food=["Domada","Mbahal","super","peng peng", "bENACHIN"]
list_of_food = []
food= input("Enter choice of food ")
end="Quick"
while food != "Quick":
    
    list_of_food.append(food)
    print(list_of_food)
    food= input("Enter choice of food ")
else:
     print("The list of your favourite foods are", list_of_food)   