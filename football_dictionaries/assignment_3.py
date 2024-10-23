def players_by_country_and_position(squads_list):
    grouped = {}
    for player in squads_list:
        country = player['country']
        position = player['position']
        if country not in grouped:
            grouped[country] = {}
        if position not in grouped[country]:
            grouped[country][position] = []
        grouped[country][position].append(player)
    return grouped

# Example usage
players_dicts = lists_to_dicts(SQUADS_DATA)
grouped_by_country_and_position = players_by_country_and_position(players_dicts)
print(grouped_by_country_and_position)
