def new_game():
    correct_guesses = 0
    question_num =0
    print("------------------------------------------------------------------------\n")
    print("                 ARE YOU EVIL ENOUGH TO HANG WITH ME                    ")
    print("                  TAKE MY QUIZ AND LET US FIND OUT!                     ")
    print("\n------------------------------------------------------------------------")

    # print all of questions
    for key in questions:
        print("\n------------------------------------------------------------------------")
        print(key)

        # print all of options
        for i in options[question_num]:
            print(i)
        
        # get the answer from player
        print("")
        guess = input("Enter (A or B): ")
        guess = guess.upper()

        # create index for the answer 
        if (guess == "A"):
            indexOf_response = 0
        else:
            indexOf_response = 1

        # print response for every answer
        for response in giveـresponse[question_num]:
            response= giveـresponse[question_num][indexOf_response]
            pass

        # (increase score or not) depends on player answers
        correct_guesses += check_answer(questions.get(key), guess, response)
        question_num += 1

    display_evil(correct_guesses)

# -----------------------------------------

def check_answer(answer, guess, response):
    if (answer== guess) :
        print("")
        print(response)
        return 1
    else:
        print("")
        print(response)
        return 0

# -----------------------------------------
def display_evil(correct_guesses):
    score = int(correct_guesses)
    if correct_guesses >= 8:
        print("\n-----------------------------------------------------")
        print("                 YOU ARE SUPER EVIL!                 ")
        print("                       BWAHAHAHA                     ")
        print("-----------------------------------------------------")
        print("       EXCELLENT! YOU ARE ALMOST AS EVIL AS ME.      ")
        print("                AND THAT'S PRETTY EVIL!              ")
        print(" WE SHOULD HANG OUT AND TAKE OVER THE WORLD TOGETHER.")
        print("-----------------------------------------------------\n")
        print("******************* Done By Team 2 *******************\n")


    elif correct_guesses >=5:
        print("\n-----------------------------------------------------------------------------------")
        print("                                YOU ARE A BIT EVIL!                                ")
        print("                    WELL, IT'S BETTER THAN NOT BEING EVIL AT ALL.                  ")
        print("-----------------------------------------------------------------------------------")
        print(" START GETTING YOUR PHONE OUT AT MOVIES AND STEALING FRIES FROM YOUR FRIEND'S PLATE")
        print("                             AND THEN WE'LL BE TALKING!                            ")
        print("-----------------------------------------------------------------------------------\n")
        print("********************************** Done By Team 2 *********************************\n")

    else:
        print("\n-------------------------------------")
        print("          I DIDN'T LIKE YOU          ")
        print("      YOU ARE  NOT EVIL AT ALL!      ")
        print("-------------------------------------\n")
        print("********** Done By Team 2 ***********\n")

# play again
def play_again():
    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()
    if response == "YES":
        return True
    else:
        return False


# List Of Questions with the evil answer
questions = {
    "1- YOU ARE ALLOWED TO HAVE ONE COOKIE. HOW MANY DO YOU REALLY TAKE?" : "A" , 
    "2- YOU'VE BEEN TOLD IT'S TIME FOR BED! ARE YOU GOING TO SLEEP OR SECRETLY STAY UP?" : "B" , 
    "3- SOMEONE IS TRYING TO NAP. WHAT DO YOU DO?" : "A" , 
    "4- DO YOU WANT TO HAVE DESSERT BEFORE DINNER?" : "B" , 
    "5- YOUR FRIEND HAS LOADS OF FRENCH FRIES. WILL YOU SECRETLY TAKE ONE?" : "B" , 
    "6- YOU'VE SEEN A NEW SHOW BEFORE A FRIEND. DO YOU SPOIL THE ENDING?": "A",
    "7- YOU HAVE TO CLEAN YOUR ROOM. WILL YOU DO IT RIGHT OR DUMP EVERYTHING IN THE CLOSET?": "A", 
    "8- YOU'RE AT THE MOVIES! ARE YOU GOING TO STAY QUIET?" : "B", 
    "9- DO YOU START GETTING ON THE BUS BEFORE OTHER PEOPLE GET OFF?": "A",
    "10- THERE IS ONLY ONE SLICE OF PIZZA LEFT. DO YOU ASK IF ANYONE ELSE WANTS IT?" : "A" , 
    "11- YOU HAVE ALL THE SNACKS! WILL YOU SHARE THEM?" : "A" 
}

# List of Answers Options
options = [
    ["  A. ALL OF THEM!", "  B. JUST ONE, BECAUSE I MIGHT GET MORE LATER!"],
    ["  A. I NEED MY BEAUTY SLEEP ", "  B. STAY UP ALL NIGHT LONG "],
    ["  A. I'LL SING THEM THE SONG OF MY PEOPLE!", "  B. I'D BRING THEM MY MOST MEGA COMFY BLANKET. "],
    ["  A. NEVER! ", "  B. DOESN'T EVERYONE?"],
    ["  A. NO WAY, THEY'RE NOT MY FRIES. ", "  B. ALL FRENCH FRIES BELONG TO ME NOW! "],
    ["  A. I'LL SPOIL ALL OF IT. ", "  B.  I WOULD NEVER!THAT'S LITERALLY THE WORST!"],
    ["  A. CLOSET ALL THE WAY! ", "  B. I'D DO IT RIGHT, AND EVEN OFFER TO VACUUM THE HOUSE."],
    ["  A. YES, AND I'LL SHUSH PEOPLE WHO AREN'T. ", "  B.  I'M ALREADY SHOUTING AT THE SCREEN."],
    ["  A. I DON'T EVEN LET THEM GET OFF.THEY LIVE ON THE BUS NOW. ", "  B. I COULD NEVER DO THAT! THAT'S SO RUDE!"],
    ["  A. NO WAY, IT'S ALL MINE.", "  B. OF COURSE I WOULD!I'D EVEN SEE IF WE COULD SHARE IT."],
    ["  A. NO WAY! ALL FOR ME.", "  B. YES, I LOVE SHARING. "]
]

# giving me response for every answer
giveـresponse=[
    ["** YES!\nALL FOR YOU,\nNONE FOR THEM! **","REALLY! HRMM"],
    ["YEAH YOU DO","** YES, AND MAKE PLANS FOR WORLD DOMINATION! **"],
    ["** MWAHAHAHAHA YES! **","OH. GOOD. I GUESS"],
    [ "REALLY? EVEN IF IT'S ICE CREAM?", "** I HAVE DESSERT FOR.. \nEVERY MEAL! **"],
    ["BUT THEY COULD BE YOURS!", "** WOAM YOU'RE GOOD ,AT BEING EVIL. **"],
    ["** YES!\nSPOIL EVERYTHING! **","THAT'S THE POINT!"],
    ["** YES!\nUNDER THE BED TOO! **","EW. HOW RESPONSIBLE."],
    ["WELL. FINE.", "** YES! LOUDER! MORE EVIL! **"],
    ["** HAMA BRILLIANT! SO. EVIL. **", "WELL YES. OBVIOUSLY"],
    ["** EXCELLENT.\nTHE PIZZA IS YOURS! **", "WHY BOTHER"],
    ["** HAHA YES!\nCHAOS! **", "I SEE. HOW NICE."]
]

# Start new game
new_game()
while play_again():
    new_game()


print("\n----------------------------------------------------------------")
print("       Byeeeeee! ,So Excited To See U In Another Games<3        ")
print("----------------------------------------------------------------\n")




