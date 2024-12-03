def chapter_2():
    
    Askwhathappened=False
    Askforsuspect= False
    Askforenemies=False

    introduction_2=True
    inhouse=0
    inquestion1=1
    inquestion2=2
    inquestion3=3
    wrapup_2=4

    keepinterrogating=True
    print("The character now to search for information interrogates a witness")
    print("The character located in the witness house")
    currentlocation=inhouse
    

    while keepinterrogating:
        if currentlocation==inhouse:
            if introduction_2:
                print("You are in the witness house thinking what questions you are going to ask him")
                introduction_2=False

            print("1.)Ask what happened")
            print("2.)Ask for possible suspect")
            print("3.)Ask for possible victim enemies")
            print("4.)Wrapup")
            try:
                currentlocation = int(input("Enter the number that corresponds to your desire choice. \n" ))
            except ValueError:
                print("invalid option please enter a valid option")

        elif currentlocation==inquestion1:
            if Askwhathappened == False:
                print("It happened so fast, I was working on my line at the factory when I heard a scream and when I went to revise I found the dead body layinh in the floor")
                Askwhathappened=True
            else:
                print("You have already asked this question")
                print("Now return to the option list to ask more")
            currentlocation=inhouse
        
        elif currentlocation==inquestion2:
            if Askforsuspect == False:
                print("I saw someone wearing a hood enter the factory early in the morning. I couldn't see his face, but I noticed that his movements seemed to be planned, since he knew what he was doing. To me, it seems suspecious")
                Askforsuspect=True
            else:
                print("You have already asked this question")
                print("Now return to the option list to ask more")
            currentlocation=inhouse

        elif currentlocation==inquestion3:
            if Askforenemies ==False:
                print("The victim was a cool guy he avoided to discuss or enter into a problem with someone, but recently he looked nervous and didn't wanted to talk to anyone")
                Askforenemies=True
            else:
                print("You have already asked this question")
                print(" Now return to the option list to ask more")
            currentlocation=inhouse

        elif currentlocation==wrapup_2:
            if Askwhathappened ==False:
                print("You still need to ask for context")
                currentlocation=inhouse
            elif Askforsuspect==False:
                print("You still need information for the suspect")
                currentlocation=inhouse
            elif Askforenemies ==False:
                print("You still need to know if the victim had enemies")
                currentlocation=inhouse
            else:
                print("CONGRATS, you gathered the information that you need, now you connected all information leading to the suspect. You can move to chapter 3")
                return True

        


        


    
    