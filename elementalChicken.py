import random
import math
import time

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


def drawCard():
    cardNumber = random.randint(0, 6)
    card = cardList[cardNumber]
    power = powerList[cardNumber]
    return card, power


def greeting():
    print(" \\              =o)")
    print(" (o>             /\\ ")
    print("_(()_Elemental _\_V_")
    print(" //       Chicken \\")
    print("                   \\")
   
    time.sleep(1)
    global player1
    player1 = input("Welcome Player 1! Pretty please with a cherry on top enter your name!: ")
    print("Welcome aboard the chicken", player1)
    time.sleep(1)
    global player2
    player2 = input("Welcome Player 2! Pretty please with a cherry on top and extra hot fudge enter your name!: ")
    print("Good to have you here", player2)
    time.sleep(1)
    print("Welcome all to Elemental Chicken! In this journey you will experience love, hatred, rage, agony, anger, revenge, power, glory, triumph, Chicken! ")
    clicker()

def decideWinner():
    if totalPower1 > totalPower2:
        global roundWin
        roundWin = "p1win"
    elif totalPower2 > totalPower1: 
        roundWin = "p2win"
    else:
        print("Tie next round.")


def clicker():
    print("Press enter to continue...")
    input()


def GoodbyeGood():
    print("Well.... As most stories go, good beats evil, the chicken gets the grain, the sun always shines in the morning.\nThe battle was tireless, strenuous, and exhausting.\nAhem- anyways,", player1, "came out victorious! Your feathers may have been ruffled, and your tail trampled but you did it!\nYou overcame- you completely winged it too! Congratulations, young poultry... you've done well.")


def GoodbyeBad():
    print("Well... this was certainly a surprise... you,", player2, ", won. Evil prevailed, good; demolished... the sun doesn't shine in the morning.\nThe battle was certainly tireless and strenuous and exhausting but you did it.\nEvery chicken in the coop now fears you, every grain now for your taking.\nYou spend the rest of your days terrorizing young chicks, enjoying the squaks of pure terror as they waddle away.\nThings are going good for you...\nbut you can't help but think of what could have been, what the world would be like if you had lost.")


def Credits():
    print("Thank you for playing our silly game, Elemental Chicken. We'd like to thank all of the wonderful people who worked on this!\nThank you to Niwesa, Daryn, Leah, and of course, Cora!")


def elementalChicken():
    greeting()
    print("Player one, your deck is: ")
    if p1card1 == "fire":
        fire_chicken()
        clicker()
    elif p1card1 == "water":
        water_chicken()
        clicker()
    elif p1card1 == "air":
        air_chicken()
        clicker()
    elif p1card1 == "earth":
        earth_chicken()
        clicker()
    elif p1card1 == "lightning":
        lightning_chicken()
        clicker()
    elif p1card1 == "dark":
        dark_chicken()
        clicker()
    elif p1card1 == "light":
        light_chicken()
        clicker()




    if p1card2 == "fire":
        fire_chicken()
        clicker()
    elif p1card2 == "water":
        water_chicken()
        clicker()
    elif p1card2 == "air":
        air_chicken()
        clicker()
    elif p1card2 == "earth":
        earth_chicken()
        clicker()
    elif p1card2 == "lightning":
        lightning_chicken()
        clicker()
    elif p1card2 == "dark":
        dark_chicken()
        clicker()
    elif p1card2 == "light":
        light_chicken()
        clicker()




    if p1card3 == "fire":
        fire_chicken()
        clicker()
    elif p1card3 == "water":
        water_chicken()
        clicker()
    elif p1card3 == "air":
        air_chicken()
        clicker()
    elif p1card3 == "earth":
        earth_chicken()
        clicker()
    elif p1card3 == "lightning":
        lightning_chicken()
        clicker()
    elif p1card3 == "dark":
        dark_chicken()
        clicker()
    elif p1card3 == "light":
        light_chicken()
        clicker()
    print(player1, "the total power of your hand is:", totalPower1)
    clicker()


    print("Player two, your deck is: ")
    if p2card1 == "fire":
        fire_chicken()
        clicker()
    elif p2card1 == "water":
        water_chicken()
        clicker()
    elif p2card1 == "air":
        air_chicken()
        clicker()
    elif p2card1 == "earth":
        earth_chicken()
        clicker()
    elif p2card1 == "lightning":
        lightning_chicken()
        clicker()
    elif p2card1 == "dark":
        dark_chicken()
        clicker()
    elif p2card1 == "light":
        light_chicken()
        clicker()


    if p2card2 == "fire":
        fire_chicken()
        clicker()
    elif p2card2 == "water":
        water_chicken()
        clicker()
    elif p2card2 == "air":
        air_chicken()
        clicker()
    elif p2card2 == "earth":
        earth_chicken()
        clicker()
    elif p2card2 == "lightning":
        lightning_chicken()
        clicker()
    elif p2card2 == "dark":
        dark_chicken()
        clicker()
    elif p2card2 == "light":
        light_chicken()
        clicker()


    if p2card3 == "fire":
        fire_chicken()
        clicker()
    elif p2card3 == "water":
        water_chicken()
        clicker()
    elif p2card3 == "air":
        air_chicken()
        clicker()
    elif p2card3 == "earth":
        earth_chicken()
        clicker()
    elif p2card3 == "lightning":
        lightning_chicken()
        clicker()
    elif p2card3 == "dark":
        dark_chicken()
        clicker()
    elif p2card3 == "light":
        light_chicken()
        clicker()
    print(player2, "the total power of your hand is:", totalPower2)
    clicker()
    
    decideWinner()
   
    if roundWin == "p1win":
        GoodbyeGood()


    elif roundWin == "p2win":
        GoodbyeBad()
    clicker()
    Credits()

powerList = [-1, 1, 2, -2, 4, -3, 3]
cardList = ["fire", "water", "air", "earth", "lightning", "dark", "light"]
roundWin = ""

#p1 deck
p1card1, p1power1 = drawCard()
p1card2, p1power2 = drawCard()
p1card3, p1power3 = drawCard()
hand1 = (p1card1, p1card2, p1card3)
totalPower1 = p1power1 + p1power2 + p1power3

#p2 deck
p2card1, p2power1 = drawCard()
p2card2, p2power2 = drawCard()
p2card3, p2power3 = drawCard()
hand2 = (p2card1, p2card2, p2card3)
totalPower2 = p2power1 + p2power2 + p2power3

elementalChicken()
