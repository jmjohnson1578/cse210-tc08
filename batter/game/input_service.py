import game
import sys
from game.point import Point
from asciimatics.event import KeyboardEvent


class InputService:
    """Detects player input. The responsibility of the class of objects is to detect and communicate player keypresses.

    Stereotype: 
        Service Provider

    Attributes:
        _screen (Screen): An Asciimatics screen.
        _keys (list): Points for up, dn, lt, rt.
    """

    def __init__(self, screen,game_state):
        """The class constructor."""
        self.game_state = game_state

        self.space_bar_pressed = False
        self.current_game_state = True
        self._screen = screen
        self._keys = {}
        
        #Former version key mapping
        #self._keys[119] = Point(0, -1) # w
        #self._keys[115] = Point(0, 1) # s
        self._keys[97] = Point(-2, 0) # a
        self._keys[100] = Point(2, 0) # d

        self._keys[37] = Point(-1,0) #Left arrow key
        self._keys[39] = Point(1,0) #Right arrow key

        self._keys[32] = "space bar"
        
    def get_direction(self):
        """Gets the selected direction for the given player.

        Returns:
            Point: The selected direction.
        """
        direction = Point(0, 0)
        event = self._screen.get_event()
        if isinstance(event, KeyboardEvent):
            if event.key_code == 27:
                sys.exit()
            elif event.key_code != 32:
                direction = self._keys.get(event.key_code, Point(0, 0))
            if event.key_code == 32:
                if not self.game_state.get_game_state():
                    self.game_state.set_game_state(True)
                if self.game_state.get_game_state() == "Game over":
                    self.game_state.set_game_state("exit")
                    
        return direction

