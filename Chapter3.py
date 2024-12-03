def chapter_3():
    

    Asklocation=False
    Askcharacteristics=False
    Askmotivation=False

    introduction_3=True
    inbar=0
    inquery1=1
    inquery2=2
    inquery3=3
    wrapup_3=4

    keepasking=True
    print("The character now with all of information goes to the location where the first suspect can be found")
    print("The first suspect is found in a clandestine bar")
    currentlocation=inbar

    while keepasking:
        if currentlocation==inbar:
            if introduction_3:
                print("You are in the front of the bartender thinking what are you are going to ask about the suspect")
                introduction_3=False

            print("1.)Ask where to find the suspect")
            print("2)Ask for physical characteristics")
            print("3.)Ask for the suspect motivations")
            print("4.)Wrapup")
            try:
                currentlocation = int(input("Enter the number that corresponds to your desire choice\n"))
            except ValueError:
                print("invalid option, please enter a valid option")

        elif currentlocation==inquery1:
            if Asklocation ==False:
                print("The guy you are looking for is sitted in the lonely table located in the far corner in the back")
                Asklocation=True
            else:
                print("You have already asked this question")
                print("Now return to the option list to ask more about the suspect")
            currentlocation=inbar
            
        elif currentlocation==inquery2:
            if Askcharacteristics ==False:
                print("When he enters the bar he is always wearing a hood, tall height, and he never talks or do something else besides ordering a beer")
                Askcharacteristics=True
            else:
                print("You have already asked this question")
                print("Now return to the option list to ask more about the suspect")
            currentlocation=inbar
            
        elif currentlocation==inquery3:
            if Askmotivation==False:
                print("He is a thought guy, no one wants to mess with him, all I know he works for someone from the underworld, but by fear no one is willing to ask for who is he working for.")
                Askmotivation=True
            else:
                print("You have already asked this question")
                print("Now return to the option list to ask more about the suspect")
            currentlocation=inbar
        
        elif currentlocation== wrapup_3:
            if Asklocation==False:
                print("You still need to know where to find the suspect")
                currentlocation=inbar
            elif Askcharacteristics==False:
                print("You still need to know the suspect characteristics")
                currentlocation=inbar
            elif Askmotivation==False:
                print("You still need to know what are the suspect motivations")
                currentlocation=inbar
            else:
                print("With all of the information gained now you can comfron the subordinate and ask for the real murder")
                chapter_3_interrogation()
                return True

def chapter_3_interrogation():

    Askboss=False
    Askmotivations_2=False

    introductionsuspect=True
    intable=0
    interrogate1=1
    interrogate2=2
    wrapup_table=3

    keepasking=True
    print("Now you are walking where the subordinate is located")
    currentlocation=intable

    while keepasking:
        if currentlocation==intable:
            if introductionsuspect:
                print("You sit in front of the subordinate and while looking at him you are going to ask some questions to him")
                introductionsuspect=False

            print("1.) Ask, who is your boss?")
            print("2)Ask, What motivated you to follow your boss?")
            print("3)Wrapup")
            try:
                currentlocation= int(input("Enter the number that corresponds to your desire choice\n"))
            except ValueError:
                print("invalid option, please enter a valid option")

        elif currentlocation==interrogate1:
            if Askboss==False:
                print("I don't need you to give you answers or tell you who is my boss because I am my own boss")
                Askboss=True
            else:
                print("You have already asked this question")
                print("Now return to the option list to ask something different")
            currentlocation=intable

        elif currentlocation==interrogate2:
            if Askmotivations_2==False:
                print("I am my own boss and the reason why I wanted this life is because the system is corrupted")
                Askmotivations_2=True
            else:
                print("You have already asked this question")
                print("Now return to the option list to ask something different")
            currentlocation=intable

        elif currentlocation==wrapup_table:
            if Askboss==False:
                print("You still need to know who is in charge")
                currentlocation=intable
            elif Askmotivations_2==False:
                print("You still need to know why he contributed to the crime")
                currentlocation=intable
            else:
                print("The subordinate decides to leave you without a rational answer and you decide to chase him outside of the bar")
                print("When you step outside 2 guys drug you and carry you into a van, YOU GOT KIDNAPPED")
                print("Continue in chapter 4")
                return


