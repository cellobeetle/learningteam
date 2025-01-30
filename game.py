print("\nhello world")
escape = ""



# this is the main game loop
print("This is the location you are in")
while(True):
    choice = input("\ndo you want to sit?")
    if(choice == "yes"):
        print("You are sitting. How pleasant it must be to sit")
        see = input("You look out the window. It is raining. Are you cold?")
    if(choice == "no"):
        print("You remain standing. Your legs must be tired")
    if(see == "yes"):
        print("That's too bad, we only have ice cream here.")
    elif(see == "no"):
        print("Oh good, maybe you should eat some ice cream:)")
    escape = input("do you want to leave?")
    if(escape == "yes"):
        break
    elif(escape == "no"):
        print("Oh good, I like having you here")



    

