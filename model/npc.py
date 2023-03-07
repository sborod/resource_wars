from model.character import Character

class NPC(Character):
    def __init__(self, name, level, health, max_health, strength, evasion, speed, armor, position, dialogue):
        super().__init__(name, level, health, max_health, strength, evasion, speed, armor, position)
        self.dialogue = dialogue
