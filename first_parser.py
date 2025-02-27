running = True



class Player:
    def __init__(self, location):
        self.location = location
class Location:
    def __init__(self, name, description, connections, items, icecream):
        self.name = name
        self.description = description
        self.connections = connections
        self.items = items
        self.icecream = icecream
locations = {
    "parlor" : Location("Parlor", "a cozy ice cream parlor. The checkered floor is cool against your socked feet. There are chairs by the window, and ice cream behind a counter", ["rollerrink"], ["button1", "chair",], []), 
    "rollerrink" : Location("Roller Rink", "a vast roller skating rink, people are zooming. Woot woot!", ["parlor", "bathroom", "laundry"], [], []), 
    "bathroom" : Location("Bathroom", "a bathroom that is surprisingly clean, but it's still weird to be wearing socks here. Someone is crying in the corner", ["rollerrink"], ["handSoap"], []), 
    "laundry" : Location("Laundry Room", "the laundry room. Piles of roller skates are here. It surprisingly doesn't smell too bad.", ["rollerrink", "garbage"], ["rollerskate"], [])
    }

player = Player(locations["parlor"])


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




while running:
    command = Command(input("enter a word: "))
    print(command.inputArray)
    command.remove_all_else(["go", "parlor", "roller", "bathroom", "laundry"] + player.location.connections)

    if "exit" in command.inputArray:
        break

    if "go" in command.inputArray:
        for option in player.location.connections:
            if option in command.inputArray:
                player.location = locations[option]
                print(f"you are now in {player.location.description}")


    print(f"you can go to {player.location.connections}")

print("goodbye, friend")
