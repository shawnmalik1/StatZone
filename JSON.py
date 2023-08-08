import json


def eastAllStars() -> str:
    # Retrieve JSON data from the file
    with open("PS3.json", "r") as file:
        data = json.load(file)

    # Access and process the retrieved JSON data
    players = data["players"]
    allstars_2010_east = data["allStars"][-1]["teams"][0]
    east_all_stars = []
    for i in range(0,11):
        east_all_stars.append(allstars_2010_east[i]["name"])

    # Print the retrieved data
    strAllStar = "";
    for i in range (len(east_all_stars)):
        strAllStar += east_all_stars[i] + "\n"

    return (f"\n {strAllStar}")

def westAllStars() -> str:
    # Retrieve JSON data from the file
    with open("PS3.json", "r") as file:
        data = json.load(file)

    # Access and process the retrieved JSON data
    players = data["players"]
    allstars_2010_west = data["allStars"][7]["teams"][1]
    west_all_stars = []
    for i in range(0,11):
        west_all_stars.append(allstars_2010_west[i]["name"])

    # Print the retrieved data
    strAllStar = "";
    for i in range (len(west_all_stars)):
        strAllStar += west_all_stars[i] + "\n"

    return (f" West All-Stars:\n {strAllStar}")