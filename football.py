n = int(input())
results = {}

for i in range(n):
    match = input().split(';')
    team_1 = match[0]
    score_1 = int(match[1])
    if team_1 not in results:
        results[team_1] = [0 for i in range(5)]
    results[team_1][0] += 1
    team_2 = match[2]
    score_2 = int(match[3])
    if team_2 not in results:
        results[team_2] = [0 for i in range(5)]
    results[team_2][0] += 1
    if score_1 == score_2:
        results[team_1][2] += 1
        results[team_1][4] += 1
        results[team_2][2] += 1
        results[team_2][4] += 1
    elif score_1 > score_2:
        results[team_1][1] += 1
        results[team_1][4] += 3
        results[team_2][3] += 1
    else:
        results[team_1][3] += 1
        results[team_2][1] += 1
        results[team_2][4] += 3

for team in results:
    print(team, end=':')
    print(' '.join([str(result) for result in results[team]]))