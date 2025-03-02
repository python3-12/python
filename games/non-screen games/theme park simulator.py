import random
import time
def randomizer(max_value):
  return random.randint(-2, max_value)
random_number = randomizer(500)
while True:
    wonder= input("do you want to go to six flags, universal, or disney").lower()
    if wonder =="six flags":
            f= input('wich ride do you want to do,eltoro,the joker, teacups, medusa, or\nking da ka').lower()
            if f == 'eltoro':
                time.sleep(5)
                print("finaly were at the ride!")
                print("bucle up!")
                print("wait you start with the big drop?!??!!?!\nah!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n now another, what are these turns!!! ah!!!!!!!!")
            elif f == "the joker":
                print("ooh this looks scary, I wonder how scary it actuly is")
                time.sleep(8)
                print("that was a while now we get to go on!!") 
                print("were going up!ah were fliping")
                print("the squigly line is us")
                print(" ______________________________~_______________/|")
                print("/                                               |")
                print("|____________________________________________   |")
                print("_____________________________________________|  |")
                print("|                                               |")
                print(" |                                              |")
                print("  |                                             |")
                print("   |____________________________________________/")
            elif f == "teacups":
                print("that's boring so no")
            elif f == "king da ka":
                time.sleep(15)
                print("up we go ah!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            elif f == "medusa":
                time.sleep(7)
                print("this is crazy")
            else:
                input("thats not a option try again")
                        
    elif wonder == "universal":
        j= input("do you want to do the hulk,spider man,or the drop of doom?").lower()
        if j == 'the hulk':
            print("after that, I think we should play a game")
            time.sleep(14)
            print("raw!!!!!!")
            print("ah!!!whats happening?!???!!")
            time.sleep(4)
            print("we could get Mario!!!")
            print("depending on the number, we get something")
            print("your turn")
            p= print(random_number)
            if random_number < (501) and random_number > (399):
                print("extra large")
            elif random_number < (400) and random_number > (299):
                print("large")
            elif random_number < (300) and random_number > (198):
                    print("medium")
            elif random_number < (198) and random_number > (96):
                    print("small")
            elif random_number < (97) and random_number > (-3):
                print("extra small")
        elif j == 'the drop of doom':
             time.sleep(3)
             print("up we go!")
             time.sleep(0.8)
             print("uh oh.")
             time.sleep(1)
             print("ah!")
        elif j == 'spider man':
             time.sleep(4)
             print("were starting")
             print("'why are you here, this could be the most dangerous time of your life', said spider man\n and mine")
             print("'trick or treat, smell my feet, time to blow you off the street, nya ha haha', said hob goblin")
             time.sleep(1)
             print("'spider man!', hob goblin said")
             print('bwoom went the bomb')
             time.sleep(1)
             print("'time for you to face my levetation ray', said doctor octupus")
             print("'what comes up must come down, nye ha ha'")
             print("'no you don't', said spider man")
             print("he shoots a web to save you, 'you did it', said spider man")
        else:
             input("that isn't a option try again")
    elif wonder == 'disney':
         i = input("do you want to do twilight zone tower of terror, gardians of the galaxy: cosmic rewind, or expedition everest")
         if i == 'twilight zone tower of terror':
              print("up we go, down we go, side we go, down we ahh!!")
         elif i == 'gardians of the galaxy: cosmic rewind':
              print("ahh! its the bad guy!")
              print("yes! we got the thing!")
         elif i == 'expidition everest':
              print("the yeti got us!")
              print("were going backward!")
              print("down we ahh!!")
         else:
              input('thats not a option try again')
    else:
        input("thats not a option try again")
