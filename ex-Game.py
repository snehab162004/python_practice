class Scene:
    def enter(self):
        pass

class Introduction(Scene):
    def enter(self):
        print("Welcome to the adventure!")
        return 'challenge'

class Challenge(Scene):
    def enter(self):
        choice = input("Solve the riddle (yes/no): ")
        if choice == "yes":
            print("You solved it!")
            return 'win'
        else:
            print("You failed!")
            return 'lose'

class Win(Scene):
    def enter(self):
        print("You won the game!")
        return 'end'

class Lose(Scene):
    def enter(self):
        print("Game over!")
        return 'end'

class Map:
    scenes = {
        'intro': Introduction(),
        'challenge': Challenge(),
        'win': Win(),
        'lose': Lose()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return self.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)

class Engine:
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            next_scene_name = current_scene.enter()
            if next_scene_name == 'end':
                break
            current_scene = self.scene_map.next_scene(next_scene_name)

game_map = Map('intro')
game_engine = Engine(game_map)
game_engine.play()
