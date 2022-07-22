class Cast:
    """
    A collection of actors.
    """

    def __init__(self):
        """
        Constructs a new Actor.
        """
        self._players = {}

    def add_player(self, group, player):
        """
        Adds an actor to the given group.

        Args:
            group: A string containing the name of the group.
            actor: The instance of Actor (or a subclass) to add.
        """
        if group not in self._players.keys():
            self._players[group] = []
        self._players[group].append(player)

    def clear_players(self, group):
        """
        Clears players from the given group.

        Args:
            group: A string containing the name of the group.
        """
        if group in self._players:
            self._players[group] = []

    def clear_all_players(self):
        """
        Clears all actors.
        """
        for group in self._players:
            self._players[group] = []

    def get_players(self, group):
        """
        Gets the players in the given group.

        Args:   
            group: A string containing the name of the group.

        Returns:
            A list of Player instances.
        """
        results = []
        if group in self._players.keys():
            results = self._players[group].copy()
        return results

    def get_all_players(self):
        """
        Gets all of the players in the cast.

        Returns:
            A list of player instances.
        """
        results = []
        for group in self._players:
            results.extend(self._players[group])
        return results

    def get_first_player(self, group):
        """
        Gets the first player in the given group.

        Args:
            group: A string containing the name of the group.

        Returns:
            An instance of Player.
        """
        result = None
        if group in self._players.keys():
            result = self._players[group][0]
        return result

    def remove_player(self, group, player):
        """
        Removes an player from the given group.

        Args:
            group: A string containing the name of the group.
            actor: The instance of Actor (or a subclass) to remove.
        """
        if group in self._players:
            self._players[group].remove(player)