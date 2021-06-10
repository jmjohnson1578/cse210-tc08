import random
import sys
import time
from game import constants
from game.action import Action
from game.point import Point
from asciimatics.event import KeyboardEvent


class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """
    def __init__(self,game_state):
        self.game_state = game_state



    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """

        if self.game_state.get_game_state():
            cast["mid game label"][0].set_text("")
            
        paddle_coords = []
        paddle_x = cast["paddle"][0].get_position().get_x()
        for x in range(paddle_x,paddle_x + 12):
            paddle_coords.append(x)

        
        #score label = cast["score label"][0] # there's only one
        paddle = cast["paddle"][0] # there's only one
        ball = cast["ball"][0]
        ball_x = ball.get_position().get_x()
        ball_y = ball.get_position().get_y()
        
       
        paddle_position = paddle.get_position()
        paddle_x = paddle_position.get_x()
        paddle_y = paddle_position.get_y()


        #Paddle impact
        if ball_y == 18:
            if ball_x in paddle_coords:
                ball_velocity = ball.get_velocity()
                ball_x = ball_velocity.get_x()
                ball_y = ball_velocity.get_y()
                new_ball_y = ball_y - 2 
                ball.set_velocity(Point(ball_x,new_ball_y))


        #Hitting the top wall
        if ball.get_position().get_y() == 1:

            ball_velocity = ball.get_velocity()
            ball_x = ball_velocity.get_x()
            ball_y = ball_velocity.get_y()
            new_ball_y = - ball_y 
            ball.set_velocity(Point(ball_x,new_ball_y))

        #Hitting the bottom wall
        if ball.get_position().get_y() == constants.MAX_Y - 1:
            if cast["lives label"][0].get_lives() > 0:
                cast["lives label"][0].update_lives(-1)
                cast["mid game label"][0].set_text("Press the space bar to continue")
                ball.set_position(Point(40,18))
                cast["paddle"][0].set_position(Point(35,19))
                self.game_state.set_game_state(False)
                
            else:
                self.game_state.set_game_state("Game Over")

        #Hitting the left wall
        if ball.get_position().get_x() == 1:
            ball_velocity = ball.get_velocity()
            new_ball_x = ball_velocity.get_x() + 2
            ball_y = ball_velocity.get_y()
        
            ball.set_velocity(Point(new_ball_x,ball_y))

        #Hitting the right wall
        if ball.get_position().get_x() == constants.MAX_X - 1:
            ball_velocity = ball.get_velocity()
            new_ball_x = - ball_velocity.get_x()
            ball_y = ball_velocity.get_y()
            ball.set_velocity(Point(new_ball_x,ball_y))

        #Brick impact
        for brick in cast["brick"]:

            brick_x = brick.get_position().get_x()
            brick_y = brick.get_position().get_y()

            if ball.get_position().get_x() == brick_x:
                if ball.get_position().get_y() == brick_y:
                    ball_velocity = ball.get_velocity()
                    ball_x = ball_velocity.get_x()
                    ball_y = ball_velocity.get_y()
                    new_ball_y = -ball_y 
                    ball.set_velocity(Point(ball_x,new_ball_y))
                    
                    cast["brick"].pop(cast["brick"].index(brick))
                    cast["score label"][0].update_score(1)
                
                  