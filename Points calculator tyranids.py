army_list = []
names_list = ["biovore", "broodlord", "carnifex"]
total_points = 0
added_points = 0
points_cost = 0

def add (name,amount,weapon1,weapon2):
    if name == "biovore":
        points_cost = 36
        added_points = points_cost*int(amount)
        #total_points_tmp = total_points+str(added_points)
        try:  
            print("you have added "+str(added_points) + " points")
        except:
            print("Oops")
        #print("you have a total of " + total_points + " points")
        #return str(added_points)
    if name == "broodlord":
        points_cost = 162
        added_points = points_cost*int(amount)
        #total_points = total_points+str(added_points)
        print("you have added "+ str(added_points) + " points")
        #print("you have a total of " + total_points + " points")
        #return str(added_points)
    if name == "carnifex":
        points_cost = 67
        if weapon1 == "monstous scything talons" and weapon2 != "monstous scything talons" or weapon1 != "monstous scything talons" and weapon2 == "monstrous scything talons":
            points_cost = points_cost + 14*int(amount)
        if weapon1 == "monstrous scything talons" and weapon2 == "monstrous scything talons":
            points_cost = points_cost + 15*int(amount)
        if weapon1 == "stranglethorn cannon" and weapon2 != "stranglethorn cannon" or weapon1 != "stranglethorn cannon" and weapon2 == "stranglethorn cannon":
            points_cost = points_cost + 25*int(amount)
        if weapon1 == "stranglethorn cannon" and weapon2 == "stranglethorn cannon":
            points_cost = points_cost + 50*int(amount)
        if weapon1 == "venom cannon" and weapon2 != "venom cannon" or weapon1 != "venom cannon" and weapon2 == "venom cannon":
            points_cost = points_cost + 20*int(amount)
        if weapon1 == "venom cannon" and weapon2 == "venom cannon":
            points_cost = points_cost + 40*int(amount)
        if weapon1 == "two devourers with brainleech worms" and weapon2 != "two devourers with brainleech worms" or weapon1 != "two devourers with brainleech worms" and weapon2 == "two devourers with brainleech worms":
            points_cost = points_cost + 14*int(amount)
        if weapon1 == "two devourers with brainleech worms" and weapon2 == "two devourers with brainleech worms":
            points_cost = points_cost + 28*int(amount)
        if weapon1 == "two deathspitters with slimer maggots" and weapon2 != "two deathspitters with slimer maggots" or weapon1 != "two deathspitters with slimer maggots" and weapon2 == "two deathspitters with slimer maggots":
            points_cost = points_cost + 14*int(amount)
        if weapon1 == "two deathspitters with slimer maggots" and weapon2 == "two deathspitters with slimer maggots":
            points_cost = points_cost + 28*int(amount)
        added_points = points_cost*int(amount)
        #total_points = total_points+str(added_points)
        print("you have added "+ str(added_points) + " points")
        #print("you have a total of " + total_points + " points")
    return added_points 
while True:
    print("choose unit")
    unit = input()
    print("choose unit size")
    size = input()
    print("choose weapon 1")
    firstweapon = input()
    print("choose weapon 2")
    secondweapon = input()
    total_points+=add(unit,size,firstweapon,secondweapon)
    print("You now have a total of" + total_points + " points")
