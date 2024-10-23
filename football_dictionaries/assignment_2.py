def players_by_position(squads_list):
    grouped = {}
    for player in squads_list:
        position = player['position']
        if position not in grouped:
            grouped[position] = []
        grouped[position].append(player)
    return grouped

# Example usage
players_dicts = lists_to_dicts(SQUADS_DATA)
grouped_by_position = players_by_position(players_dicts)
print(grouped_by_position)
