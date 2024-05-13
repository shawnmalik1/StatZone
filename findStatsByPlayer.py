def findStatsForPlayer(data, given_player):
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