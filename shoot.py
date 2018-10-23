from enemies import *
from player import *
from time import clock

killwords = ["bang","pew","shoot","kill"]


def input_fast_enough(max_time,enemy):
    # Record the time before and after the user types their input.
    start_time = clock()
    correct = random.choice(killwords)
    print("Enter the next word quickly!:")
    user_input = input(correct + "\n")
    end_time = clock()
    # Return True if they were fast enough and gave the correct input.
    time_taken = end_time - start_time
    dead = False
    temp = True
    while dead == False:
        if user_input == correct and time_taken <= max_time:
            enemy["health"] = enemy["health"] - luke["luke_damage"]
            if enemy["health"] <= 0:
                print("enemy is dead")
                dead = True
        else:
            luke["luke_max_health"] = luke["luke_max_health"] - 10
            print(luke["luke_max_health"])
            if luke["luke_max_health"] <= 0:
                print("luke is dead")
                dead = True
            else:
                pass

input_fast_enough(3,stormtrooper)
