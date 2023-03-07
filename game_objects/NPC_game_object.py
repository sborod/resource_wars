from game_objects.character_game_object import CharacterGameObject

class NPCGameObject(CharacterGameObject):
    def __init__(self, npc):
        super().__init__(npc)
        self.dialogue_menu = None
