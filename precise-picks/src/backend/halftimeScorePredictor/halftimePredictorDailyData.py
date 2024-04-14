from nba_api.live.nba.endpoints import boxscore, scoreboard

board = scoreboard.ScoreBoard()
box = boxscore.BoxScore()
print(box.game.get_dict())