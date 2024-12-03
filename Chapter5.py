def chapter_5():

    dodge1_left=False
    #dodge1_Right=True

    introduction_5=True
    office=0
    decision1=1
    decision2=2

    keepchasing=True
    print("Free from his captors the character ties up all the loose ends and finds the responsible for the crime and finds out is the factory's owner")
    print("Back at the factory the character confronts the criminal and finds out that he wanted to sabotage the factory to get more money")
    currentlocation=office

    while keepchasing:
        if currentlocation==office:
            if introduction_5:
                print("You found yousrelf confronting the owner but he escapes and you decided to chase him, he pulls out a gun and shoots you ")
                introduction_5=False

            print("1.) Decide to dodge left")
            print("2.) Decide to dodge right")
            try:
                currentlocation=int(input("Enter the number that corresponds to your desire choice\n"))
            except ValueError:
                print("Invalid option, please enter a valid option")

        elif currentlocation==decision1:
                if dodge1_left==False:
                    print("You dodged left making the owner to miss the shot")
                    dodge1_left=True
                    chapter_5_chase()
                    return True
                
        elif currentlocation==decision2:
             print("you dodged to the right, but the bullet hitted you and died")
             print("use anothe option")
             currentlocation=office

def chapter_5_chase():
     
    dodge2_right=False

    introduction=True

    hallway=0
    finaldecision1=1
    finaldecision2=2

    keepchasing=True
    print("The owner hides and you decide to find him")
    currentlocation=hallway

    while keepchasing:
        if currentlocation==hallway:
            if introduction:
                print("The owner surprise you and shoots again")
                introduction=False

            print("1.) Decide to dodge left")
            print("2.) Decide to dodge right")
            try:
                currentlocation=int(input("Enter the number that corresponds to your desire choice\n"))
            except ValueError:
                print("Invalid option, please enter a valid option")

        elif currentlocation==finaldecision1:
            print("You decided to dodge left, but the bullet hitted you and died")
            print("use another option")
            currentlocation=hallway

        elif currentlocation==finaldecision2:
            if dodge2_right==False:
                print("You dodged right making the owner miss the shot")
                print("character jumps over the owner and incapacitates him")
                print("CONGRATS you have completed the game")
                return
        
              