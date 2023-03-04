class Renderer:
    def __init__(self):
        self.objects = []

    def set_objects(self, objects):
        self.objects = objects

    def render(self):
        for obj in self.objects:
            # Отображение объекта на экране
            pass