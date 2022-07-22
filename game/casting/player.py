from game.casting.text import Text


class Player:
    """
    A participant in the game."""

    def __init__(self, debug = False):
        """Constructs a new Player using the given group and id.
        
        Args:
            group   : A string containing the player's group name.
            id      : A number that uniquely identifies the player within the group.
        """
        self._debug = debug

    def is_debug(self):
        """
        Whether or not the player is being debugged.
        
        Returns:
            True if the player is being debugged; False if otherwise.
        """
        return self._debug