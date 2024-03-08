import json


# Retrieve JSON data from the file
with open("2015FantasyDraft.json", "r") as file:
    data = json.load(file)

def allStars() -> str:
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
    for i in range (len(east_all_stars)):
        strEastAllStar += east_all_stars[i] + "\n"

    strWestAllStar = "";
    for i in range (len(west_all_stars)):
        strWestAllStar += west_all_stars[i] + "\n"

    return (f"\n **East All Stars:** \n {strEastAllStar} \n **West All Stars:** \n {strWestAllStar}")

def findPlayer(given_player) -> str:
    # Access and process the retrieved JSON data
    players = data["players"]
    teams = data["teams"]

    for player in players:
        if player["firstName"] + " " + player['lastName'] == given_player:
            if(not player['stats']):
                return "Player is a rookie! Has not played a game yet."
            playerData = player['stats'][-1]
            ppg = round((float(playerData['pts'])/playerData['gp']), 2)
            apg = round((float(playerData['ast'])/playerData['gp']), 2)
            rpg = round((float((playerData['orb'] +playerData['drb']))/playerData['gp']), 2)
            spg = round((float(playerData['stl'])/playerData['gp']), 2)
            bpg = round((float(playerData['blk'])/playerData['gp']), 2)
            ewa = round(float(playerData['ewa']), 2)
            per = round(float(playerData['per']), 2)
            fg = round((100 * float(playerData['fg'] / playerData['fga'])), 2)
            tp = round((100 * float(playerData['tp'] / playerData['tpa'])), 2)
            statsStr = f'**PPG: **' + str(ppg) + "\n" + \
                       f'**APG: **' + str(apg) + "\n" + \
                       f'**RPG: **' + str(rpg) + "\n" + \
                       f'**SPG: **' + str(spg) + "\n" + \
                       f'**BPG: **' + str(bpg) + "\n" + \
                       f'**EWA: **' + str(ewa) + "\n" + \
                       f'**PER: **' + str(per) + "\n" + \
                       f'**FG%: **' + str(fg) + "\n" + \
                       f'**3PT%: **' + str(tp) + "\n"
            return f'{statsStr}'

    return f'Player not found.'

def player_strength_and_weakness(playerName):
    # Find the player's data using the player_name
    target_player = None
    for player in data['players']:
        if (player['firstName'] + " " + player['lastName']) == playerName:
            target_player = player
            break

    if target_player:
        # Extract player's attributes
        attributes = target_player['ratings'][-1]

        # Define attribute thresholds for strengths and weaknesses
        strength_threshold = 60
        weakness_threshold = 40

        # Analyze strengths and weaknesses
        strengths = []
        weaknesses = []
        map = {
            "hgt": "Height",
            "stre": "Strength",
            "spd": "Speed",
            "jmp": "Jump",
            "endu": "Endurance",
            "ins": "Inside Scoring",
            "dnk": "Dunking",
            "ft": "Free Throw",
            "fg": "Midrange",
            "tp": "Three Point",
            "diq": "Defensive IQ",
            "oiq": "Offensive IQ",
            "drb": "Dribbling",
            "pss": "Passing",
            "reb": "Rebounding"
        }
        for attr, value in attributes.items():
            if(attr == 'season'):
                break;
            if int(value) >= strength_threshold:
                strengths.append(map[attr])
            elif int(value) <= weakness_threshold:
                weaknesses.append(map[attr])

        strengthsStr = "";
        if(len(strengths) == 0):
            strengthsStr = "Nothing, dude is a BUM"
        for element in strengths:
            strengthsStr += element + "\n"

        weaknessesStr = "";
        for element in weaknesses:
            weaknessesStr += element + "\n"


        return (f"\n **Player's Strengths: ** \n {strengthsStr}" + f"\n **Player's Weakness's: ** \n {weaknessesStr}")
    else:
        return(f"{playerName} not found")

def filter_by_stat(stat, threshold):
    players = []
    s = 0
    if(threshold < 0 or threshold > 100):
        return("Invalid threshold, must be between 0 and 100")
    for player in data['players']:
        if(player['tid']  >= -1):
            attributes = player['ratings'][-1]
            for attr, value in attributes.items():
                if attr == stat:
                    s = value
            if int(s) >= int(threshold):
                players.append(player['firstName'] + " " + player['lastName'])
    playersStr = ""
    for i in range(len(players)):
        playersStr += players[i] + "\n"
    return (f'\n **Players with {stat} above {threshold}:** \n {playersStr}')



