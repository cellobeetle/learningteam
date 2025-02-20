print("hello world")
escape = ""



class Player:
    def __init__(self, location, inventory, health):
        self.location = location
        self.inventory = inventory
        self.health = health
class Location:
    def __init__(self, name, description, connections, items, icecream):
        self.name = name
        self.description = description
        self.connections = connections
        self.items = items
        self.icecream = icecream
class Item:
    def __init__(self, name, description, properties):
        self.name = name
        self.description = description
        self.properties = properties
class IceCream:
    def __init__(self, name, description):
        self.name = name
        self.description = description
class Button:
    def __init__(self, name, description, locationa, locationb):
        self.name = name
        self.description = description
        self.locationa = locationa
        self.locationb = locationb

def create_game_world():
    locations = {
    "mainParlor" : Location("Main Parlor", "This is a cozy ice cream parlor. The checkered floor is cool against your socked feet. There are chairs by the window, and ice cream behind a counter", ["rollerRink"], ["button1", "chair",], []), 
    "rollerRink" : Location("Roller Rink", "A vast roller skating rink, people are zooming. Woot woot!", ["mainParlor", "bathroom", "laundry"], [], []), 
    "bathroom" : Location("Bathroom", "This bathroom is surprisingly clean, but it's still weird to be wearing socks here. Someone is crying in the corner", ["rollerRink"], ["handSoap"], []), 
    "laundry" : Location("Laundry Room", "Piles of roller skates are here. It surprisingly doesn't smell too bad.", ["rollerRink", "garbage"], ["rollerskate"], [])
    }




# this is the main game loop
print("You are in an ice cream parlor. The checkered floor is cool against your socked feet.")
while(True):
    choice = input("\nDo you want to sit?")
    if(choice == "yes"):
        print("You are sitting. How pleasant it must be to sit")
        see = input("You look out the window. It is raining. Are you cold?")
        if(see == "yes"):
            print("That's too bad, we only have ice cream here.")
        elif(see == "no"):
            print("Oh good, maybe you should eat some ice cream:)")
    if(choice == "no"):
        print("You remain standing. Your legs must be tired")
    
    escape = input("do you want to leave?")
    if(escape == "yes"):
        print("Good bye, friend:)")
        break
    elif(escape == "no"):
        print("Oh good, I like having you here")



    

