import random
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.control_actors_action import ControlActorsAction
from game.draw_actors_action import DrawActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.move_actors_action import MoveActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from game.game_state import Game_State
from asciimatics.screen import Screen 

def main(screen):

    # create the cast {key: tag, value: list}
    cast = {}

    #Creating label for current score
    score_label = Actor(score=0)
    score_label.set_text(f"Score: {score_label.score}")
    score_label_position = Point(5,constants.MAX_Y)
    score_label.set_position(score_label_position)
    score_label.set_color(2)
    cast["score label"] = [score_label]
    
    #Creating a label for current lives
    lives_label = Actor(lives = 5)
    lives_label.set_text(f"Lives: {lives_label.lives}")
    lives_label_position = Point(20,constants.MAX_Y)
    lives_label.set_position(lives_label_position)
    lives_label.set_color(3)
    cast["lives label"] = [lives_label]

    #Creating a mid-game label
    mid_game_label = Actor()
    mid_game_label_position = Point(25,10)
    mid_game_label.set_position(mid_game_label_position)
    cast["mid game label"] = [mid_game_label]

    x = int(constants.MAX_X / 2)
    y = int(constants.MAX_Y - 1)
    position = Point(x, y)
    paddle = Actor()
    paddle.set_text("===========")
    paddle.set_position(position)
    cast["paddle"] = [paddle]

    cast["brick"] = []
    for x in range(5, 75):
        for y in range(2, 6):
            position = Point(x, y)
            brick = Actor()
            brick.set_text("*")
            brick.set_position(position)
            brick.set_color(4)
            cast["brick"].append(brick)


    x = int(constants.MAX_X / 2)
    y = int(constants.MAX_Y / 2)
    position = Point(x, y)
    velocity = Point(1, -1)
    ball = Actor()
    ball.set_text("@")
    ball.set_position(position)
    ball.set_velocity(velocity)
    ball.set_color(1)
    cast["ball"] = [ball] 
    
    # create the script {key: tag, value: list}
    script = {}

    game_state = Game_State(cast)
    input_service = InputService(screen,game_state)
    output_service = OutputService(screen)
    control_actors_action = ControlActorsAction(input_service,game_state)
    move_actors_action = MoveActorsAction()
    handle_collisions_action = HandleCollisionsAction(game_state)
    draw_actors_action = DrawActorsAction(output_service,cast)
    
    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_collisions_action]
    script["output"] = [draw_actors_action]

    # start the game
    director = Director(cast, script,game_state)
    director.start_game()

Screen.wrapper(main)