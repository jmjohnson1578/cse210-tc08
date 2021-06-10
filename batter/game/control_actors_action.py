from game import constants
import game
from game.action import Action

class ControlActorsAction(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def __init__(self, input_service,game_state):
        """The class constructor.
        
        Args:
            input_service (InputService): An instance of InputService.
        """
        self._input_service = input_service
        self.game_state = game_state

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        direction = self._input_service.get_direction()
        paddle = cast["paddle"][0] # there's only one in the cast
        ball = cast["ball"][0]
        paddle.set_velocity(direction)
        if not self.game_state.get_game_state():
            ball.set_velocity(direction)              
