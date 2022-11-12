'''10/10/2020 '''
'''This program is done by Diaa Almughrabi'''

import random
import master_mind_GUI
def _main_():
    def Master_mind_game(guess,computer):
        correct_place=0
        wrong_place=0
        for choice in range(len(guess)) :   
            if guess[choice] == computer[choice]:
                correct_place+= 1
            elif  guess[choice] in computer:
                wrong_place+= 1 
        return correct_place,wrong_place

    def computer_guessing():
        list1= []
        while len(list1)<4:
            computer_choice= random.randint(0,5)
            if computer_choice not in list1: 
                list1.append(computer_choice)
        return list1

    window= master_mind_GUI.create_GUI()
    attempts= 0
    secret_choice=computer_guessing()
    playing= True 
    while playing== True :
        guess= master_mind_GUI.make_guess(attempts,window)
        places= Master_mind_game(guess,secret_choice)
        master_mind_GUI.peg_feedback(attempts,places[0],places[1],window)
        attempts+=1 
        if places[0]==4 :
            master_mind_GUI.gameover_screen(attempts,"Winner")
            playing=False 
        elif attempts== 7 :
            master_mind_GUI.gameover_screen(attempts,"loser")
            playing= False 
    return
_main_() 
