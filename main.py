
print("")
print("                                  ,'\\")
print("    _.----.        ____         ,'  _\   ___    ___     ____")
print("_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.")
print("\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |")
print(" \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |")
print("   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |")
print("    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |")
print("     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |")
print("      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |")
print("       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |")
print("        \_.-'       |__|    `-._ |              '-.|     '-.| |   |")
print("                                `'                            '-._|")
print("")
print("Pokemon Battle")
print("")

import json
import random

# read Pokemon file into dictionary
pokemons_file = open('pokemons.json') # opening JSON file
pokemons = json.load(pokemons_file) # returns JSON object as a dictionary
pokemons_file.close() # Closing file

print(pokemons[0])

while True:
    print("1. Show pokemon by index")
    print("2. Top 10 strongest pokemons")
    print("3. Top 10 weakest pokemons")
    print("4. Battle of 2 pokemons")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        x = input("Ieraksti ciparu: ")
        print(pokemons[int(x)])
        pass
    elif choice == '2':
        def attack(n):
            return int(n["attack"])
        pokemons.sort(key = attack, reverse=True)
        print(pokemons[:10])
    elif choice == '3':
        def attack(n):
            return int(n["attack"])
        pokemons.sort(key = attack, reverse=False)
        print(pokemons[:10])
        pass
    elif choice == '4':
        # Battle
        pok1 = random.choice(pokemons)
        x = int(input("Ieraksti ciparu: "))
        f = random.randint(5,20)
        pok2 = pokemons[x]
        print(pok1["name"], " ", pok2["name"])
        while pok1["total"] > 0 and pok2["total"] > 0:
            damage1 = pok2["attack"] - pok1["defense"] + f
            damage2 = pok1["attack"] - pok2["defense"] + f
            pok1["total"] = pok1["total"] - damage1
            pok2["total"] = pok2["total"] - damage2
            if pok1["total"] <= 0:
                print (pok1["name"])
            elif pok2["total"] <= 0:
                print (pok2["name"])
        
        # https://www.w3schools.com/python/ref_random_choice.asp - random choice
        # Computer choosing one random Pokemon from list
        # Player choosing by entering Pokemon index
        # Damage is calculated by: (attack of Pokemon 2) - (defense of Pokemon 1) + (random from 5 to 20), and vice-versa
        # Player reaching 0 health - lost
        pass

    elif choice == '5':
        print("Exiting")
        break
    else:
        print("Invalid choice, choose from 1 to 5")

    print("==========================")


