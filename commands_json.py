import json

# Retrieve JSON data from the file
with open("2025 NBA Roster.json", "r") as file:
    data = json.load(file)

# Streamline Player Display & Finding
players = data["players"]
for player in players:
    if player['lastName'].find(' (PO)') != -1:
        player['lastName'] = player['lastName'].replace(' (PO)', '')
    if player['lastName'].find(' (TO)') != -1:
        player['lastName'] = player['lastName'].replace(' (TO)', '')

def allStars() -> str:
    # Access and process the retrieved JSON data
    try:
        allstars_east = data["allStars"][-1]["teams"][0]
    except:
        return "All Star Break has not occured yet!"

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

def playerStats(given_player) -> str:
    # Access and process the retrieved JSON data
    for player in players:
        if player["firstName"] + " " + player['lastName'] == given_player:
            if(not player['stats']):
                return "Player is a rookie! Has not played a game yet."
            try:
                playerData = player['stats'][-1]
                ppg = round((float(playerData['pts']) / playerData['gp']), 2)
                apg = round((float(playerData['ast']) / playerData['gp']), 2)
                rpg = round((float((playerData['orb'] + playerData['drb'])) / playerData['gp']), 2)
                spg = round((float(playerData['stl']) / playerData['gp']), 2)
                bpg = round((float(playerData['blk']) / playerData['gp']), 2)
                ewa = round(float(playerData['ewa']), 2)
                per = round(float(playerData['per']), 2)
                fg = round((100 * float(playerData['fg'] / playerData['fga'])), 2)
                tp = round((100 * float(playerData['tp'] / playerData['tpa'])), 2)
                statsStr = f'**Position: **' + player['pos'] + "\n" + \
                           f'**PPG: **' + str(ppg) + "\n" + \
                           f'**APG: **' + str(apg) + "\n" + \
                           f'**RPG: **' + str(rpg) + "\n" + \
                           f'**SPG: **' + str(spg) + "\n" + \
                           f'**BPG: **' + str(bpg) + "\n" + \
                           f'**EWA: **' + str(ewa) + "\n" + \
                           f'**PER: **' + str(per) + "\n" + \
                           f'**FG%: **' + str(fg) + "\n" + \
                           f'**3PT%: **' + str(tp) + "\n"
                return f'{statsStr}'
            except ZeroDivisionError:
                return "Has not played a game this season."


    return f'Player not found.'

def player_strength_and_weakness(playerName):
    # Find the player's data using the player_name
    target_player = None
    for player in players:
        if (player['firstName'] + " " + player['lastName']) == playerName:
            target_player = player
            break

    if target_player:
        # Extract player's attributes
        attributes = target_player['ratings'][-1]
        # Define attribute thresholds for strengths and weaknesses
        strength_threshold = 65
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
            if attr in map and int(value) >= strength_threshold:
                strengths.append(map[attr])
            elif attr in map and int(value) <= weakness_threshold:
                weaknesses.append(map[attr])

        strengthsStr = ""
        if(len(strengths) == 0):
            strengthsStr = "Nothing"
        for element in strengths:
            strengthsStr += element + "\n"

        weaknessesStr = ""
        if(len(weaknesses) == 0):
            weaknessesStr = "Nothing"
        for element in weaknesses:
            weaknessesStr += element + "\n"


        return (f"\n **Player's Strengths: ** \n {strengthsStr}" + f"\n **Player's Weaknesses: ** \n {weaknessesStr}")
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

def roster(team_name):
    roster = []
    teamMap = {
        "Atlanta Hawks": 0,
        "Boston Celtics": 1,
        "Brooklyn Nets": 2,
        "Charlotte Hornets": 3,
        "Chicago Bulls": 4,
        "Cleveland Cavaliers": 5,
        "Dallas Mavericks": 6,
        "Denver Nuggets": 7,
        "Detroit Pistons": 8,
        "Golden State Warriors": 9,
        "Houston Rockets": 10,
        "Indiana Pacers": 11,
        "Los Angeles Clippers": 12,
        "Los Angeles Lakers": 13,
        "Memphis Grizzlies": 14,
        "Miami Heat": 15,
        "Milwaukee Bucks": 16,
        "Minnesota Timberwolves": 17,
        "New Orleans Pelicans": 18,
        "New York Knicks": 19,
        "Oklahoma City Thunder": 20,
        "Orlando Magic": 21,
        "Philadelphia 76ers": 22,
        "Phoenix Suns": 23,
        "Portland Trailblazers": 24,
        "Sacramento Kings": 25,
        "San Antonio Spurs": 26,
        "Toronto Raptors": 27,
        "Utah Jazz": 28,
        "Washington Wizards": 29
    }
    parts = team_name.split(" ")
    capitalized_name = " ".join([word.title() for word in parts])
    team_name = capitalized_name
    if team_name not in teamMap:
        return "Team not found. Must be in city/name format (ex: Washington Wizards)."
    for player in players:
        if player['tid'] == teamMap[team_name]:
            roster.append(player['firstName'] + " " + player['lastName'])
    rosterStr = ""
    count = 1
    for i in range(len(roster)):
        rosterStr += str(count) + ". " + roster[i] + "\n"
        count += 1
    return rosterStr



