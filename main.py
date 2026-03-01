import random
import time
coun = 1
while coun == 1:
    chosen_chars = [""]
    counter = 9
    spells = {
    "Thunderbolt" : "Electric",
    "Nightmare Grasp" : "Dark",
    "\'Antidote\' Stone Fist" : "Ground",
    "Frostbite" : "Ice",
    "Flame Vortex" : "Fire",
    "Tsunami" : "Water",
    "Rotten Bite" : "Poison",
    "Diamond Pickaxe" : "Metal",
    "Root Grave \'Isolator\'" : "Wood",
    "Blinding Shock" : "Light"
    }
    weakness = ("Bronzium", "Solaris", "Toxis", "Aqueon", "Frostix", "Inferno", "Timberon", "Stonek", "Voltis", "Noxor")
    chars = ["Voltis", "Noxor", "Stonek", "Frostix", "Inferno", "Aqueon", "Toxis", "Bronzium", "Timberon", "Solaris"]
    per_chars = ["Voltis", "Noxor", "Stonek", "Frostix", "Inferno", "Aqueon", "Toxis", "Bronzium", "Timberon", "Solaris"]
    resistance = {
    "Voltis" : 0.7,
    "Noxor" : 0.4,
    "Stonek" : 1.7,
    "Frostix" : 1.6,
    "Inferno" : 1,
    "Aqueon" : 0.9,
    "Toxis" : 1.2,
    "Bronzium" : 1.2,
    "Timberon" : 1.1,
    "Solaris" : 1.6
    }
    e_type = {
    "Voltis" : "Electric",
    "Noxor" : "Dark",
    "Stonek" : "Ground",
    "Frostix" : "Ice",
    "Inferno" : "Fire",
    "Aqueon" : "Water",
    "Toxis" : "Poison",
    "Bronzium" : "Metal",
    "Timberon" : "Wood",
    "Solaris" : "Light"
    }
    health = {
    "Voltis" : 90,
    "Noxor" : 130,
    "Stonek" : 120,
    "Frostix" : 50,
    "Inferno" : 80,
    "Aqueon" : 110,
    "Toxis" : 150,
    "Bronzium" : 90,
    "Timberon" : 125,
    "Solaris" : 60
    }
    print("""
               ©Ibrahim Malas

\033[38;2;255;255;120m█     █     █  █████  █████     █    ████   ████   █
 █   █ █   █     █       █     █ █   █   █  █   █  █
  █ █   █ █      █      █     █████  ████   █   █
   █     █     █████   █████  █   █  █   █  ████   █\033[0m\n
\033[1mSave the lands\033[0m with your \033[1mmighty staff of power!\033[0m You have a \033[1mlimited\033[0m number of \033[1mturns\033[0m to \033[1mdefeat\033[0m all of the \033[1menemies\033[0m.
Each enemy has its \033[38;2;85;0;189mtype\033[0m, \033[38;2;0;58;208mresistance\033[0m (defence), and \033[38;2;235;50;0mhealth\033[0m shown. Also, Wood types are made of inflammable wood.
Choose your \033[38;2;200;200;200mdifficulty\033[0m:
\033[1m1\033[0m for \033[38;2;124;255;112mEasy\033[0m (2 enemies, 8 rounds) \n\033[1m2\033[0m for \033[38;2;255;255;112mNormal\033[0m (4 enemies, 14 rounds) \n\033[1m3\033[0m for \033[38;2;149;0;0mNightmare\033[0m (7 enemies, 24 rounds)""")
    while True:
        try:
            difficulty = int(input(""))
        except:
            print("You did not enter a valid response. Try again.")
        else:
            if 1 <= difficulty <= 3:
                break
            else:
                print("You did not enter a valid response. Try again.")
    if difficulty == 1:
        num_chars = 2
        rounds = 8
        difficulty = "Easy"
    elif difficulty == 2:
        num_chars = 4
        rounds = 14
        difficulty = "Normal"
    else:
        num_chars = 7
        rounds = 24
        difficulty = "Nightmare"
    for a in range(num_chars):  
        chosen_chars.insert(0, chars[random.randint(0, counter)])
        chars.remove(chosen_chars[0])
        counter -= 1
    counter = 0
    print("\nYou have\033[1m", rounds, "\033[0mrounds to defeat all monsters! \033[1mGO!\033[0m")
    current = chosen_chars[0]
    curr_health = health.get(current)
    for b in range(rounds):
        current = chosen_chars[0]
        print("\nEnemy: ", current, "\nRound ", b + 1, "\nType: ", e_type.get(current),
        "\nResistance Multiplier: ", resistance.get(current), "\nHealth: ", curr_health, "\nChoose a spell:", sep = "")
        time.sleep(0.8)
        for key in spells:
            counter += 1
            print("\033[1m" + str(counter), "\033[0mfor", key)
            time.sleep(0.1)
        counter = 0
        while True:
            try:
                spell_c = int(input("\nMake your decision: \033[38;2;42;194;51m"))
                print("\033[0m")
            except:
                print("\nYou did not enter a valid response. Try again.")
            else:
                if 1 <= spell_c <= 10:
                    break
                else: 
                    print("You did not enter a valid response. Try again.")
        if spell_c == weakness.index(current) + 1:
            print("Your spell was extremely effective against the enemy!")
            curr_health -= 70 / resistance.get(current)
            if curr_health <= 0:
                print("You defeated", current, "!!!")
                chosen_chars.remove(current)
                curr_health = health.get(chosen_chars[0])
                if chosen_chars[0] == "":
                    break
            else:
                time.sleep(0.5)
                curr_health = round(curr_health, 1)
            time.sleep(1)
        elif spell_c == per_chars.index(current) + 1:
            print("You dealt no damage because your spell was the same as your enemy's type!")
            time.sleep(1)
        else:
            print("You dealt damage, but you could have done more if you used an element that is stronger against the enemy's type.")
            curr_health -= 40 / resistance.get(current)
            if curr_health <= 0:
                print("You defeated", current, "!!!")
                chosen_chars.remove(current)
                curr_health = health.get(chosen_chars[0])
                if chosen_chars[0] == "":
                    break
            else:
                curr_health = round(curr_health, 1)
            time.sleep(1)
    if chosen_chars[0] == "":
        print("You finished off all the enemies on", difficulty, "difficulty! You Won!")
        print("""░░░░░░░░░░░░░░░░░░░░░
░░░░█▀▀▀░█▀▀▀░░░█░░░░
░░░░█░▀█░█░▀█░░░▀░░░░
░░░░▀▀▀▀░▀▀▀▀░░░▀░░░░
░░░░░░░░░░░░░░░░░░░░░""")
    else:
        print("You lost because you couldn't eliminate all the enemies in time :(")
    while True:
        try:
            time.sleep(0.5)
            coun = int(input("Do you want to play again? 0 for no, 1 for yes. "))
        except:
            print("You did not enter a valid response. Try again.")
        else:
            if coun == 1:
                print("Restarting....")
                time.sleep(1)
                chars = ["Voltis", "Noxor", "Stonek", "Frostix", "Inferno", "Aqueon", "Toxis", "Bronzium", "Timberon", "Solaris"]
                break
            elif coun == 0:
                print("Ending....")
                break
            else:
                print("You did not enter a valid response. Try again.")