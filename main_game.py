#Diego Lozano
#CSS225 Milestone 3 
#This game is a mystery game where the player has to collect clues and find the responsible that comitted the crime.
import Chapter1
import Chapter2
import Chapter3
import Chapter4
import Chapter5


def main():

    Gameover=False
    chapter1=True
    chapter2=True
    chapter3=True
    chapter4=True 
    chapter5=True
    
    game_is_running=True
    
    while game_is_running:
        if chapter1:
            chapter2 = Chapter1.chapter_1()
            chapter1 = False
        elif chapter2:
            chapter3 =Chapter2.chapter_2()
            chapter2 = False
        elif chapter3:
            chapter4= Chapter3.chapter_3()
            chapter3=False
        elif chapter4:
            chapter5=Chapter4.chapter_4()
            chapter4=False
        elif chapter5:
            Gameover=Chapter5.chapter_5()
            chapter5=False
        
    
    if Gameover==True:
        print("You have completed the Game")
    
            
main() 
