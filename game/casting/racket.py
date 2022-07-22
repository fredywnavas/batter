from constants import *
from game.casting.player import Player
from game.casting.point import Point


class Racket(Player):
    """
    An implement used to hit and bounce the ball in the game.
    """

    def __init__(self, body, animation, debug = False):
        """
        Constructs a new Bat.

        Args:
            body        : A new instance of Body
            aninmation  : A new instance of Animation
            debug       : If it s being debugged.
        """
        super().__init__(debug)
        self._body = body
        self._animation = animation

    def get_animation(self):
        """
        Get the bat's animation.

        Returns:
            An instance of Animation.
        """
        return self._animation

    def get_body(self):
        """
        Gets the bat's body.

        Returns:
            An instance of Body.
        """
        return self._body
    
    def move_next(self):
        """
        Moves the bat using its velocity.
        """
        position = self._body.get_postion()
        velocity = self._body.get_velocity()
        new_position = position.add(velocity)
        self._body.set_position(new_position)

    def swing_left(self):
        """
        Steers the bat to the left.
        """
        velocity = Point(-RACKET_VELOCITY, 0)
        self._body.set_velocity(velocity)

    def swing_right(self):
        """
        Steers the bat to the right.
        """
        velocity = Point(RACKET_VELOCITY, 0)
        self._body.set_velocity(velocity)

    def stop_moving(self):
        """
        Stops the bat from moving.
        """
        velocity = Point(0, 0)
        self._body.set_velocity(velocity)