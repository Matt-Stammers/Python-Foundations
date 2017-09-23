# this creates a simple game which cycles through various moves:

health = 100
position = 0
coins = 0

def main():
    roll_dice()
    move()
    combat()
    get_coins()
    buy_health()
    print_status()
    
# as a list expression

health = 100
position = 0
coins = 0

def main():
  [phase() for phase in[roll_dice, move, combat, get_coins, buy_health, print_status]]
