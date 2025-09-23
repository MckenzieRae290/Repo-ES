
hero_stats = {
    "name" : "hero", # key : value (name -> key) (hero -> value)
    "strength": 7,
    "health" : 100,
}



def quit ():
    print ("You Chose To Flee\n")
    print ("Game Over\n")
    return False 

def player_stats ():
    print("you are:")
    for key, value in hero_stats.items():
        print (f"{key} : {value}" )



def player_move():
    pass

def player_attack():
    pass



isPlaying = True 

hero_stats["name"] = input ("What is your name?\n").lower()

player_stats()

while (isPlaying):

    action = input ("\nSelect Action: Attack, Move & Flee\n").lower()
    
    print (f"Player Action: {action}")

    if (action == "flee"):
        isPlaying = quit() #<-- isPlaying = False
    elif (action == "attack"):
        player_attack()
    elif (action == "move"):
        player_move()
    else:
        print(f"[action] is an invalid action")
