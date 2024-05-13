def findAllStars(data):
    # Access and process the retrieved JSON data
    allstars_east = data["allStars"][-1]["teams"][0]
    east_all_stars = []
    for player in allstars_east:
        east_all_stars.append(player["name"])

    allstars_west = data["allStars"][-1]["teams"][1]
    west_all_stars = []
    for player in allstars_west:
        west_all_stars.append(player["name"])
    # Print the retrieved data
    strEastAllStar = "";
    for i in range(len(east_all_stars)):
        strEastAllStar += east_all_stars[i] + "\n"

    strWestAllStar = "";
    for i in range(len(west_all_stars)):
        strWestAllStar += west_all_stars[i] + "\n"

    return (f"\n **East All Stars:** \n {strEastAllStar} \n **West All Stars:** \n {strWestAllStar}")