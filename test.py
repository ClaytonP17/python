print("You come to a cave.  Go in or go back?")
choice=input("Type 1 for go in, Type 2 for go back")
if choice=="1":
    print("You walked into the cave, but it is dark.")
    choice2=input("There is a torch.  Type 1 to use it.")
    if choice2=="1":
        print("You can see the cave.")
    elif choice2=="2":
        print("Something else")
else:
    print("You went back home.")
