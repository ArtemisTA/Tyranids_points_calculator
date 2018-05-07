army_list = []
names_list = ["biovore", "broodlord", "carnifex"]
total_points = 0
added_points = 0
points_cost = 0
alwaystrue = True

def add (name,amount,weapon1,weapon2,addordel):
    if name == "biovore":
        points_cost = 36
        added_points = points_cost*int(amount)
    if name == "broodlord":
        points_cost = 162
        added_points = points_cost*int(amount)
    if name == "carnifex":
        points_cost = 67
        if weapon1 == "monstous scything talons" and weapon2 != "monstous scything talons" or weapon1 != "monstous scything talons" and weapon2 == "monstrous scything talons":
            points_cost = points_cost + 14
        if weapon1 == "monstrous scything talons" and weapon2 == "monstrous scything talons":
            points_cost = points_cost + 15
        if weapon1 == "stranglethorn cannon" and weapon2 != "stranglethorn cannon" or weapon1 != "stranglethorn cannon" and weapon2 == "stranglethorn cannon":
            points_cost = points_cost + 25
        if weapon1 == "stranglethorn cannon" and weapon2 == "stranglethorn cannon":
            points_cost = points_cost + 50
        if weapon1 == "heavy venom cannon" and weapon2 != "heavy venom cannon" or weapon1 != "heavy venom cannon" and weapon2 == "heavy venom cannon":
            points_cost = points_cost + 20
        if weapon1 == "heavy venom cannon" and weapon2 == "heavy venom cannon":
            points_cost = points_cost + 40
        if weapon1 == "two devourers with brainleech worms" and weapon2 != "two devourers with brainleech worms" or weapon1 != "two devourers with brainleech worms" and weapon2 == "two devourers with brainleech worms":
            points_cost = points_cost + 14
        if weapon1 == "two devourers with brainleech worms" and weapon2 == "two devourers with brainleech worms":
            points_cost = points_cost + 28
        if weapon1 == "two deathspitters with slimer maggots" and weapon2 != "two deathspitters with slimer maggots" or weapon1 != "two deathspitters with slimer maggots" and weapon2 == "two deathspitters with slimer maggots":
            points_cost = points_cost + 14
        if weapon1 == "two deathspitters with slimer maggots" and weapon2 == "two deathspitters with slimer maggots":
            points_cost = points_cost + 28
        if weapon1 == "monstrous crushing claws" and weapon2 != "monstrous crushing claws" or weapon1 != "monstrous crushing claws" and weapon2 == "monstrous crushing claws":
            points_cost = points_cost + 12
        if weapon1 == "monstrous crushing claws" and weapon2 == "monstrous crushing claws":
            points_cost = points_cost + 24
        added_points = points_cost*int(amount)
    if name == "exocrine":
        points_cost = 216
        added_points = points_cost*int(amount)
    if name == "gargoyle":
        points_cost = 6
        added_points = points_cost*int(amount)
    if name == "genestealer":
        points_cost = 12
        added_points = points_cost*int(amount)
    if name == "harpy":
        points_cost = 179
        added_points = points_cost*int(amount)
    if name == "haruspex":
        points_cost = 198
        added_points = points_cost*int(amount)
    if name == "hive crone":
        points_cost = 161
        added_points = points_cost*int(amount)
    if name == "hive guard":
        points_cost = 18
        if weapon1 == "shockcannon":
            points_cost = points_cost + 21
        if weapon1 == "impaler cannon":
            points_cost = points_cost + 30
        added_points = points_cost*int(amount)
    if name == "hive tyrant":
        points_cost = 143
        if weapon1 == "stranglethorn cannon" and weapon2 != "stranglethorn cannon" or weapon1 != "stranglethorn cannon" and weapon2 == "stranglethorn cannon":
            points_cost = points_cost + 25
        if weapon1 == "stranglethorn cannon" and weapon2 == "stranglethorn cannon":
            points_cost = points_cost + 50
        if weapon1 == "heavy venom cannon" and weapon2 != "heavy venom cannon" or weapon1 != "heavy venom cannon" and weapon2 == "heavy venom cannon":
            points_cost = points_cost + 20
        if weapon1 == "heavy venom cannon" and weapon2 == "heavy venom cannon":
            points_cost = points_cost + 40
        if weapon1 == "two devourers with brainleech worms" and weapon2 != "two devourers with brainleech worms" or weapon1 != "two devourers with brainleech worms" and weapon2 == "two devourers with brainleech worms":
            points_cost = points_cost + 14
        if weapon1 == "two devourers with brainleech worms" and weapon2 == "two devourers with brainleech worms":
            points_cost = points_cost + 28
        if weapon1 == "two deathspitters with slimer maggots" and weapon2 != "two deathspitters with slimer maggots" or weapon1 != "two deathspitters with slimer maggots" and weapon2 == "two deathspitters with slimer maggots":
            points_cost = points_cost + 14
        if weapon1 == "two deathspitters with slimer maggots" and weapon2 == "two deathspitters with slimer maggots":
            points_cost = points_cost + 28
        if weapon1 == "monstrous scything talons" and weapon2 == "monstrous scything talons":
            points_cost = points_cost + 20
        if weapon1 == "monstrous scything talons" and weapon2 != "monstrous scything talons" or weapon1 != "monstrous scything talons" and weapon2 == "monstrous scything talons":
            points_cost = points_cost + 15
        if weapon1 == "monstrous boneswords" and weapon2 == "monstrous boneswords":
            points_cost = points_cost + 40
        if weapon1 == "monstrous boneswords" and weapon2 != "monstrous boneswords" or weapon1 != "monstrous boneswords" and weapon2 == "monstrous boneswords":
            points_cost = points_cost + 20
        if weapon1 == "lash whip and monstrous bonesword" and weapon2 == "lash whip and monstrous bonesword":
            points_cost = points_cost + 30
        if weapon1 == "lash whip and monstrous bonesword" and weapon2 != "lash whip and monstrous bonesword" or weapon1 != "lash whip and monstrous bonesword" and weapon2 == "lash whip and monstrous bonesword":
            points_cost = points_cost + 15
        added_points = points_cost*int(amount)
    if name == "hive tyrant with wings":
        points_cost = 170
        if weapon1 == "stranglethorn cannon" and weapon2 != "stranglethorn cannon" or weapon1 != "stranglethorn cannon" and weapon2 == "stranglethorn cannon":
            points_cost = points_cost + 25
        if weapon1 == "stranglethorn cannon" and weapon2 == "stranglethorn cannon":
            points_cost = points_cost + 50
        if weapon1 == "heavy venom cannon" and weapon2 != "heavy venom cannon" or weapon1 != "heavy venom cannon" and weapon2 == "heavy venom cannon":
            points_cost = points_cost + 20
        if weapon1 == "heavy venom cannon" and weapon2 == "heavy venom cannon":
            points_cost = points_cost + 40
        if weapon1 == "two devourers with brainleech worms" and weapon2 != "two devourers with brainleech worms" or weapon1 != "two devourers with brainleech worms" and weapon2 == "two devourers with brainleech worms":
            points_cost = points_cost + 14
        if weapon1 == "two devourers with brainleech worms" and weapon2 == "two devourers with brainleech worms":
            points_cost = points_cost + 28
        if weapon1 == "two deathspitters with slimer maggots" and weapon2 != "two deathspitters with slimer maggots" or weapon1 != "two deathspitters with slimer maggots" and weapon2 == "two deathspitters with slimer maggots":
            points_cost = points_cost + 14
        if weapon1 == "two deathspitters with slimer maggots" and weapon2 == "two deathspitters with slimer maggots":
            points_cost = points_cost + 28
        if weapon1 == "monstrous scything talons" and weapon2 == "monstrous scything talons":
            points_cost = points_cost + 20
        if weapon1 == "monstrous scything talons" and weapon2 != "monstrous scything talons" or weapon1 != "monstrous scything talons" and weapon2 == "monstrous scything talons":
            points_cost = points_cost + 15
        if weapon1 == "monstrous boneswords" and weapon2 == "monstrous boneswords":
            points_cost = points_cost + 40
        if weapon1 == "monstrous boneswords" and weapon2 != "monstrous boneswords" or weapon1 != "monstrous boneswords" and weapon2 == "monstrous boneswords":
            points_cost = points_cost + 20
        if weapon1 == "lash whip and monstrous bonesword" and weapon2 == "lash whip and monstrous bonesword":
            points_cost = points_cost + 30
        if weapon1 == "lash whip and monstrous bonesword" and weapon2 != "lash whip and monstrous bonesword" or weapon1 != "lash whip and monstrous bonesword" and weapon2 == "lash whip and monstrous bonesword":
            points_cost = points_cost + 15
        added_points = points_cost*int(amount)
    if name == "hormagaunt":
        points_cost = 5
        added_points = points_cost*int(amount)
    if name == "lictor":
        points_cost = 45
        added_points = points_cost*int(amount)
    if name == "maleceptor":
        points_cost = 172
        added_points = points_cost*int(amount)
    if name == "mawloc":
        points_cost = 104
        added_points = points_cost*int(amount)
    if name == "mucolid spore":
        points_cost = 20
        added_points = points_cost*int(amount)
    if name == "neurothrope":
        points_cost = 70
        added_points = points_cost*int(amount)
    if name == "pyrovore":
        points_cost = 38
        added_points = points_cost*int(amount)
    if name == "ravener":
        points_cost = 23
        if weapon1 == "devourer" and weapon2 != "devourer" or weapon1 != "devourer" and weapon2 == "devourer":
            points_cost = points_cost + 4
        if weapon1 == "spinefists" and weapon2 != "spinefists" or weapon1 != "spinefists" and weapon2 == "spinefists":
            points_cost = points_cost + 1
        if weapon1 == "deathspitter" and weapon2 != "deathspitter" or weapon1 != "deathspitter" and weapon2 == "deathspitter":
            points_cost = points_cost + 5
        if weapon1 == "rending claws" or weapon2 == "rending claws":
            points_cost = points_cost + 2
        added_points = points_cost * int(amount)
    if name == "ripper swarm":
        points_cost = 11
        if weapon1 == "spinemaws" or weapon2 == "spinemaws":
            points_cost = points_cost + 2
        added_points = points_cost * int(amount)
    if name == "screamer-killers":
        points_cost = 105
        added_points = points_cost * int(amount)
    if name == "spore mine":
        points_cost = 10
        added_points = points_cost*int(amount)
    if name == "sporocyst":
        points_cost = 79
        if weapon1 == "barbed strangler" or weapon2 == "barbed strangler":
            points_cost = points_cost + 50
        if weapon2 == "deathspitter" or weapon1 == "deathspitter":
            points_cost = points_cost + 25
        if weapon1 == "venom cannon" or weapon2 == "venom cannon":
            points_cost = points_cost + 100
        added_points = points_cost*int(amount)
    if name == "termagant":
        points_cost = 4
        if weapon1 == "devourer":
            points_cost = points_cost + 4
        added_points = points_cost*int(amount)
    if name == "tervigon":
        points_cost = 233
        if weapon1 == "massive scything talons":
            points_cost = points_cost + 10
        if weapon2 == "massive crushing claws":
            points_cost = points_cost + 20
        added_points = points_cost * int(amount)
    if name == "thornback":
        points_cost = 70
        if weapon1 == "monstrous scything talons" or weapon2 == "monstrous scything talons":
            points_cost = points_cost + 10
        if weapon2 == "two devourers with brainleech worms" or weapon1 == "two devourers with brainleech worms":
            points_cost = points_cost + 7
        if weapon2 == "stranglethorn cannon" or weapon1 == "stranglethorn cannon":
            points_cost = points_cost + 25
        if weapon1 == "monstrous crushing claws" or weapon2 == "monstrous crushing claws":
            points_cost = points_cost + 20
        added_points = points_cost * int(amount)
    if name == "toxicrene":
        points_cost = 157
        added_points = points_cost * int(amount)
    if name == "trygon":
        points_cost = 168
        added_points = points_cost * int(amount)
    if name == "trygon prime":
        points_cost = 198
        added_points = points_cost * int(amount)
    if name == "tyranid prime":
        points_cost = 100
        if weapon1 == "devourer" or weapon2 == "devourer":
            points_cost = points_cost + 4
        if weapon1 == "deathspitter" or weapon2 == "deathspitter":
            points_cost = points_cost + 5
        if weapon1 == "spinefists" or weapon2 == "spinefists":
            points_cost = points_cost + 1
        if weapon1 == "rending claws" and weapon2 != "rending claws" or weapon1 != "rending claws" and weapon2 == "rending claws":
            points_cost = points_cost + 2
        if weapon1 == "rending claws" and weapon2 == "rending claws":
            points_cost = points_cost + 4
        if weapon1 == "boneswords" and weapon2 != "boneswords" or weapon1 != "boneswords" and weapon2 == "boneswords":
            points_cost = points_cost + 2
        if weapon1 == "boneswords" and weapon2 == "boneswords":
            points_cost = points_cost + 4
        if weapon1 == "lash whip and bonesword" and weapon2 != "lash whip and boneswords" or weapon1 != "lash whip and bonesword" and weapon2 == "lash whip and bonesword":
            points_cost = points_cost + 2
        if weapon1 == "lash whip and bonesword" and weapon2 == "lash whip and bonesword":
            points_cost = points_cost + 4
        added_points = points_cost * int(amount)
    if name == "tyranid warrior":
        points_cost = 20
        if weapon1 == "devourer" or weapon2 == "devourer":
            points_cost = points_cost + 4
        if weapon1 == "deathspitter" or weapon2 == "deathspitter":
            points_cost = points_cost + 5
        if weapon1 == "spinefists" or weapon2 == "spinefists":
            points_cost = points_cost + 1
        if weapon1 == "rending claws" and weapon2 != "rending claws" or weapon1 != "rending claws" and weapon2 == "rending claws":
            points_cost = points_cost + 2
        if weapon1 == "rending claws" and weapon2 == "rending claws":
            points_cost = points_cost + 4
        if weapon1 == "boneswords" and weapon2 != "boneswords" or weapon1 != "boneswords" and weapon2 == "boneswords":
            points_cost = points_cost + 2
        if weapon1 == "boneswords" and weapon2 == "boneswords":
            points_cost = points_cost + 4
        if weapon1 == "lash whip and bonesword" and weapon2 != "lash whip and boneswords" or weapon1 != "lash whip and bonesword" and weapon2 == "lash whip and bonesword":
            points_cost = points_cost + 2
        if weapon1 == "lash whip and bonesword" and weapon2 == "lash whip and bonesword":
            points_cost = points_cost + 4
        if weapon1 == "barbed strangler" or weapon2 == "barbed strangler":
            points_cost = points_cost + 15
        if weapon1 == "venom cannon" or weapon2 == "venom cannon":
            points_cost = points_cost + 20
        added_points = points_cost * int(amount)
    if name == "tyrannocyte":
        points_cost = 98
        if weapon1 == "barbed strangler" or weapon2 == "barbed strangler":
            points_cost = points_cost + 50
        if weapon2 == "deathspitter" or weapon1 == "deathspitter":
            points_cost = points_cost + 25
        if weapon1 == "venom cannon" or weapon2 == "venom cannon":
            points_cost = points_cost + 100
        added_points = points_cost*int(amount)
    if name == "tyrannofex":
        points_cost = 189
        if weapon1 == "acid spray" or weapon2 == "acid spray":
            points_cost = points_cost + 25
        if weapon1 == "fleshborer hive" or weapon2 == "fleshborer hive":
            points_cost = points_cost + 15
        if weapon1 == "rupture cannon" or weapon2 == "rupture cannon":
            points_cost = points_cost + 49
        added_points = points_cost *int(amount)
    if name == "tyrant guard":
        points_cost = 37
        if weapon1 == "crushing claws" or weapon2 == "crushing claws":
            points_cost = points_cost + 15
        if weapon1 == "lash whip and bonesword" or weapon2 == "lash whip and bonesword":
            points_cost = points_cost + 2
        added_points = points_cost * int(amount)
    if name == "venomthrope":
        points_cost = 30
        added_points = points_cost * int(amount)
    if name == "zoanthrope":
        points_cost = 40
        added_points = points_cost * int(amount)
    if name == "deathleaper":
        points_cost = 90
        added_points = points_cost * int(amount)
    if name == "old one eye":
        points_cost = 200
        added_points = points_cost * int(amount)
    if name == "the red terror":
        points_cost = 75
        added_points = points_cost * int(amount)
    if name == "the swarmlord":
        points_cost = 300
        added_points = points_cost * int(amount)
    if addordel == "add":
        print("you have added a total of " + str(added_points) + " points")
        return added_points
    if addordel == "delete":
        print("you have removed a total of " + str(added_points) + " points")
        return added_points * -1
print("WELCOME! This is V1.0 of the Tyranids points calculator program! There are a few rules to using this...")
print(" Rule 1: This points counter will tell you the points however IT IS NOT A CODEX. Values such as unit size")
print("     and weapon choices will have to be looked up in the Tyranids 8th edition codex")
print(" Rule 2: ALWAYS enter the singular version of the model e.g: gargoyle, termagant, hormagaunt otherwise it will malfunction, this")
print("     does not apply for weapons so you can still input weapons such as 'spinemaws' normally as written in codex")
print(" Rule 3: If you desire, you do not have to enter the weapons for a model which cannot choose it's weapons. Similarly,")
print("     if a unit can only take one weapon, leave <weapon2> blank")
print(" Rule 4: If you have a unit with different weapons e.g: 10 termagants 5 devourers 5 fleshborers, input this as")
print("     5 termagants with fleshborers and 5 termagants with devourers seperately")
print(" Rule 5: if the chosen unit can have 3 or more weapons, only input the weapons which are not free and are optional. e.g:")
print("     with raveners, who can take 3 weapons (one of which must be scything talons) do not input scything talons as they are free")
print(" Rule 6: SPOROCYST AND TYRANNOCYTE ONLY: you may only input the one weapon you will take 5 times in any of the weapon slots")
print("----------------------------------------------------------------------------------------------------------------------------------")
while alwaystrue:
    print("add or delete a unit?")
    plusorminus = input()
    print("choose unit")
    unit = input()
    print("choose unit size")
    size = input()
    print("choose weapon 1")
    firstweapon = input()
    print("choose weapon 2")
    secondweapon = input()
    total_points+=add(unit,size,firstweapon,secondweapon,plusorminus)
    print("You now have a total of " + str(total_points) + " points")
    print("would you like to quit?")
    choice = input()
    if choice == "yes":
        alwaystrue = False
    
