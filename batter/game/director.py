from game.input_service import InputService
from time import sleep
from game import constants
import tkinter.messagebox

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        _cast (dictionary): The game actors {key: name, value: object}
        _script (dictionary): The game actions {key: tag, value: object}
    """

    def __init__(self, cast, script,game_state):
        """The class constructor.
        
        Args:
            cast (dict): The game actors {key: tag, value: list}.
            script (dict): The game actions {key: tag, value: list}.
            game_state: an instance of Game_State, used to handle the current_game state
        """

        self._cast = cast
        self._script = script
        self.game_state = game_state
    
    def start_game(self):
        """Starts the game loop to control the sequence of play."""
        while True:
            
            self._cue_action("input")
            self._cue_action("update")
            self._cue_action("output")
            sleep(constants.FRAME_LENGTH)
                

            if self.game_state.get_game_state() == "Game Over":
                final_score = self._cast["score label"][0].get_score()
                break
                
        print("-" * 10)
        print(f"Game Over! Your score was {final_score}")
        print("-" * 10)
                
            
        

    def _cue_action(self, tag):
        """Executes the actions with the given tag.
        
        Args:
            tag (string): The given tag.
        """ 
        for action in self._script[tag]:
            action.execute(self._cast)