print("Hello there! I have an exciting story about a runaway dog. I can't wait to tell it.")
print("Before the story begins, I have a few questions that I need you to answer.")

print("After typing your answer, please press the enter key. \n")

input("\nPress the enter key to continue...")

breed = input("\nWhat Breed is the dog?  ")
while (len(breed) == 0) :
    breed = input("Please enter your breed:  ")

dogName = input("\nWhat is the dogs name?  ")
while (len(dogName) == 0) :
    dogName = input("Please enter your dog's name  ")

town = input("\nWhat is the name of your town?  ")
while (len(town) == 0) :
    town = input("Please enter the name of your town:  ")

pond = input("\nWhat kind of pond do you like?  ")
while (len(pond) == 0) :
    pond = input("Please enter the kind of pond you like:  ")

number = input("\nWhat is your favorite number:  ")
while not number.isdigit() :
        number = input("Value not recognized. What is your favorite number:  ")
number = int(number)

userName = input("\nWhat is your name?  ")
while (len(userName) == 0) :
    userName = input("Please enter your name:  ")

playAgain = "y"
while playAgain.lower() == "yes":
    print("\nLet the games begin!")


    print("\nOnce upon a time there was a" ,breed, "named" ,dogName + ".")

    print(dogName, "was left at the local shelter for the weekend while" ,userName, "went away.")

    print(dogName, "liked going for morning runs." ,dogName, "really wanted to go for a run this sunny and warm day, and saw that the gate was accidently left open!")

    print(dogName, "ran out of the gate heading straight towards" ,town + "never looking back.")

    print("\nWhile walking down the street" ,dogName, "arrived at a nice looking",pond, "pond.")

    print(dogName, "wanted to cool off because it was really hot there today")

    sneakIntoPond = input("\nShould " + str(dogName) + " sneak into the pond?  Type Yes or No?  ")

    if sneakIntoPond == "yes":
        print(dogName, "\nsneaks into the" ,pond, "pond.")
        print("When the homeowners find" ,dogName, "jumping and playing in the" ,pond, "pond they yell very loud while they try getting the dog out of the pond." ,dogName, "gets very scared and runs between the homeowners and into their prized rose garden, trampling their award winning roses!")
        print("The homeowners are very angry and call the poice.")
        print(dogName, "runs off down the road before the police arrive.")
    else:
        print("\n" + dogName + " decides it is too risky to sneak into the " ,pond, "pond.")
        print("Being too afraid of getting caught, the dog sees a sprinkler at a nearby house and lays in the puddle on the sidewalk for " ,number, "minutes before the sprinkler automatically turns off, forcing the dog to leave.")

    print("\nAfter a hot long day exploring " ,town,"," ,dogName,  "comes across a family cookout in the park.")
    print(dogName, "had played and cooled off, and now the dog was very hungry!")

    checkOutCookout = input("\nShould " + str(dogName) + " check out the cookout?  Type yes or no?  ")

    if checkOutCookout == "yes":
        print(dogName, " decides to go ahead and ckeck out the cookout, everyone looks like they are having so much fun!")
        print(dogName, " spends",number, "minutes eating the bbq food and playing with all the children before laying down for a quick nap before heading off.")
   
    else:
        print(dogName, " decides not to go into the family cookout." ,breed, " get scared very easily.")
        print("\nBeing too afraid of all the new people and worried that someone might call the police,")
        print(dogName, "decides to just keep on walking hoping that no one notices, " ,dogName, "does not want to make a scene.")

    if sneakIntoPond == "yes" and checkOutCookout == "yes":
        print("\nAfter spending a very adventurous day in " ,town, "," ,dogName, "was caught by the police.")
        print("Luckily, the police officer noticed the name " ,userName, "on the dogs collar tag and remebered the kennel calling in for a runaway dog.")
        print(dogName, "was successfully returned to the kennelwith a full belly!")

    elif sneakIntoPond == "yes" and checkOutCookout == "no":
        print("\nAfter spending a day in " ,town, "," ,dogName, "was caught by the police.")
        print("Luckily, the police noticed " ,userName, "was printed on the dogs collar, and the dog was returned to the kennel successfully.")
        print("Surprisingly, the police did not realize that is was infact " ,dogName, " that trampled the homeowners prized rose garden!")

    elif sneakIntoPond == "no" and checkOutCookout == "yes":
        print(dogName, "Spent a wonderful day in the city." ,dogName, "played with the children at the cookout, ate lots and lots of food, and took a wonderful nap before someone realized that ",dogName, "did not belong to anyone at the cookout.")
        print("so, the called the police and held the dog until the police arrived. The family members told the police office that" ,dogName, "was very well behaved and pointe dout his owners name on his collar. The police officer returned" ,dogName, "to teh kennel where " ,userName, "was waiting for him.")
        print(dogName, "Knew that" ,userName, "was very angry, but," ,dogName, "did have a really great day!")

    else: 
        print("\nAfter spending a day in " ,town, "," ,dogName, " was caught by the police.")
        print("Luckily, they spotted the name " ,userName, "on the dogs collar.")
        print(dogName, " was successfully returned to the kennel. The police could not belive how well behaved the dog had been all day.")


    print("\nTHE END!!!!")


    playAgain = input("Do you want to play again? Please enter yes or no:  ")

    print("\nThis game will self destruct in 60 seconds!")
    for seconds in range(60, 0, -1):
                print(seconds, end = " \r")
                import time
                time.sleep(1)

    
















