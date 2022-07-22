from constants import *
from game.scripting.action import Action


class CheckOverAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        bricks = cast.get_players(BRICK_GROUP)
        if len(bricks) == 0:
            stats = cast.get_first_player(STATS_GROUP)
            stats.next_level()
            callback.on_next(NEXT_LEVEL)