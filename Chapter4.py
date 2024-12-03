def chapter_4():

    #lookaround=False
    weakpoint=False
    #breakthelock=False

    introduction_4=True
    incage=0
    action1=1
    action2=2
    action3=3

    keepacting=True
    print("The subordinate informed the minions about the investigation and you got kidnapped")
    print("The character finds himself in a clandestine prison")
    currentlocation=incage

    while keepacting:
        if currentlocation==incage:
            if introduction_4:
                print('You wake up and found yourself emprisoned and you want to find a way to escape')
                introduction_4=False

            print("1)Look around the cage")
            print("2)Try to find a weak point")
            print("3)Try break the lock")
            try:
                currentlocation=int(input("Enter the number that corresponds to your desire choide\n"))
            except ValueError:
                print("Invalid option, please enter a valid option")

        elif currentlocation==action1:
            print("You walk around and you see humid walls and a bar window where you can see that the prison is located somewhere around in a port")
            currentlocation=incage

        elif currentlocation==action2:
            if weakpoint==False:
                print("In the back of the cage where the rusty bars are easy to move you are able to move them from their position enaabling you to escape ")
                weakpoint=True
                chapter_4_escape()
                return True
                

        elif currentlocation==action3:
            print("While trying to break the lock you made too much noise and alerted the guards")
            print("You got incapacitated and reelocated to another cage")
            print("Use other option")
            currentlocation=incage


def chapter_4_escape():
     
    sneak=False
    #run=False

    introduction=True
    hallway=0
    decision1=1
    decision2=2

    keepacting=True
    print("You have escaped from the cage now you need to escape from the prison")
    currentlocation=hallway

    while keepacting:
        if currentlocation==hallway:
            if introduction:
                print('You found yourself in the prison dirty hallway, where after crossing it there is a window from where you can escape')
                introduction=False

            print("1.)Choose the action to run")
            print("2)Choose the action to sneak")
            try:
                currentlocation=int(input("Enter the number that corresponds to your desire choice\n"))
            except ValueError:
                print("Invalid option, please enter a valid option")

        elif currentlocation==decision1:
            print("While you are running you made too much noise and alerted the guards, then you got captured")
            print("you got incapacitated and relocated to another cage")
            print("use other option")
            currentlocation=hallway

        elif currentlocation==decision2:
            if sneak==False:
                print("You sneaked and reached window to escape")
                print("congrats you have escaped from the prison")
                print("continues in chapter 5")
                return

            
            
            


            
                  