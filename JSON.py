import json


def eastAllStars() -> str:
    # Retrieve JSON data from the file
    with open("Draft.json", "r") as file:
        data = json.load(file)

    # Access and process the retrieved JSON data
    players = data["players"]
    allstars_east = data["allStars"][-1]["teams"][0]
    east_all_stars = []
    for i in range(0,12):
        east_all_stars.append(allstars_east[i]["name"])

    # Print the retrieved data
    strAllStar = "";
    for i in range (len(east_all_stars)):
        strAllStar += east_all_stars[i] + "\n"

    return (f"\n **East All Stars:** \n {strAllStar}")

def westAllStars() -> str:
    # Retrieve JSON data from the file
    with open("Draft.json", "r") as file:
        data = json.load(file)

    # Access and process the retrieved JSON data
    players = data["players"]
    allstars_west = data["allStars"][-1]["teams"][1]
    west_all_stars = []
    for i in range(0,12):
        west_all_stars.append(allstars_west[i]["name"])

    # Print the retrieved data
    strAllStar = "";
    for i in range (len(west_all_stars)):
        strAllStar += west_all_stars[i] + "\n"

    return (f"\n **West All Stars:** \n {strAllStar}")

def findPlayer(given_player) -> str:
    # Retrieve JSON data from the file
    with open("Draft.json", "r") as file:
        data = json.load(file)

    # Access and process the retrieved JSON data
    players = data["players"]
    teams = data["teams"]

    playerData = ""
    for player in players:
        if player.firstName + " " + player.lastName == given_player:
            playerData = 0