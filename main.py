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
               █████     █████
               █████     █████
                    █████
                  █████████
                  █████████
                  ██     ██

█     █     █  █████  █████     █    ████   ████   █
 █   █ █   █     █       █     █ █   █   █  █   █  █
  █ █   █ █      █      █     █████  ████   █   █
   █     █     █████   █████  █   █  █   █  ████   █\n
Save the lands with your mighty staff of power! You have a limited number of turns to defeat all of the enemies.
Each enemy has its type, resistance (defence), and health shown. Also, Wood types are made of inflammable wood.
Choose your difficulty:
1 for Easy (2 enemies, 8 rounds) \n2 for Normal (4 enemies, 14 rounds) \n3 for Nightmare (7 enemies, 24 rounds)""")
	while True:
		try:
			difficulty = int(input(""))
		except:
			print("You did not enter a valid answer. Try again.")
		else:
			if 1 <= difficulty <= 3:
				break
			else: 
				print("You did not enter a valid answer. Try again.")
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
	print("You have", rounds, "rounds to defeat all monsters! GO!")
	current = chosen_chars[0]
	curr_health = health.get(current)
	for b in range(rounds):
		current = chosen_chars[0]
		print("Enemy: ", current, "\nRound ", b + 1, "\nType: ", e_type.get(current),
		"\nResistance Multiplier: ", resistance.get(current), "\nHealth: ", curr_health, "\nChoose a spell:", sep = "")
		time.sleep(0.8)
		for key in spells:
			counter += 1
			print(counter, "for", key)
			time.sleep(0.1)
		counter = 0
		while True:
			try:
				spell_c = int(input("Make your decision: "))
			except:
				print("You did not enter a valid answer. Try again.")
			else:
				if 1 <= spell_c <= 10:
					break
				else: 
					print("You did not enter a valid answer. Try again.")
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
			print("You did not enter a valid answer. Try again.")
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
				print("You did not enter a valid answer. Try again.")
