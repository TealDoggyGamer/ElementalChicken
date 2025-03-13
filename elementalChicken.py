#importing modules
import random
import math
import time


#card that prints for fire chicken
def fire_chicken():
    print("______________________________________")
    print("|       ,~.                          |")
    print("|    ,-'__ `-,                       |")
    print("|   {,-'  `. }                ,')    |")
    print("|   ,( O )   `-.__           ,',')~, |")
    print("|  <=.) (         `-.__,==' ' ' '}   |")
    print("|    (   )                      /    |")
    print("|     `-'\   ,                  )    |")
    print("|        |  \        `~.      /      |")
    print("|        \   `._        \    /       |")
    print("|          \     `._____,'   /       |")
    print("|           `-.            ,'        |")
    print("|              `-.      ,-'          |")
    print("|                 `~~~~'             |")
    print("|                 //_||              |")
    print("|             __//--'/`              |")        
    print("|           ,--'/`  '                |")
    print("|             FIRE CHICKEN -1        |")      
    print("|____________________________________|")


#card that prints for water chicken
def water_chicken():
    print("______________________________________")
    print("|       ,~.                          |")
    print("|    ,-'__ `-,                       |")
    print("|   {,-'  `. }                ,')    |")
    print("|   ,( O )   `-.__           ,',')~, |")
    print("|  <=.) (         `-.__,==' ' ' '}   |")
    print("|    (   )                      /    |")
    print("|     `-'\   ,                  )    |")
    print("|        |  \        `~.      /      |")
    print("|        \   `._        \    /       |")
    print("|          \     `._____,'   /       |")
    print("|           `-.            ,'        |")
    print("|              `-.      ,-'          |")
    print("|                 `~~~~'             |")
    print("|                 //_||              |")
    print("|             __//--'/`              |")        
    print("|           ,--'/`  '                |")
    print("|            WATER CHICKEN +1        |")      
    print("|____________________________________|")


#card that prints for air chicken
def air_chicken():
    print("______________________________________")
    print("|       ,~.                          |")
    print("|    ,-'__ `-,                       |")
    print("|   {,-'  `. }                ,')    |")
    print("|   ,( O )   `-.__           ,',')~, |")
    print("|  <=.) (         `-.__,==' ' ' '}   |")
    print("|    (   )                      /    |")
    print("|     `-'\   ,                  )    |")
    print("|        |  \        `~.      /      |")
    print("|        \   `._        \    /       |")
    print("|          \     `._____,'   /       |")
    print("|           `-.            ,'        |")
    print("|              `-.      ,-'          |")
    print("|                 `~~~~'             |")
    print("|                 //_||              |")
    print("|             __//--'/`              |")        
    print("|           ,--'/`  '                |")
    print("|             AIR CHICKEN +2         |")      
    print("|____________________________________|")


#card that prints for earth chicken
def earth_chicken():
    print("______________________________________")
    print("|       ,~.                          |")
    print("|    ,-'__ `-,                       |")
    print("|   {,-'  `. }                ,')    |")
    print("|   ,( O )   `-.__           ,',')~, |")
    print("|  <=.) (         `-.__,==' ' ' '}   |")
    print("|    (   )                      /    |")
    print("|     `-'\   ,                  )    |")
    print("|        |  \        `~.      /      |")
    print("|        \   `._        \    /       |")
    print("|          \     `._____,'   /       |")
    print("|           `-.            ,'        |")
    print("|              `-.      ,-'          |")
    print("|                 `~~~~'             |")
    print("|                 //_||              |")
    print("|             __//--'/`              |")        
    print("|           ,--'/`  '                |")
    print("|             EARTH CHICKEN -2       |")      
    print("|____________________________________|")


#card that prints for lightning chicken
def lightning_chicken():
    print("______________________________________")
    print("|       ,~.                          |")
    print("|    ,-'__ `-,                       |")
    print("|   {,-'  `. }                ,')    |")
    print("|   ,( O )   `-.__           ,',')~, |")
    print("|  <=.) (         `-.__,==' ' ' '}   |")
    print("|    (   )                      /    |")
    print("|     `-'\   ,                  )    |")
    print("|        |  \        `~.      /      |")
    print("|        \   `._        \    /       |")
    print("|          \     `._____,'   /       |")
    print("|           `-.            ,'        |")
    print("|              `-.      ,-'          |")
    print("|                 `~~~~'             |")
    print("|                 //_||              |")
    print("|             __//--'/`              |")        
    print("|           ,--'/`  '                |")
    print("|         LIGHTNING CHICKEN +4       |")      
    print("|____________________________________|")


#card that prints for dark chicken
def dark_chicken():
    print("______________________________________")
    print("|       ,~.                          |")
    print("|    ,-'__ `-,                       |")
    print("|   {,-'  `. }                ,')    |")
    print("|   ,( O )   `-.__           ,',')~, |")
    print("|  <=.) (         `-.__,==' ' ' '}   |")
    print("|    (   )                      /    |")
    print("|     `-'\   ,                  )    |")
    print("|        |  \        `~.      /      |")
    print("|        \   `._        \    /       |")
    print("|          \     `._____,'   /       |")
    print("|           `-.            ,'        |")
    print("|              `-.      ,-'          |")
    print("|                 `~~~~'             |")
    print("|                 //_||              |")
    print("|             __//--'/`              |")        
    print("|           ,--'/`  '                |")
    print("|             DARK CHICKEN -3        |")      
    print("|____________________________________|")


#card that prints if you draw light chicken
def light_chicken():
    print("______________________________________")
    print("|       ,~.                          |")
    print("|    ,-'__ `-,                       |")
    print("|   {,-'  `. }                ,')    |")
    print("|   ,( O )   `-.__           ,',')~, |")
    print("|  <=.) (         `-.__,==' ' ' '}   |")
    print("|    (   )                      /    |")
    print("|     `-'\   ,                  )    |")
    print("|        |  \        `~.      /      |")
    print("|        \   `._        \    /       |")
    print("|          \     `._____,'   /       |")
    print("|           `-.            ,'        |")
    print("|              `-.      ,-'          |")
    print("|                 `~~~~'             |")
    print("|                 //_||              |")
    print("|             __//--'/`              |")        
    print("|           ,--'/`  '                |")
    print("|            LIGHT CHICKEN +3        |")      
    print("|____________________________________|")


#get the card and power of the card
def drawCard():
    #get the index for the lists
    cardNumber = random.randint(0, 6)
    #find the card with that index
    card = cardList[cardNumber]
    #find the power with that index
    power = powerList[cardNumber]
    #return card and power
    return card, power


#greet the player
def greeting():
    #looks like birds?
    print(" \\              =o)")
    print(" (o>             /\\ ")
    print("_(()_Elemental _\_V_")
    print(" //       Chicken \\")
    print("                   \\")
   
    time.sleep(1)
    global player1
    #get p1 name
    player1 = input("Welcome Player 1! Pretty please with a cherry on top enter your name!: ")
    #greet the player
    print("Welcome aboard the chicken", player1)
    time.sleep(1)
    global player2
    #get p2 name
    player2 = input("Welcome Player 2! Pretty please with a cherry on top and extra hot fudge enter your name!: ")
    #greet p2
    print("Good to have you here", player2)
    time.sleep(1)
    print("Welcome all to Elemental Chicken! In this journey you will experience love, hatred, rage, agony, anger, revenge, power, glory, triumph, Chicken! ")
    clicker()


#determine which of the players is the winner
def decideWinner():
    #p1 wins
    if totalPower1 > totalPower2:
        global roundWin
        roundWin = "p1win"
    #p2 wins
    elif totalPower2 > totalPower1:
        roundWin = "p2win"
    #tie
    else:
        print("Tie next round.")


#wait for input before continuing game
def clicker():
    print("Press enter to continue...")
    #once it get input it continues
    input()


#end statement if p1 wins
def GoodbyeGood():
    print("Well.... As most stories go, good beats evil, the chicken gets the grain, the sun always shines in the morning.\nThe battle was tireless, strenuous, and exhausting.\nAhem- anyways,", player1, "came out victorious! Your feathers may have been ruffled, and your tail trampled but you did it!\nYou overcame- you completely winged it too! Congratulations, young poultry... you've done well.")


#end statement if p2 wins
def GoodbyeBad():
    print("Well... this was certainly a surprise... you,", player2, ", won. Evil prevailed, good; demolished... the sun doesn't shine in the morning.\nThe battle was certainly tireless and strenuous and exhausting but you did it.\nEvery chicken in the coop now fears you, every grain now for your taking.\nYou spend the rest of your days terrorizing young chicks, enjoying the squaks of pure terror as they waddle away.\nThings are going good for you...\nbut you can't help but think of what could have been, what the world would be like if you had lost.")


#give credits to the players
def Credits():
    print("Thank you for playing our silly game, Elemental Chicken. We'd like to thank all of the wonderful people who worked on this!\nThank you to Niwesa, Daryn, Leah, and of course, Cora!")


#run the game
def elementalChicken():
    #player 1 turn start
    global totalPower1
    p1card1, p1power1 = drawCard()
    hand1 = [p1power1]
    totalPower1 = sum(hand1)
    #totalPower1 = p1power1
    #tell the player their deck
    print("Player one, your deck is: ")
    #determine what the first card that player 1 has and then print it
    #if fire chicken is drawn
    if p1card1 == "fire":
        fire_chicken()
    #if water chicken is drawn
    elif p1card1 == "water":
        water_chicken()
    #if air chicken is drawn
    elif p1card1 == "air":
        air_chicken()
    #if earth chicken is drawn
    elif p1card1 == "earth":
        earth_chicken()
    #if lightning chicken is drawn
    elif p1card1 == "lightning":
        lightning_chicken()
    #if dark chicken is drawn
    elif p1card1 == "dark":
        dark_chicken()
    #if light chicken is drawn
    elif p1card1 == "light":
        light_chicken()




    #tell player1 their total power than ask if they want another card
    print("Your total power is", totalPower1, ", do you want to add another card to your hand? yes or no: ")
    #set the input as a variable
    choose = input()
    #p1 wants another card
    if choose == "yes":
        #draw card
        p1card2, p1power2 = drawCard()
        #totalPower1 = totalPower1 + p1power2
        hand1.append(p1power2)
        #add hand together
        totalPower1 = sum(hand1)
        #determine what the second card that player 1 has is and then print it
        #if fire chicken is drawn
        if p1card2 == "fire":
            fire_chicken()
        #if water chicken is drawn
        elif p1card2 == "water":
            water_chicken()
        #if air chicken is drawn
        elif p1card2 == "air":
            air_chicken()
        #if earth chicken is drawn
        elif p1card2 == "earth":
            earth_chicken()
        #if lightning chicken is drawn
        elif p1card2 == "lightning":
            lightning_chicken()
        #if dark chicken is drawn
        elif p1card2 == "dark":
            dark_chicken()
        #if light chicken is drawn
        elif p1card2 == "light":
            light_chicken()
            
        #tell player total power than ask if they want another card
        print("Your total power is", totalPower1, ", do you want to add another card to your hand? yes or no: ")
        #set their input as a variable
        choose = input()
        #if they want another card
        if choose == "yes":
            #draw another card
            p1card3, p1power3 = drawCard()
            #totalPower1 = totalPower1 + p1power3
            hand1.append(p1power3)
            #add hand together
            totalPower1 = sum(hand1)
            #determine what the third card that player 1 has is and then print it
            #if fire chicken is drawn
            if p1card3 == "fire":
                fire_chicken() 
            #if water chicken is drawn
            elif p1card3 == "water":
                water_chicken()
            #if air chicken is drawn
            elif p1card3 == "air":
                air_chicken()
            #if earth chicken is drawn
            elif p1card3 == "earth":
                earth_chicken()
            #if lightning chicken is drawn
            elif p1card3 == "lightning":
                lightning_chicken()
            #if dark chicken is drawn
            elif p1card3 == "dark":
                dark_chicken()
            #if light chicken is drawn
            elif p1card3 == "light":
                light_chicken()
        #tell player one the power of their hand
        totalPower1 = sum(hand1)
    print(player1, "the total power of your hand is:", totalPower1)
    clicker()


    #player 2 turn start
    global totalPower2
    #draw the card
    p2card1, p2power1 = drawCard()
    #add the power value to the list
    hand2 = [p2power1]
    #add the list together
    totalPower2 = sum(hand2)
    print("Player two, your deck is: ")
    #determine what the first card that player 2 has is then print it
    #if fire chicken is drawn
    if p2card1 == "fire":
        fire_chicken()
    #if water chicken is drawn
    elif p2card1 == "water":
        water_chicken()
    #if air chicken is drawn
    elif p2card1 == "air":
        air_chicken()
    #if earth chicken is drawn
    elif p2card1 == "earth":
        earth_chicken()
    #if lightning chicken is drawn
    elif p2card1 == "lightning":
        lightning_chicken()
    #if dark chicken is drawn
    elif p2card1 == "dark":
        dark_chicken()
    #if light chicken is drawn
    elif p2card1 == "light":
        light_chicken()
    #tell p2 total power than ask if they want another card in their hand
    print("Your total power is", totalPower2, ", do you want to add another card to your hand? yes or no: ")
    #set the input as a variable
    choose = input()
    #if they want another card
    if choose == "yes":
        #draw the card
        p2card2, p2power2 = drawCard()
        #add the card to the hand
        hand2.append(p2power2)
        #add the hand together
        totalPower2 = sum(hand2)
        #determine what the second card that player 2 has is then print it
        #if fire chicken
        if p2card2 == "fire":
            fire_chicken()
        #if water chicken is drawn
        elif p2card2 == "water":
            water_chicken()
        #if air chicken is drawn
        elif p2card2 == "air":
            air_chicken()
        #if earth chicken is drawn
        elif p2card2 == "earth":
            earth_chicken()
        #if lightning chicken is drawn
        elif p2card2 == "lightning":
            lightning_chicken()
        #if dark chicken is drawn
        elif p2card2 == "dark":
            dark_chicken()
        #if light chicken is drawn
        elif p2card2 == "light":
            light_chicken()
        #tell them their power and ask if they want to draw a card again
        print("Your total power is", totalPower2, ", do you want to add another card to your hand? yes or no: ")
        #set the input as a variable
        choose = input()
        #if they want another card
        if choose == "yes":
            #draw the card
            p2card3, p2power3 = drawCard()
            #add the card to their hand
            hand2.append(p2power3)
            #add the hand together
            totalPower2 = sum(hand2)
            # determine what the third card that player 2 has then print it
            #if fire chicken is drawn
            if p2card3 == "fire":
                fire_chicken()
            #if water chicken is drawn
            elif p2card3 == "water":
                water_chicken()
            #if air chicken is drawn
            elif p2card3 == "air":
                air_chicken()
            #if earth chicken is drawn
            elif p2card3 == "earth":
                earth_chicken()
            #if lightning chicken is drawn
            elif p2card3 == "lightning":
                lightning_chicken()
            #if dark chicken is drawn
            elif p2card3 == "dark":
                dark_chicken()
            #if light chicken is drawn
            elif p2card3 == "light":
                light_chicken()
    #tell player two the power of their hand
    print(player2, "the total power of your hand is:", totalPower2)
    clicker()
   
    decideWinner()
    #determine which end statment to print
    #p1 wins
    if roundWin == "p1win":
        #print the message that good has prevailed
        GoodbyeGood()
        global totalWins1
        #set player1 total wins to one higher
        totalWins1 += 1
    #p2 wins
    elif roundWin == "p2win":
        #print the message that bad won
        GoodbyeBad()
        global totalWins2
        #set p2 total wins one higher
        totalWins2 += 1
    clicker()
    


#lists to store values
powerList = [-1, 1, 2, -2, 4, -3, 3]
#different elements
cardList = ["fire", "water", "air", "earth", "lightning", "dark", "light"]
#initializing variables
roundWin = ""
p1power1 = p1power2 = p1power3 = p2power1 = p2power2 = p2power3 = 0
p1card1 = p1card2 = p1card3 = p2card1 = p2card2 = p2card3 = ""
hand1 =[]
totalPower1 = 0
hand2 = []
totalPower2 = 0
playAgain = "yes"
totalWins1 = 0
totalWins2 = 0

#greet the player
greeting()
while playAgain != "no":
    #run the game
    elementalChicken()
    #tell the players how many times they have won
    print(player1, "has won", totalWins1, "rounds.")
    print(player2, "has won", totalWins2, "rounds.")
    #see if they want to play again
    playAgain = input("Do you want to play again to even the score? yes or no: ")


#print the end credits
Credits()
