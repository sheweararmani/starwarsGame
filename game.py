from map import locations
from items import items
from player import *
from music import *
from gameparser import normalise_input
from time import sleep, clock


# Take timed input, timed in seconds.
def input_fast_enough(prompt, correct_input, max_time):
    # Record the time before and after the user types their input.
    start_time = clock()
    user_input = input(correct_input)
    end_time = clock()

    # Return True if they were fast enough and gave the correct input.
    time_taken = end_time - start_time
    if user_input == correct_input and time_taken <= max_time:
        return True
    else:
        return False


# Items in inventory
def list_of_items(items):

    # Create a string of items
    string_of_items = ""
    for item in items:
        if item != items[len(items) - 1]:
            string_of_items = string_of_items + item["name"] + ", "
        else:
            string_of_items = string_of_items + item["name"]
    return string_of_items


# Items in the location
def print_location_items(location):
    # If there are no items, 
    if location["items"] == []:
        return


# Print the current location
def print_location(player):

    # Introduce location
    print("You're currently located in the " + player["location"]["name"] + "...")
    # Describe location
    print(player["location"]["description"])
    print()
    # Display items in location
    print_location_items(player["location"])


# Available exits
def exit_leads_to(exits, direction):
    return locations[exits[direction]]["name"]


# Valid exits
def is_valid_exit(chosen_exit, exits):

    return chosen_exit in exits


# Print exits
def print_exit(direction, leads_to):

    print("GO " + direction.upper() + " to " + leads_to + ".")


# Print menu
def print_menu(exits, location_items, inv_items):

    print("You can:")
    # Iterate over available exits
    for direction in exits:
        # Print exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))

    # Item options
    for item in location_items:
        print("TAKE " + item["id"].upper() + " to take " + item["name"] + ".")
    for item in inv_items:
        print("DROP " + item["id"].upper() + " to drop " + item["name"] + ".")

    print("What do you want to do?")


# Execute Functions
# Execute go
def execute_go(player, direction):
    if is_valid_exit(direction, player["location"]["exits"]):
        player["location"] = move(player["location"]["exits"], direction)
    else:
        print("You cannot go there.")

# Execute take
def execute_take(player, item_id):

    found = False

    for item in player["location"]["items"]:
        if item_id == item["id"] and inventory_mass(player["inventory"]) + item["mass"] <= player["max_mass"]:
            player["inventory"].append(item)
            player["location"]["items"].remove(item)
            found = True
            print(item_id, " added to inventory")
# OPTIONAL - MASS CAPACITY FUNCTION
        elif inventory_mass(player["inventory"]) + item["mass"] > player["max_mass"]:
            print("You've reach your maximum mass capacity")
            # Display mass status
            print("You're carrying" + str(inventory_mass(player["inventory"]) +
                  item["mass"]) + "kg, this is too much!")
            return
    # Necessary reject
    if found == False:
        print("You cannot take that.")


# Execute drop
def execute_drop(player, item_id):

    success = False
    for items in player["inventory"]:
        if item_id == items["id"]:
            player["location"]["items"].append(items)
            player["inventory"].remove(items)
            print(items["name"] + " dropped.")
            success = True
    if success == False:
        print("You cannot drop that.")


# Execute command
def execute_command(player, command):

    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(player, command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(player, command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(player, command[1])
        else:
            print("Drop what?")

    else:
        print("This makes no sense.")


# Inventory mass
def inventory_mass(inventory):

    # Original mass
    x = 0

    # Adding mass to the inventory
    for item in inventory:
        x += item["mass"]

    # Returning the new mass
    return x


# Menu
def menu(exits, location_items, inv_items):

    # Display menu
    print_menu(exits, location_items, inv_items)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    # Return the input
    return normalised_user_input


# Print the player's health
def print_health(player):
    print("Your current health is " + str(player["health"]) + "/" + str(player["max_health"]) + ".")


# Move
def move(exits, direction):
    return locations[exits[direction]]


# Allow the player to choose a character.
def choose_character():
    # Ask the user who to play as, repeat as long as they give invalid input.
    choice = input("Would you like to play as Luke or Han?").lower().strip()
    while choice != "luke" and choice != "han":
        print("You can only choose Luke or Han.")
        choice = input("Would you like to play as Luke or Han?").lower().strip()
    
    if choice == "luke":
        return luke
    else:
        return han


# Main function
def main():
    # Introduction (ready to play etc)
    input("Press enter when you're ready to play")

    # Show the title sequence
    intro()

    print()

    # Allow the user to select a character
    player = choose_character()

    while True:
        # Print status
        print_location(player)
        print_health(player)

        # Show possible actions
        command = menu(player["location"]["exits"],
                       player["location"]["items"], player["inventory"])

        # Execute the user's commands
        execute_command(player, command)


if __name__ == "__main__":
    main()
