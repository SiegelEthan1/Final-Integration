# for my final integration project, I improved my game show
# makes all questions random
import random

# MC questions/answers
def get_MC_statements():
    statements = []
    statements.append(["What is the capital of Spain?\nA. Barcelona\nB. Lisbon\nC. Madrid \nD. Ronda", "C"])
    statements.append(["The name of a Sherlock Holmes villain:\nA. Rattigan\nB. Moriarty\nC. Mr. Hook\nD. Lupin", "B"])
    statements.append(["Christopher Columbus sailed the ocean blue, in... \nA. 1432\nB. 1855\nC. 2022\nD. 1492", "D"])
    statements.append(["Who Framed Roger Rabbit?\nA. Judge Doom\nB. Eddie Brock\nC. Jessica Rabbit\nD. No clue", "A"])
    statements.append(["What's 9+10?\nA. Twenty-one\nB. 21\nC. 19\n D. '20'", "C"])
    statements.append(["Answer here to get a point.\nA. [Answer]\nB. here\nC. Here\nD. Pick Me!", "B"])
    statements.append(["How many holes are in a shirt?\nA. 0\nB. 1\nC. 2\nD. 4", "D"])
    statements.append(["Name a Russian Queen:\nA. Catherine\nB. Cleopatra\nC. Elizabeth\nD. Freddie", "A"])
    statements.append(["What is love?\nA. BABY DON'T HURT ME!\nB. EVOL spelled backwards\nC. A&B\nD. NotA", "C"])
    statements.append(["Who's the greatest teacher in COP?\nA. Osherott\nB. Somebody else\nC. Batman\nD. Ethan", "A"])
    return statements


def play_MC_game():
    # get true or false statements
    MC_statements = get_MC_statements()

    # Randomize tof statements
    random.shuffle(MC_statements)

    # set player score to 0
    MC_score = int(0)
    # Show tof statements using a loop
    for s in MC_statements:
        pass
        while True:
            print("Question: " + s[0])

            # user enters guess
            guess = input("Enter A, B, C, or D: ")
            # if guess is not capitalized, the program capitalizes it
            guess = guess.capitalize()
            # check if guess is correct
            if guess == s[1]:
                print("Good job! That was correct!")
                # update score
                MC_score = MC_score + 1
                break
            # user enters invalid answer
            elif guess not in ["A", "B", "C", "D"]:
                print("I'm sorry, I don't understand that answer!")
                # continue
            else:
                print("Sorry! That was wrong!")
                break

    # present statement
    # show final score
    print("Congratulations! You scored a total of " + str(MC_score) + " points.")
    # user scores 10
    if MC_score == 10:
        print("You looked at your phone, didn't you?")
    # user scores between 9 and 7
    elif MC_score <= 9 and MC_score >= 7:
        print("Hey! You did pretty good!")
    # user scores 6 or 5
    elif MC_score <= 6 and MC_score >= 5:
        print("Not a bad score, but not a good one either...")
    # user scores between 4 and 2
    elif MC_score <= 4 and MC_score >= 2:
        print("Looks like someone needs to study a bit more!")
    # user scores 0
    else:
        print("Okay, boomer")
    return

# Tof questions/answers
def get_Tof_statements():
    statements = []
    statements.append(["Ladybugs can only be red with black spots", "F"])
    statements.append(["Leonardo Dicaprio won his first Oscar for best actor in 2016", "T"])
    statements.append(["a hyena's 'laughter' is a form of communication used to convey frustration or fear", "T"])
    statements.append(["The Konami Code is activated when the player inputs '↓ ↘ → + B'", "F"])
    statements.append(["The Beatles debut album 'Please Please Me' was released on August 5, 1966", "F"])
    statements.append(["Jason Voorhees did not make an appearance until the second 'Friday the 13th' movie", "T"])
    statements.append(["The arcade game 'Donkey Kong' was originally planned to be a 'Popeye' game", "T"])
    statements.append(["Nobody expects the Spanish Inquisition!", "T"])
    statements.append(["In Marvel Comics, the superhero Thor's alter ego was originally Donald Blake", "T"])
    statements.append(["The Teenage Mutant Ninja Turtles did not have a live musical tour in 1990.", "F"])

    return statements


def play_Tof_game():
    # get true or false statements
    tof_Statements = get_Tof_statements()

    # Randomize tof statements
    random.shuffle(tof_Statements)

    # set player score to 0
    ToF_score = int(0)
    open("QuizScore.txt", 'a')
    # Show tof statements using a loop
    for s in tof_Statements:
        # present statement
        while True:
            print("True or False: " + s[0])

            # user enters guess
            # find function that uppercase guess
            guess = input("Enter T or F: ")
            # if guess is not capitalized, the program capitalizes it
            guess = guess.capitalize()
            # check if guess is correct

            if guess == s[1]:
                print("Good job! That was correct!")
                # update score
                ToF_score = ToF_score + 1
                break
            # user enters invalid answer
            elif guess not in ["T", "F"]:
                print("I'm sorry, I don't understand that answer!")
                # continue
            else:
                print("Sorry! That was wrong!")
                break
    # show final score
    print("Congratulations! You scored a total of " + str(ToF_score) + " points.")
    if ToF_score == 10:
        print("You looked at your phone, didn't you?")
    elif ToF_score <= 9 and ToF_score >= 7:
        print("Hey! You did pretty good!")
    elif ToF_score <= 6 and ToF_score >= 5:
        print("Not a bad score, but not a good one either...")
    elif ToF_score <= 4 and ToF_score >= 2:
        print("Looks like someone needs to study a bit more!")
    else:
        print("Okay, boomer")
    # return to main menu
    return


def No_choice():
    print("Sorry, I don't understand that.\nPlease try again!")
    return


def mainMenu():
    user_continue = True
    while user_continue:
        print("+------------------------------+")
        print("|Welcome to Ethan's game show! |")
        print("|Please select an option:      |")
        print("|1. Play True or False         |")
        print("|2. Play Multiple Choice       |")
        print("|0. Quit                       |")
        print("+------------------------------+")
        # player chooses to play or quit
        choice = input("Enter here: ")
        if choice == "1":
            play_Tof_game()
        elif choice == "2":
            play_MC_game()
        elif choice == "0":
            print("Thanks for playing!")
            user_continue = False
        # What if user enters "3"?
        else:
            No_choice()


mainMenu()
