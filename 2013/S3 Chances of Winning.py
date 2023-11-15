# https://dmoj.ca/problem/ccc13s3
import itertools

favourite_team = int(input())
games_played = int(input())

# games[0] = result of team 1 vs 2
# games[1] = result of team 1 vs 3
# games[2] = result of team 1 vs 4
# games[3] = result of team 2 vs 3
# games[4] = result of team 2 vs 4
# games[5] = result of team 3 vs 4
# W for win, L for lose, T for tie, from the perspective of team on left of each vs

def team_to_index(team_a, team_b):
    # given two teams, return the index in the games array
    if {team_a, team_b} == {1, 2}:
        return 0
    elif {team_a, team_b} == {1, 3}:
        return 1
    elif {team_a, team_b} == {1, 4}:
        return 2
    elif {team_a, team_b} == {2, 3}:
        return 3
    elif {team_a, team_b} == {2, 4}:
        return 4
    elif {team_a, team_b} == {3, 4}:
        return 5

games = ["", "", "", "", "", ""]
missing_indexes = [0, 1, 2, 3, 4, 5]

for _ in range(games_played):
    team_a, team_b, a_score, b_score = list(map(int, input().split()))

    index = team_to_index(team_a, team_b)
    if a_score > b_score:
        games[index] = "W"
    elif a_score < b_score:
        games[index] = "L"
    else:
        games[index] = "T"
    missing_indexes.remove(index)


# Now loop through every possible combination of wins, losses, and ties, and see in how many combinations the team wins
possible_results = []
for _ in range(6 - games_played):
    possible_results.append("W")
    possible_results.append("L")
    possible_results.append("T")

possible_games = set(itertools.permutations(possible_results, 6 - games_played))  # every possible combination of missing games

winning_scenarios = 0

for possible_game in possible_games:
    possible_game_results = games[:]  # copy

    # filling in the missing games
    for i in range(6 - games_played):
        possible_game_results[missing_indexes[i]] = possible_game[i]

    # Now manually calculate scores
    scores = [0, 0, 0, 0]

    if possible_game_results[0] == "W":
        scores[0] += 3
    elif possible_game_results[0] == "L":
        scores[1] += 3
    elif possible_game_results[0] == "T":
        scores[0] += 1
        scores[1] += 1

    if possible_game_results[1] == "W":
        scores[0] += 3
    elif possible_game_results[1] == "L":
        scores[2] += 3
    elif possible_game_results[1] == "T":
        scores[0] += 1
        scores[2] += 1

    if possible_game_results[2] == "W":
        scores[0] += 3
    elif possible_game_results[2] == "L":
        scores[3] += 3
    elif possible_game_results[2] == "T":
        scores[0] += 1
        scores[3] += 1

    if possible_game_results[3] == "W":
        scores[1] += 3
    elif possible_game_results[3] == "L":
        scores[2] += 3
    elif possible_game_results[3] == "T":
        scores[1] += 1
        scores[2] += 1

    if possible_game_results[4] == "W":
        scores[1] += 3
    elif possible_game_results[4] == "L":
        scores[3] += 3
    elif possible_game_results[4] == "T":
        scores[1] += 1
        scores[3] += 1

    if possible_game_results[5] == "W":
        scores[2] += 3
    elif possible_game_results[5] == "L":
        scores[3] += 3
    elif possible_game_results[5] == "T":
        scores[2] += 1
        scores[3] += 1

    # check if it has the highest score
    highest = True
    for i in range(len(scores)):
        if i != favourite_team - 1:
            if scores[i] >= scores[favourite_team - 1]:
                highest = False

    if highest:
        winning_scenarios += 1

print(winning_scenarios)


"""
3
4
1 3 5 7
3 4 8 0
2 4 2 2
1 2 5 5
"""
