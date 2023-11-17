from sportsipy.nba.teams import Teams

teams = Teams()
for team in teams:
    print(team.name, team.abbreviation)