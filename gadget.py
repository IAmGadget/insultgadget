#Section 1 - Do you know gadget?
know_gadget = input("Hello! Do you know gadget? ")

#Handles if the answer to section 1 is yes
if know_gadget == "yes":
    answer1 = input("He's so stupid isn't he! ")
    if answer1 == "yes":
        print("It's so good that you feel the same way about that idiot!")
    elif answer1 == "no":
        print("Well than you must also be a complete idiot if you think that!")
    else:
        print("I do not understand you, you complete imbocile")

#Handles if the answer to section 1 is no
elif know_gadget == "no":
    print("That's a good thing tbh")

#Handles if the answer to section 1 is maybe
elif know_gadget == "maybe":
    answer2 = input("What the hell do you mean by maybe? ")
    if answer2 == "idk":
        print("Well you better get knowing smh")
        answer3 = int(input("What is your IQ? "))
        if answer3 == 0:
            print("You should really get yourself checked out if you are really that dense!")
        elif answer3 <=50:
            print("Damn you are pretty stupid, you should probably stop talking to me!")
        elif answer3 <= 100:
            print("Guess you aren't as dumb as I initially thought... you can still get outta here though!")
        elif answer3 > 100:
            print("Okay Einstein, jeez")

#Handles if you ask the program if you asked
elif know_gadget == "did i ask?":
    print("Sorry solid! Didn't know you were that hard bruv.")

elif know_gadget == "test1":
    print("This is purely a pycharm commit test")

#The code explains itself
elif know_gadget == "daddy":
    print("uwu")

#Handles if the user inputs anything but 'yes', 'no' or 'maybe' into section 1
else:
    print("I do not understand you, you complete imbocile")
