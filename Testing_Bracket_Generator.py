def NewRoundIds( teams_in_tournament ):
    round_ids = []
    game_id = 0
    games_in_next_round = len(teams_in_tournament)/2 #need to count the number of teams_in_tournament list
    while games_in_next_round > 0:
        round_ids += [game_id]
        game_id += games_in_next_round
        games_in_next_round /= 2
        print(round_ids)
    return round_ids

NewRoundIds([1,2,3,4])
