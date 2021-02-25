# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 16:17:30 2021

@author: ramon
"""

from random import randint
import time


def slow_text(string, delay, wait):
    """ Print string letter after letter instead of at once. """

    for char in string:
        print(char, end='')
        time.sleep(delay)
    time.sleep(wait)  


team1_scores = 0
team2_scores = 0
quit_loop = 0

def scores_question(team1_name, team2_name, question, question_outcome):
    """ Gives a score to a team depending on correct answering a question. 
        Gives also a score for the opponents team"""
    
    global team1_scores, team2_scores
    quit_loop = False
    question_right = randint(1, 10)
    question_wrong = randint(1, 6) #chance to score a penalty when question is wrong
    chance_opponent = randint(1, 3) #chance for the opponent to score
    true = ["True", "true", "T", "t"]
    false = ["False", "false", "F", "f"]
    
    print(question)
    while True:
        choice = input("> ")
        if question_outcome == "True": #answer is true
            if choice in false:
                if question_wrong < 2:
                    team1_scores += 1
                    slow_text("Wrong answer!\n", 0, 2)
                    slow_text(f"However, {team1_name} manages to score a really lucky goal!\n", 0, 3)
                    slow_text(f"\nThe score is {team1_scores} -- {team2_scores}\n", 0, 3)
                    if team1_scores == 5:
                        slow_text(f"Congratulations, {team1_name} wins the Champions League after penalties!!!\n", 0, 5)
                        return False
                    break
                else:
                    team1_scores += 0
                    slow_text("Wrong answer!\n", 0, 2)
                    slow_text("Oof, brilliant safe from the goalkeeper!\n", 0, 3)
                    slow_text(f"\nThe score is {team1_scores} -- {team2_scores}\n", 0, 3)
                    break
            elif choice in true:
                if question_right <= 8:
                    team1_scores += 1
                    slow_text("Correct!\n", 0, 2)
                    slow_text(f"{team1_name} manages to score the penalty!!\n", 0, 3)
                    slow_text(f"\nThe score is {team1_scores} -- {team2_scores}\n", 0, 3)
                    if team1_scores == 5:
                        slow_text(f"Congratulations, {team1_name} wins the Champions League after penalties!!!\n", 0, 5)
                        return False
                    break
                else:
                    team1_scores += 0
                    slow_text("Correct!\n", 0, 2)
                    slow_text("Auch, that is an unlucky shot! He misses..\n", 0, 3)
                    slow_text(f"\nThe score is {team1_scores} -- {team2_scores}\n", 0, 3)
                    break
            else:
                slow_text("That is not a valid answer, please try again.\n", 0, 3)  
        elif question_outcome == "False": #answer is false
              if choice in true:
                if question_wrong < 2:
                    team1_scores += 1
                    slow_text("Wrong answer!\n", 0, 2)
                    slow_text(f"However, {team1_name} manages to score a really lucky goal!\n", 0, 3)
                    slow_text(f"\nThe score is {team1_scores} -- {team2_scores}\n", 0, 3)
                    if team1_scores == 5: 
                        slow_text(f"Congratulations, {team1_name} wins the Champions League after penalties!!!\n", 0, 5)
                        return False
                    break
                else:
                    team1_scores += 0
                    slow_text("Wrong answer!\n", 0, 2)
                    slow_text("Oof, brilliant safe from the goalkeeper!\n", 0, 3)
                    slow_text(f"\nThe score is {team1_scores} -- {team2_scores}\n", 0, 3)
                    break
              elif choice in false:
                if question_right <= 8:
                    team1_scores += 1
                    slow_text("Correct!\n", 0, 2)
                    slow_text(f"{team1_name} manages to score the penalty!!\n", 0, 3)
                    slow_text(f"\nThe score is {team1_scores} -- {team2_scores}\n", 0, 3)
                    if team1_scores == 5:
                        slow_text(f"Congratulations, {team1_name} wins the Champions League after penalties!!!\n", 0, 5)
                        return False
                    break
                else:
                    team1_scores += 0
                    slow_text("Correct!\n", 0, 2)
                    slow_text("Auch, that is an unlucky shot! He misses..\n", 0, 3)
                    slow_text(f"\nThe score is {team1_scores} -- {team2_scores}\n", 0, 3)
                    break
              else:
                  slow_text("That is not a valid answer, please try again.\n", 0, 3)
    # Penalty opponent
    slow_text("\nOpponents turn!\n", 0, 3)
    if chance_opponent <= 1:
        team2_scores += 1
        slow_text(f"{team2_name} manages to score the penalty!\n", 0, 3)
        slow_text(f"\nThe score is {team1_scores} -- {team2_scores}\n", 0, 3)
        if team2_scores == 5:
            slow_text(f"You lost! {team2_name} wins the Champions League after penalties...\n", 0, 5)
            return False
    else:
        team2_scores += 0
        slow_text(f"{team2_name} misses the penalty!\n", 0, 3)
        slow_text(f"\nThe score is {team1_scores} -- {team2_scores}\n", 0, 3)
        
        
class FootballFinal:

    def enter_world(self):
        slow_text("Reporter:\n", 0, 3)
        slow_text("Welcome to the final of the Champions League on this beautiful day!\n", 0, 3)
        slow_text("Today, the two teams will battle for eternal glory.\n", 0, 3)
        slow_text("The match ended in 2-2 in the regular time.\n", 0, 3)
        slow_text("Now, penalties are needed to decide who will be the winner!\n", 0, 3)
        slow_text("The first team to take a penalty is:\n", 0, 3)
        
        print("\nChoose your favourite player: (please enter the number of the player)")
        print("1: \tLionel Messi")
        print("2: \tCristiano Ronaldo")
        print("3: \tRobert Lewandowski")
        print("4: \tGeorginio Wijnaldum")
        print("5: \tKevin de Bruyne")
        
        # Chosing team
        while True:
            team1 = input("> ")
            if team1 == "1":
                team1_name = "Barcelona"
                print("Your team is Barcelona!")
                break
            elif team1 == "2":
                team1_name = "Juventus"
                print("Your team is Juventus!")
                break
            elif team1 == "3":
                team1_name = "Bayern München"
                print("Your team is Bayern München!")
                break
            elif team1 == "4":
                team1_name = "Liverpool"
                print("Your team is Liverpool!")
                break
            elif team1 == "5":
                team1_name = "Manchester City"
                print("Your team is Manchester City!")
                break
            else:
                print("Please enter a valid number.")
        
        slow_text("\nAnd on the other side of the field we have:\n", 0, 1)
         
        print("\nChoose another player: (please enter the number of the player)")
        print("1: \tLionel Messi")
        print("2: \tCristiano Ronaldo")
        print("3: \tRobert Lewandowski")
        print("4: \tGeorginio Wijnaldum")
        print("5: \tKevin de Bruyne")
        
        # Chosing opponents team
        while True: 
            team2 = input("> ")
            if team2 != team1:
                if team2 == "1":
                    team2_name = "Barcelona"
                    print("The other team is Barcelona!")
                    break
                elif team2 == "2":
                    team2_name = "Juventus"
                    print("The other team is Juventus!")
                    break
                elif team2 == "3":
                    team2_name = "Bayern München"
                    print("The other team is Bayern München!")
                    break
                elif team2 == "4":
                    team2_name = "Liverpool"
                    print("The other team is Liverpool!")
                    break
                elif team2 == "5":
                    team2_name = "Manchester City"
                    print("The other team is Manchester City!")
                    break
                else:
                    print("Please enter a valid number.")
            elif team2 == team1:
                print("You have already chosen this team!\nPlease choose another team.")
        
        slow_text(f"\nSo, can {team1_name} handle the pressure better than {team2_name}?\n", 0, 3)
        print("-"*10)
        
        # Players need to answer questions correct to have a higher chance to score a penalty
        slow_text("Answer questions correct to have a higher chance to score a penalty.\n", 0, 3)
        slow_text("The first team to score 5 penalties is the winner!\n", 0, 3)
        slow_text("All answers are 'True' or 'False'.\n", 0, 3)
        
        while True:  
            if team1_scores or team2_scores == 5:
                return False
            else:
                # Question 1, true is correct
                question1 = "\nQuestion 1:\n\nCOVID-19 is an abbreviation for Corona Virus Disease 2019"
                question = question1
                question_outcome = "True"
                scores_question(team1_name, team2_name, question, question_outcome)
            
                # Question 2, false is correct
                question2 = "\nQuestion 2:\n\nM&M stands for Mars and Moordale"
                question = question2
                question_outcome = "False"
                scores_question(team1_name, team2_name, question, question_outcome)

                # Question 3, false is correct
                question3 = "\nQuestion 3:\n\nThere are two parts of the body that can't heal themselves"
                question = question3
                question_outcome = "False"
                scores_question(team1_name, team2_name, question, question_outcome)
                
                # Question 4, true
                question4 = "\nQuestion 4:\n\nBananas are curved because they grow upwards towards the sun"
                question = question4
                question_outcome = "True"
                scores_question(team1_name, team2_name, question, question_outcome)
                
                # Question 5, true
                question5 = "Question 5:\n\nIn the 'normal' Harry Potter story, there are 7 books and 8 movies\n"
                question = question5
                question_outcome = "True"
                scores_question(team1_name, team2_name, question, question_outcome)            
                if team1_scores or team2_scores == 5:
                    break
                
                # Question 6, true
                question6 = "\nQuestion 6:\n\nThe small intestine is about 7 meters long\n"
                question = question6
                question_outcome = "True"
                scores_question(team1_name, team2_name, question, question_outcome)
                if team1_scores or team2_scores == 5:
                    break
                
                # Question 7, false
                question7 = "\nQuestion 7:\n\nCoffee will dehydrate you\n"
                question = question7
                question_outcome = "False"
                scores_question(team1_name, team2_name, question, question_outcome)
                if team1_scores or team2_scores == 5:
                    break
                
                # Question 8, false
                question8 = "\nQuestion 8:\n\nSydney is the capital of Australia\n"
                question = question8
                question_outcome = "False"
                scores_question(team1_name, team2_name, question, question_outcome)
                if team1_scores or team2_scores == 5:
                    break
                
                # Question 9, true
                question9 = "\nQuestion 9:\n\nCarrots are good for your eyes\n"
                question = question9
                question_outcome = "True"
                scores_question(team1_name, team2_name, question, question_outcome)
                if team1_scores or team2_scores == 5:
                    break
                
                # Question 10, false
                question10 = "\nQuestion 10:\n\nLightning never strikes the same place twice\n"
                question = question10
                question_outcome = "False"
                scores_question(team1_name, team2_name, question, question_outcome)
                if team1_scores or team2_scores == 5:
                    break
                
                # Question 11, true
                question11 = "\nQuestion 11:\n\nPeople in Japan eat Kentucky Fried Chicken for Christmas dinner\n"
                question = question11
                question_outcome = "True"
                scores_question(team1_name, team2_name, question, question_outcome)
                if team1_scores or team2_scores == 5:
                    break
                
                # Question 12, true
                question12 = "\nQuestion 12:\n\nCows sleep standing up.\n"
                question = question12
                question_outcome = "True"
                scores_question(team1_name, team2_name, question, question_outcome)
                if team1_scores or team2_scores == 5:
                    break
                
                # Question 13, false
                question13 = "\nQuestion 13:\n\nAn octopus has four hearts\n"
                question = question13
                question_outcome = "False"
                scores_question(team1_name, team2_name, question, question_outcome)
                if team1_scores or team2_scores == 5:
                    break
                
                # Question 14, true
                question14 = "\nQuestion 14:\n\nVenus is the hottest planet in the solar system\n"
                question = question14
                question_outcome = "True"
                scores_question(team1_name, team2_name, question, question_outcome)
                if team1_scores or team2_scores == 5:
                    break
                
                # Question 15, true
                question15 = "\nQuestion 3:\n\nIf you did reach question 15, your general knowledge is lacking (no offense)\n"
                question = question15
                question_outcome = "True"
                scores_question(team1_name, team2_name, question, question_outcome)
                if team1_scores or team2_scores == 5:
                    break
                
        
class Main:

    def __init__(self):
        self.worlds = {
            #'World 1': MonsterFightWorld(), 
            'World 2': FootballFinal()
            # 'World 3': ,
            # 'World 4': 
        }
        self.completed = {f'World {i}': False for i in range(1, 5)}

    def all_worlds_completed(self):
        if False in self.completed.values():
            return False
        else:
            return True

    def main_menu(self):
        print("\n--------")
        print("Welcome (back) to the main menu.\n")
        print("Available worlds:")
        print("\tWorld 1: Defeat a tough monster!")
        print("\tWorld 2: Champions League final!\n")
        print("Type below the world you want to enter!")
        while True:
            world_choice = input("> ")
            if world_choice not in self.worlds.keys():
                print("Not a world.")
                continue
            else:
                slow_text(f"Entering {world_choice}.\n", 0, 2)
                print("--------")
                break
        return world_choice
    
    def play(self):
        while True:
            world = self.main_menu()
            current_world_completed = self.worlds.get(world).enter_world()
            if self.completed[world] is not True: #assures already completed world stays completed even if player restarts level and then loses the level
                self.completed[world] = current_world_completed
            if self.all_worlds_completed():
                slow_text("Congratulations, you beat all worlds! Game ends now.", 0, 3)
                break


if __name__ == "__main__":
    game = Main()
    game.play()        

