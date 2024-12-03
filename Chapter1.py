def chapter_1():
    pass

    FindsMurderWeapon= False
    FindsFingerprints= False
    FindsDNAsamples= False
    Enoughclues= False
   
    introduction = True 
    inOffice = 0
    inAssemblingline= 1
    inMachineryRoom= 2
    inHallway= 3
    TalktoWorkers= 4
    Wrapup=5

    keepexploring= True
    TalktoWorkers_2=True
    print("It was in the middle of the night, heavy rain falls in the hot summer")
    print("The character finds himself at the crime scene in the factory")
    currentlocation = inOffice
    player_choice = TalktoWorkers
    
    while keepexploring:
        if currentlocation == inOffice:
            if introduction:
                print("You are in the office finding yourself where to begin the investigation")
                introduction = False
            
            print("1.)The Assembling Line")
            print("2.)The Machinery Room")
            print("3.)The Hallway")
            print("4.)Talk to the Workers")
            print("5.)Wrapup")
            try:
                currentlocation = int(input("Enter the number that corresponds to your desire choice.\n"))
            except ValueError:
                print("Invalid option please enter a valid option")
                continue
        
        elif currentlocation==inAssemblingline: #Assemnly line
            if FindsMurderWeapon ==False:
                print("You have found the weapon that the murder used to commit the crime.")
                FindsMurderWeapon= True
            else:
                print("You have collected all of the clues at this location. You can still explore this location but there's nothing else to be found here")
            print("you return to the office to place the clue")
            currentlocation=inOffice

        elif currentlocation==inMachineryRoom:
            if FindsFingerprints ==False:
                print("You have found the fingerprints of the murder")
                FindsFingerprints= True
            else:
                print("You have collected all of the clues at this location. You can still explore this location but there's nothing else to be found here")
            print("you return to the office to place the clue")
            currentlocation=inOffice
        
        elif currentlocation==inHallway:
            if FindsDNAsamples ==False:
                print("You have found DNA samples that the murder left befind, he didn't covered his steps")
                FindsDNAsamples= True
            else:
                print("You have collected all of the clues at this location. You can still explore this location but there's nothing else to be found here")
            print("you return to the office to place the clue")
            currentlocation=inOffice

        elif currentlocation==TalktoWorkers:
            while TalktoWorkers_2:
                print("Now you are going to interrogate a worker")
                print("1.)where do you were last night?")
                print("2.)you saw something suspecious?")
                print("3.)how do you know the victim?")
                print("4.)back to the decision trade")
                    
                try:
                    player_choice= int(input("Enter the number that corresponds to your desire question.\n"))
                    if player_choice ==1:
                        print("The worker confess that he was at home when the crime happened")
                    elif player_choice==2:
                        print("The worker saw someone sneaking around late at night")
                    elif player_choice==3:
                        print("The worker said that he worked with the victim and knew him for a few years")
                    elif player_choice==4:
                        print("You decided to back to the office")
                        currentlocation = inOffice
                        TalktoWorkers_2 = False
                except ValueError:
                        print("Invalid option please enter a valid question option")
            
        elif currentlocation==Wrapup:
            if FindsMurderWeapon == False:
                print("You still need to find a clue in the Assembling line")
                currentlocation=inOffice
            elif FindsFingerprints==False:
                print("You still need to find a clue in the Machinery room")
                currentlocation=inOffice
            elif FindsDNAsamples==False:
                print("You still need to find a clue in the hallway")
                currentlocation=inOffice
            else:
                print("Congrats, you found all of the clues and you are one step ahead to complete this mystery. You can move to chapter 2")
                return True
                                   
