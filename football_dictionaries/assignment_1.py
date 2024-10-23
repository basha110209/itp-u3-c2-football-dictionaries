def players_as_dictionaries(squads_list):
    pass
    
def lists_to_dicts(players):
    keys = ['number', 'position', 'name', 'date_of_birth', 'caps', 'club', 'country', 'club_country', 'year']
    return [dict(zip(keys, player)) for player in squads_list]

# Example usage
SQUADS_DATA = [
    ["1", "GK", "Juan Botasso", "(1908-10-23)23 October 1908 (aged 21)", "", "Quilmes", "Argentina", "Argentina", "1930"],
    ["9", "FW", "Roberto Cherro", "(1907-02-23)23 February 1907 (aged 23)", "", "Boca Juniors", "Argentina", "Argentina", "1930"]
]

players_dicts = players_as_dictionaries(SQUADS_DATA)
print(players_dicts)
