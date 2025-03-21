

running = True



class Player:
    def __init__(self, location, inventory):
        self.location = location
        self.inventory = inventory
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

locations = {
    "parlor" : Location("Parlor", "a cozy ice cream parlor. The checkered floor is cool against your socked feet.", ["rink"], ["button", 
                                                                                                                               "chair"], []), 
    "rink" : Location("Rink", "a vast roller skating rink, people are zooming. Woot woot!", ["parlor", "bathroom", "laundry"], [], []), 
    "bathroom" : Location("Bathroom", "a bathroom that is surprisingly clean, but it's still weird to be wearing socks here. Someone is crying in the corner", ["rink"], ["handSoap"], []), 
    "laundry" : Location("Laundry", "the laundry room. Piles of roller skates are here. It surprisingly doesn't smell too bad.", ["rink", "garbage"], ["rollerskate"], [])
    }

#{"button" : Item("button", "big red button, how tempting", "opens door into rink"), "chair" : Item("chair", "a four legged chair with a pink checkered cushion", "allows for sitting")}

player = Player(locations["parlor"], [])


class Command:
    def __init__(self, inputText):
        self.inputText = inputText
        self.inputArray = inputText.split()

    def remove_all_else(self, list_to_keep):
        newArray = []
        for element in self.inputArray:
            if element in list_to_keep:
                newArray.append(element)
        self.inputArray = newArray

commands={"look":"tells you about surroundings", "inspect":"tells you about an item's appearance", "go":"move to new area", "grab":"picks up an item", "exit":"exit the game"}



print("hi friend! type 'help' for a list of commands\nyou are in a cozy ice cream parlor. The checkered floor is cool against your socked feet.")
while running:
    command = Command(input("enter a word: "))
    command.remove_all_else(["go","look", "grab", "help"] + player.location.connections + player.location.items)

    if "exit" in command.inputArray:
        break


    if "go" in command.inputArray:
        for option in player.location.connections:
            if option in command.inputArray:
                player.location = locations[option]
                print(f"you are now in {player.location.description}")

    if "look" in command.inputArray:

        print(f"you can go to {player.location.connections}")
        print(f"you can grab {player.location.items}")

    if "grab" in command.inputArray:
        for item in player.location.items:
            if item in command.inputArray:
                player.inventory.append(item)
                print(f"you grabbed the {item}")
                del player.location.items[item] 
                break
    
    if "inspect" in command.inputArray:
        for item in player.location.items:
            print(item.description)


    if "help" in command.inputArray:
        for key, value in commands.items():
            print(f"{key}: {value}")

print("goodbye friend")
