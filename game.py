print("hello world")
escape = ""



class Player:
    def __init__(self, location, inventory, health):
        self.location = location
        self.inventory = inventory
        self.health = health
class Location:
    def __init__(self, name, description, connections, items):
        self.name = name
        self.description = description
        self.connections = connections
        self.items = items
class Item:
    def __init__(self, name, description, properties):
        self.name = name
        self.description = description
        self.properties = properties
class IceCream():
    def __init__(self, name, description):
        self.name = name
        self.description = description


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



    

