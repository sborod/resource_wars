class GameObjectView:
    def __init__(self, game_object):
        self.game_object = game_object

    def get_position(self):
        return self.game_object.get_position()
