def tally(rows):
    match_teams = {}
    matches = [row.split(';') for row in rows]
    for (team1, team2, result) in matches:
        for team in [team1, team2]:
            if team not in match_teams:
                match_teams[team]={'W': 0, 'L': 0, 'D': 0, 'P': 0, 'MP': 0}
        if result == 'win':
            match_teams[team1]["W"]+=1
            match_teams[team2]["L"]+=1
            match_teams[team1]["P"]+=3
            match_teams[team1]["MP"]+=1
            match_teams[team2]["MP"]+=1  
        elif result == 'loss':
            match_teams[team2]["W"]+=1
            match_teams[team1]["L"]+=1
            match_teams[team2]["P"]+=3
            match_teams[team1]["MP"]+=1
            match_teams[team2]["MP"]+=1
        elif result == 'draw':
            match_teams[team1]["D"]+=1
            match_teams[team2]["D"]+=1
            match_teams[team1]["P"]+=1
            match_teams[team2]["P"]+=1
            match_teams[team2]["MP"]+=1
            match_teams[team1]["MP"]+=1     
    sort_match_teams=sorted(list(match_teams.items()),key=lambda x:x[0])
    sort_match_teams=sorted(sort_match_teams,key=lambda x: x[1]['P'], reverse=True)
    result_table = ["Team                           | MP |  W |  D |  L |  P"]
    for key, value in sort_match_teams:
        result_table.append(f'{key:<31}| {value["MP"]:>2d} | {value["W"]:>2d} | {value["D"]:>2d} | {value["L"]:>2d} | {value["P"]:>2d}')
    return result_table    
 
