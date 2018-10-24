# Add "items": [item_a, item_b, ...]
# Add "description": "this is the description."

location_landspeeder = {
    "name": "Landspeeder",

    "exits": {"north": "Farm"}
}

location_toschestation = {
    "name": "Tosche Station",

    "exits":  {"west": "Farm"}
}

location_cantina = {
    "name": "Cantina",

    "exits": {"east": "Farm", "west": "booth", "north": "bar", "south": "TIE Fighter" }
}

location_booth = {
    "name": "Booth",

    "exits": {"east": "Cantina"}
}

location_farm = {
    "name": "Farm",

    "exits": {"west": "Cantina", "south": "Landspeeder", "east": "Tosche Station"}
}

location_bar = {
    "name": "Bar",

    "exits": {"south": "Cantina"}
}

location_tiefighter = {
    "name": "TIE Fighter",
    
    "exits": {"north": "Cantina", "south": "Death Star"}
}

location_deathstar = {
    "name": "Death Star",

    "exits": {"north": "N/4.07", "south": "TIE Fighter", "east": "Leias Cell"}
}

location_leiascell = {
    "name": "Leia's Cell",

    "exits": {"west": "Death Star"}
}

location_n_4_07 = {
    "name": "N/4.07",

    "exits": {"south": "Death Star"}
}

locations = {
    "Landspeeder": location_landspeeder,
    "Tosche Station": location_toschestation,
    "Farm": location_farm,
    "Cantina": location_cantina,
    "Booth": location_booth,
    "Bar": location_bar,
    "TIE Fighter": location_tiefighter,
    "Death Star": location_deathstar,
    "Leia's Cell": location_leiascell,
    "N/4.07": location_n_4_07
}
