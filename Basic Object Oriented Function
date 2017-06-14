# A simple guessing game where the player has to guess a number and loses a life if they guess wrong

class Player():  # 1) Code starts here with the player class being placed and initiated below
    def __init__(self, number, lives):
        self.number = number # 3)the numbers are then assigned to the object self as attributes of self
        self.lives = lives
 
    def guess(self,n): # 4) then the guess function is run
        if self.lives < 1: # 5) in this case there are 2 lives so this if clause is skipped
            raise ValueError("")   
        elif n != self.number: # 6) the numbers are equal so this also evaluates to false and no lives are removed
            self.lives -= 1
            return False
        elif n == self.number: # 7) finally this clause evaluates to true and True is returned!
            return True
      
play = Player(10, 2)  # 2) The player is then given a number - 10 and 2 lives in this instance assigned to object play.
play.guess(10)        #    The guess of 10 is then played which is obviously correct!
