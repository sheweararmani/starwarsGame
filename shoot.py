from enemies import *
from player import *
from time import clock,sleep



def fight(max_time,enemy):
    # Record the time before and after the user types their input.
    print("Enemy: {}".format(enemy["name"]))
    sleep(1)
    print("Enter the next word quickly!:")
    sleep(0.5)
    print(".")
    sleep(0.5)
    print(".")
    sleep(0.5)
    print(".")
    sleep(0.5)
    print("Fight!")
    start_time = clock()
    end_time = clock()
    # Check if they were fast enough and gave the correct input.
    time_taken = end_time - start_time
    while True:
        killwords = enemy["killwords"]
        correct = random.choice(killwords)
        user_input = input(correct + "\n")
        if user_input == correct and time_taken <= max_time:
            enemy["health"] = enemy["health"] - luke["damage"]
            print(enemy["health"])
            if enemy["health"] <= 0:
                return True
        else:
            luke["health"] = luke["health"] - enemy["damage"]
            print(luke["health"])
            if luke["health"] <= 0:
                return False


