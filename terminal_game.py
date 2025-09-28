## RPG GAME ##

import random
import time

hp = 500
cutlass_damage = 80
swings = 4
flintlock_damage = 40
ammo = 8
gold = 0

print("====== PIRATE ADVENTURE =======")
print("Prepare to embark on an epic adventure in search of Blackbeard's hidden treasure...")
time.sleep(3)
print("But first, you must select your partner for this journey, choose wisely: ")
time.sleep(3)

print("\n====== COMPANIONS ======")
print("1) Parrot: Will search for ammo or heal HP")
print("2) Coward: Sharpens your cutlass, too afraid to battle")
print("===============================")
pirate_companion = int(input("Enter your choice here: "))
while pirate_companion != 1 and pirate_companion != 2:
    print("Please input either 1 or 2")
    pirate_companion = int(input("Enter here: "))
print("===============================")
if pirate_companion == 1:
    print("You chose a Parrot!")
if pirate_companion == 2:
    print("You chose a Coward!")

time.sleep(2)
print("\n===== THE TAVERN =====")
print("You and your pirate crew have decided to stop at a nearby tavern for the night.")
time.sleep(2)
print("Across the bar, a man gives an intimidating glance...")
time.sleep(3)
print("===============================")
print("Confront him? ")
time.sleep(2)
print("1) Yes")
print("2) No")
print("===============================")
tavern_fight_answer = int(input("Enter your choice: "))
while tavern_fight_answer != 1 and tavern_fight_answer != 2:
    print("Please input either 1 or 2")
    tavern_fight_answer = int(input("Enter here: "))


if tavern_fight_answer == 2:
    print("===============================")
    print("As you leave the tavern, you are stopped by the man")
    time.sleep(1)
    print("He stands in your way in front of the door, leaving no choice but to battle")
    time.sleep(3)
    tavern_crook1_hp = 100
    while tavern_crook1_hp > 0 and hp > 0:
        print("\n===== BATTLE =====")
        print(f"HEALTH: {hp}")
        print(f"SWINGS REMAINING: {swings}")
        print(f"AMMO REMAINING: {ammo}")
        print("===== ENEMY =====")
        print(f"CROOK HP: {tavern_crook1_hp}")
        print("===============================")
        print("What will you do?: ")
        print("1) Cutlass Slice")
        print("2) Flintlock Shot")
        print("3) Call Companion")
        print("===============================")
        tavern_fight_choice = int(input("Enter your choice: "))
        while tavern_fight_choice != 1 and tavern_fight_choice != 2 and tavern_fight_choice != 3:
            print("Please input either 1, 2 or 3")
            tavern_fight_choice = int(input("Enter here: "))
        while ammo <= 0 and tavern_fight_choice == 2:
            print("No Ammo, please try a different option")
            tavern_fight_choice = int(input("Enter here: "))
        while swings <= 0 and tavern_fight_choice == 1:
            print("Out of Swings, try a different option")
            tavern_fight_choice = int(input("Enter here: "))

        if tavern_fight_choice == 1:
            tavern_crook1_hp -= cutlass_damage
            swings -= 1
            print("===============================")
            print("Crook was hit by the cutlass!")
            time.sleep(1)
            print("-1 Swing")
            print("===============================")
            time.sleep(3)

        if tavern_fight_choice == 2:
            tavern_crook1_hp -= flintlock_damage
            ammo -= 1
            print("===============================")
            print("You shot the Crook with the flintlock pistol!")
            time.sleep(1)
            print("-1 Ammo")
            print("===============================")
            time.sleep(3)

        if tavern_fight_choice == 3:
            if pirate_companion == 1:
                parrot_choice = random.randint(1, 2)
                if parrot_choice == 1:
                    print("===============================")
                    print("Parrot Found a Bullet!")
                    time.sleep(1)
                    print("Ammo +1")
                    ammo += 1
                    print("===============================")
                    time.sleep(3)

                if parrot_choice == 2:
                    print("===============================")
                    print("Parrot healed you for 50 HP!")
                    print("===============================")
                    hp += 50
                    time.sleep(3)

            if pirate_companion == 2:
                print("===============================")
                print(
                    "The coward hides behind you, he slowly and quietly sharpens your blade as you stare down the enemy")
                time.sleep(2)
                print("Swings +1")
                swings += 1
                print("===============================")
                time.sleep(3)

        if tavern_crook1_hp < 0:
            break

        crook1_choice = random.randint(1, 2)
        if crook1_choice == 1:
            print("The crook slashes you with a dagger!")
            time.sleep(1)
            print("-40 HP")
            print("===============================")
            hp -= 40
            time.sleep(3)

        if crook1_choice == 2:
            print("The crook hit a sucker punch!")
            time.sleep(1)
            print("-20 HP")
            print("===============================")
            hp -= 20
            time.sleep(3)

    if hp > 0:
        print("You defeated the crook!")
        time.sleep(1)
        print("+20 GOLD")
        gold += 20
    else:
        time.sleep(1)
        print("\nYou were killed in action...")
        time.sleep(1)
        print("GAME OVER")
        quit()

if tavern_fight_answer == 1:
    print("===============================")
    print("You confront the man, the crook clenches his fist and assumes a fighting stance, ready for battle")
    time.sleep(3)
    tavern_crook1_hp = 100
    while tavern_crook1_hp > 0 and hp > 0:
        print("\n===== BATTLE =====")
        print(f"HEALTH: {hp}")
        print(f"SWINGS REMAINING: {swings}")
        print(f"AMMO REMAINING: {ammo}")
        print("===== ENEMY =====")
        print(f"CROOK HP: {tavern_crook1_hp}")
        print("===============================")
        print("What will you do?: ")
        print("1) Cutlass Slice")
        print("2) Flintlock Shot")
        print("3) Call Companion")
        print("===============================")
        tavern_fight_choice = int(input("Enter your choice: "))
        while tavern_fight_choice != 1 and tavern_fight_choice != 2 and tavern_fight_choice != 3:
            print("Please input either 1, 2 or 3")
            tavern_fight_choice = int(input("Enter here: "))
        while ammo <= 0 and tavern_fight_choice == 2:
            print("No Ammo, please try a different option")
            tavern_fight_choice = int(input("Enter here: "))
        while swings <= 0 and tavern_fight_choice == 1:
            print("Out of Swings, try a different option")
            tavern_fight_choice = int(input("Enter here: "))

        if tavern_fight_choice == 1:
            tavern_crook1_hp -= cutlass_damage
            swings -= 1
            print("===============================")
            print("Crook was hit by the cutlass!")
            time.sleep(1)
            print("-1 Swing")
            print("===============================")
            time.sleep(3)


        if tavern_fight_choice == 2:
            tavern_crook1_hp -= flintlock_damage
            ammo -= 1
            print("===============================")
            print("You shot the Crook with the flintlock pistol!")
            time.sleep(1)
            print("-1 Ammo")
            print("===============================")
            time.sleep(3)

        if tavern_fight_choice == 3:
            if pirate_companion == 1:
                parrot_choice = random.randint(1, 2)
                if parrot_choice == 1:
                    print("===============================")
                    print("Parrot Found a Bullet!")
                    time.sleep(1)
                    print("Ammo +1")
                    ammo += 1
                    print("===============================")
                    time.sleep(3)

                if parrot_choice == 2:
                    print("===============================")
                    print("Parrot healed you for 50 HP!")
                    print("===============================")
                    hp += 50
                    time.sleep(3)

            if pirate_companion == 2:
                print("===============================")
                print("The coward hides behind you, he slowly and quietly sharpens your blade as you stare down the enemy")
                time.sleep(2)
                print("Swings +1")
                swings += 1
                print("===============================")
                time.sleep(3)

        if tavern_crook1_hp < 0:
            break

        crook1_choice = random.randint(1,2)
        if crook1_choice == 1:
            print("The crook slashes you with a dagger!")
            time.sleep(1)
            print("-40 HP")
            print("===============================")
            hp -= 40
            time.sleep(3)

        if crook1_choice == 2:
            print("The crook hit a sucker punch!")
            time.sleep(1)
            print("-20 HP")
            print("===============================")
            hp -= 20
            time.sleep(3)

    if hp > 0:
        print("You defeated the crook!")
        time.sleep(1)
        print("+20 GOLD")
        gold += 20
    else:
        time.sleep(1)
        print("\nYou were killed in action...")
        time.sleep(1)
        print("GAME OVER")
        quit()

print("===============================")
time.sleep(2)
print("The crook is laying flat on the ground, with his last breath of strength, he says")
time.sleep(2)
print("CROOK: Step a single foot near Captain Blackbeard and you're a dead man")
time.sleep(2)
print("You brush it off, wondering how he knows about your intention for the gold")
time.sleep(3)
print("In his pocket, you catch sight of a mossy, stone amulet")
time.sleep(2)
print("+1 JUNGLE AMULET")
time.sleep(3)

print("\n===== THE GALLEON =====")
print("After leaving the tavern, you lift anchor and begin sailing...")
time.sleep(3)
print("You catch sight of a ship, all black and sailing faster than the waves")
time.sleep(1)
print("===============================")
print("Follow the ship?: ")
time.sleep(2)
print("1) Yes")
print("2) No")
print("===============================")
follow_answer = int(input("Enter your choice: "))
print("===============================")

while follow_answer != 1 and follow_answer != 2:
    print("Please input either 1 or 2")
    follow_answer = int(input("Enter here: "))

if follow_answer == 2:
    print("Instead of following, you prepare your ship for a long voyage to search all nearby islands")
    time.sleep(4)
    print("Blackbeard must be nearby if one of his crew members are near")
    time.sleep(2)
    print(".")
    time.sleep(2)
    print(".")
    time.sleep(2)
    print(".")
    time.sleep(2)

    print("You dock at a nearby outpost to spend the night and prepare")
    time.sleep(4)

    print("\n===== THE NEXT DAY =====")
    time.sleep(3)
    print("You lower the sails to depart, but they are all ripped up!!")
    time.sleep(2)
    print("BOOOOM")
    time.sleep(4)
    print("You ship explodes from a TNT barrel")
    time.sleep(3)
    print("You are killed from the blast")
    time.sleep(3)
    print("In your last breath, you feel regret for not following the black ship")
    time.sleep(2)
    print("\nGAME OVER")
    quit()

if follow_answer == 1:
    print("You decide to follow the ship, hoping for a lead to find Blackbeard's treasure")
    time.sleep(2)
    print("The ship is heading north, fading into the horizon, but you maintain a steady distance")
    time.sleep(2)
    print("All of a sudden, the ship begins to shake...")
    time.sleep(4)
    print("A KRAKEN! Eight tentacles emerge from the deep dark blue waters")
    time.sleep(2)
    print("You have no choice but to fight back")
    time.sleep(2)

    kraken_hp = 250
    while kraken_hp > 0 and hp > 0:

        print("\n===== BOSS BATTLE - KRAKEN =====")
        print(f"HEALTH: {hp}")
        print(f"SWINGS REMAINING: {swings}")
        print(f"AMMO REMAINING: {ammo}")
        print("===== ENEMY =====")
        print(f"KRAKEN HP: {kraken_hp}")
        print("===============================")
        print("What will you do?: ")
        print("1) Cutlass Slice")
        print("2) Flintlock Shot")
        print("3) Call Companion")
        print("===============================")
        kraken_fight_choice = int(input("Enter your choice: "))
        while kraken_fight_choice != 1 and kraken_fight_choice != 2 and kraken_fight_choice != 3:
            print("Please input either 1, 2 or 3")
            kraken_fight_choice = int(input("Enter here: "))
        while ammo <= 0 and kraken_fight_choice == 2:
            print("No Ammo, please try a different option")
            kraken_fight_choice = int(input("Enter here: "))
        while swings <= 0 and kraken_fight_choice == 1:
            print("Out of Swings, try a different option")
            kraken_fight_choice = int(input("Enter here: "))

        if kraken_fight_choice == 1:
            kraken_hp -= cutlass_damage
            swings -= 1
            print("===============================")
            print("You rush towards the closest tentacle and slash it with your cutlass!")
            time.sleep(1)
            print("-1 Swing")
            print("===============================")
            time.sleep(3)

        while ammo <= 0 and kraken_fight_choice == 2:
            print("No Ammo, please try a different option")
            kraken_fight_choice = int(input("Enter here: "))
        if kraken_fight_choice == 2:
            kraken_hp -= flintlock_damage
            ammo -= 1
            print("===============================")
            print("You shot the Krakens tentacle with the flintlock pistol!")
            time.sleep(1)
            print("-1 Ammo")
            print("===============================")
            time.sleep(3)

        if kraken_fight_choice == 3:
            if pirate_companion == 1:
                parrot_choice = random.randint(1, 2)
                if parrot_choice == 1:
                    print("===============================")
                    print("Parrot Found a Bullet!")
                    time.sleep(1)
                    print("Ammo +1")
                    ammo += 1
                    print("===============================")
                    time.sleep(3)

                if parrot_choice == 2:
                    print("===============================")
                    print("Parrot healed you for 50 HP!")
                    print("===============================")
                    hp += 50
                    time.sleep(3)

            if pirate_companion == 2:
                print("===============================")
                print(
                    "The coward hides behind you, he slowly and quietly sharpens your blade as you stare down the enemy")
                time.sleep(2)
                print("Swings +1")
                swings += 1
                print("===============================")
                time.sleep(3)

        if kraken_hp < 0:
            break

        kraken_choice = random.randint(1, 2)
        if kraken_choice == 1:
            print("The Kraken whips its tentacle onto the ship! Causing you to lose balance and slam your head")
            time.sleep(2)
            print("-20 HP")
            print("===============================")
            hp -= 20
            time.sleep(3)

        if kraken_choice == 2:
            print("The Kraken wraps its tentacles around you and straggles you! You are able to break free")
            time.sleep(1)
            print("-50 HP")
            print("===============================")
            hp -= 50
            time.sleep(3)

    if hp > 0:
        print("You defeated the Kraken!")
        time.sleep(1)
        print("+50 GOLD")
        gold += 50
    else:
        time.sleep(1)
        print("\nYou were killed in action...")
        time.sleep(1)
        print("GAME OVER")
        quit()

    print("===============================")

    time.sleep(4)
    print("\n===== THE SEAS =====")
    print("After barely surviving the deadly kraken, you continue to follow the black ship, sailing in the distance...")
    time.sleep(5)
    print(".")
    time.sleep(2)
    print(".")
    time.sleep(2)
    print(".")
    print("The ship approaches an island overflowing with vegetation, its towering trees and tangled undergrowth unmistakably marking it as a wild, thriving jungle.")
    time.sleep(3)

    print("\n===== JUNGLE ISLAND? =====")

    print("You dock the ship along the shoreline")
    time.sleep(2)
    print("Along with your trusty companion, you slice through the jungle with your cutlass searching for any secrets this island may have")
    time.sleep(4)
    print("You spot a cave, barely visible through the trees and vines")
    time.sleep(3)
    print("It appears the entrance to the cave is shut, with a slot on the wall which can perfectly fit your JUNGLE AMULET")
    time.sleep(2)
    print("===============================")
    print("Place your amulet in the slot?")
    print("1) Yes")
    print("2) No")
    print("===============================")
    slot_answer = int(input("Enter your answer: "))

    while slot_answer != 1 and slot_answer != 2:
        print("Please choose either 1) or 2)")
        slot_answer = int(input("Enter your answer: "))

    if slot_answer == 1:
        time.sleep(2)
        print("You insert the amulet inside of the slot, it fits perfectly")
    elif slot_answer == 2:
        time.sleep(2)
        print("After pondering for a while, you realize that there is no alternative story option programmed for saying no")
        time.sleep(4)
        print("So you wake up to your senses and put the amulet inside the slot")

    time.sleep(2)
    print("-1 JUNGLE AMULET")
    time.sleep(3)
    print("After inserting the amulet, two large rectangular stones separate, opening an entrance")
    time.sleep(3)
    print("You begin to walk inside the dark cave, by switching your eye patch to your other eye, you can see better")
    time.sleep(3)
    print(".")
    time.sleep(2)
    print(".")
    time.sleep(2)
    print(".")
    time.sleep(2)
    print("After walking through the dark cave, you catch a glimmer of light from a torch, with chatter ahead")
    time.sleep(5)
    print("Its heading your way!!")
    time.sleep(3)
    print("You frantically run the other direction, but you're cornered! Light from a torch is emerging from that side as well")
    time.sleep(4)
    print("\nUNKNOWN: I knew you would follow us")
    time.sleep(3)
    print("")
    time.sleep(2)
    print("UNKNOWN: He's mine, time to make an example of him")
    time.sleep(3)
    print("")
    time.sleep(2)
    print("")
    time.sleep(2)
    print("A large, muscular, dark figure, with a coat stretching down to his feet, emerges from the shadows")
    time.sleep(5)
    print("Its Captain Blackbeard, there's no question about it")
    time.sleep(2)
    print("Without a single exchange of words, pirates from both sides form a circle around the two of you")
    time.sleep(3)
    print("Theres no escape, you must fight a death match for your life")
    time.sleep(4)

    print("")
    time.sleep(3)
    print("Deep down, you feel an increase in your will and dedication to win")
    time.sleep(2)
    print("+50 HP")
    time.sleep(1)
    print("+3 SWINGS")
    time.sleep(1)
    print("++ CUTLASS DAMAGE INCREASED")
    time.sleep(3)
    swings += 3
    cutlass_damage = 100

    blackbeard_hp = 500
    while blackbeard_hp > 0 and hp > 0:
        print("\n===== DEATH MATCH - CAPTAIN BLACKBEARD =====")
        print(f"HEALTH: {hp}")
        print(f"SWINGS REMAINING: {swings}")
        print(f"AMMO REMAINING: {ammo}")
        print("===== ENEMY =====")
        print(f"BLACKBEARD HP: {blackbeard_hp}")
        print("===============================")
        print("What will you do?: ")
        print("1) Cutlass Slice")
        print("2) Flintlock Shot")
        print("3) Call Companion")
        print("===============================")
        blackbeard_fight_choice = int(input("Enter your choice: "))
        while blackbeard_fight_choice != 1 and blackbeard_fight_choice != 2 and blackbeard_fight_choice != 3:
            print("Please input either 1, 2 or 3")
            blackbeard_fight_choice = int(input("Enter here: "))
        while ammo <= 0 and blackbeard_fight_choice == 2:
            print("No Ammo, please try a different option")
            blackbeard_fight_choice = int(input("Enter here: "))
        while swings <= 0 and blackbeard_fight_choice == 1:
            print("Out of Swings, try a different option")
            blackbeard_fight_choice = int(input("Enter here: "))

        if blackbeard_fight_choice == 1:
            blackbeard_hp -= cutlass_damage
            swings -= 1
            print("===============================")
            print("Your blades collide with sparks flying across the cave!")
            time.sleep(2)
            print("You find an opening and slice him!")
            time.sleep(1)
            print("-1 Swing")
            print("===============================")
            time.sleep(3)

        while ammo <= 0 and blackbeard_fight_choice == 2:
            print("No Ammo, please try a different option")
            blackbeard_fight_choice = int(input("Enter here: "))

        if blackbeard_fight_choice == 2:
            blackbeard_hp -= flintlock_damage
            ammo -= 1
            print("===============================")
            print("You shot Blackbeard's chest with the flintlock pistol!")
            time.sleep(2)
            print("The bullet causes damage, but barely penetrates his muscle")
            time.sleep(1)
            print("-1 Ammo")
            print("===============================")
            time.sleep(3)

        if blackbeard_fight_choice == 3:
            if pirate_companion == 1:
                parrot_choice = random.randint(1, 2)
                if parrot_choice == 1:
                    print("===============================")
                    print("Parrot Found a Bullet!")
                    time.sleep(1)
                    print("Ammo +1")
                    ammo += 1
                    print("===============================")
                    time.sleep(3)

                if parrot_choice == 2:
                    print("===============================")
                    print("Parrot healed you for 50 HP!")
                    print("===============================")
                    hp += 50
                    time.sleep(3)

            if pirate_companion == 2:
                print("===============================")
                print("The coward hides behind you, he slowly and quietly sharpens your blade as you stare down the enemy")
                time.sleep(2)
                print("Swings +1")
                swings += 1
                print("===============================")
                time.sleep(3)

        if blackbeard_hp <= 0:
            break

        blackbeard_choice = random.randint(1, 4)
        if blackbeard_choice == 1:
            print("Blackbeard sprints towards you and picks you up by the neck")
            time.sleep(3)
            print("As soon as you were about to break free, he tosses you across the ground")
            time.sleep(2)
            print("-80 HP")
            print("===============================")
            hp -= 80
            time.sleep(3)

        if blackbeard_choice == 2:
            print("Blackbeard squares up for a fist exchange, almost seamlessly, he uppercuts you in a flash")
            time.sleep(1)
            print("-50 HP")
            print("===============================")
            hp -= 50
            time.sleep(3)

        if blackbeard_choice == 3:
            if blackbeard_hp > 200:
                time.sleep(2)
                print("The captain stands up, unfazed by your presence, he stands there laughing instead of returning a blow")
                time.sleep(5)
            else:
                time.sleep(2)
                print("The captain falls to one knee from the damage he has taken so far, he gets back up but does not attack")
                time.sleep(4)

        if blackbeard_choice == 4:
            time.sleep(3)
            print("BLACKBEARD: Hit me again! Show me what you got")
            time.sleep(3)


if hp > 0:
    print("Blackbeard falls to his knees, in complete shock of his defeat")
    time.sleep(5)
    print("He takes off his coat, gold is flooding out of his pockets")
    time.sleep(4)
    print("")
    time.sleep(2)
    print("BLACKBEARD: Son...")
    time.sleep(3)
    print("\nBLACKBEARD: Im sorry")
    time.sleep(4)
    print("\nHe takes his last breath, as he falls to the ground")
    time.sleep(3)
    print("\n+1 000 000 GOLD")
    gold += 1000000
    time.sleep(2)
    print("\nThe other pirates are too scared to approach you")
    time.sleep(4)
    print("")
    time.sleep(2)
    print("You stand still in confusion, you've finally reached your goal, but you feel empty inside")
    time.sleep(6)
    print("\nEND - Thanks for playing!")
else:
    time.sleep(1)
    print("\nYou were killed in action...")
    time.sleep(1)
    print("GAME OVER - TRY AGAIN!!")
    quit()


