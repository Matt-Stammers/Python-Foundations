# This code works out what a player in an nba game would have scored had the played a full game given their minutes per game and score:

def nba_extrap(ppg, mpg):
    return round(48.0 / mpg * ppg, 1) if mpg > 0 else 0
    
# or
    
def nba_extrap(ppg, mpg):
    if mpg == 0: return 0
    return round(48.0 / mpg * ppg,1)
