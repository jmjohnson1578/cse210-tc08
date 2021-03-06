from game.point import Point
import random
class Game_State:
    
    """A class to handle the current state of the game. 
    Specifically when the user loses a life and the game is paused momentarily
    
    Responibility: Information Holder
    
    Attributes:
        cast (dictionary): The game actors {key: name, value: object}
    
    """

    def __init__(self,cast):
        self._current_state = True
        self.cast = cast
    
    def get_game_state(self):
        return self._current_state

    def set_game_state(self,state):
        self._current_state = state
        ball = self.cast["ball"][0]
        if state:
            random_velocity_index = random.randint(0,1)
            random_velocities = [-1,1]
            random_velocity = random_velocities[random_velocity_index]

            ball.set_velocity(Point(random_velocity,-1))

        else:
            ball.set_velocity(Point(0,0))
