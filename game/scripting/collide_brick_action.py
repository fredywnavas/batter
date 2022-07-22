from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action

class CollideBrickAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service

    def execute(self, cast, script, callback):
        ball = cast.get_first_player(BALL_GROUP)
        bricks = cast.get_players(BRICK_GROUP)
        stats = cast.get_first_player(STATS_GROUP)

        for brick in bricks:
            ball_body = ball.get_body()
            brick_body = brick.get_body()

            if self._physics_service.has_collided(ball_body, brick_body):
                ball.bounce_y()
                sound = Sound(BOUNCE_SOUND)
                self._audio_service.play_sound(sound)
                points = brick.get_points()
                stats.add_points(points)
                cast.remove_player(BRICK_GROUP, brick)