from sys import exit
from random import randint
from textwrap import dedent

class Scene:
    def enter(self):
        print("This scene is not yet configured.")
        exit(1)

class Engine:
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Death(Scene):
    def enter(self):
        print("You died. Game over!")
        exit(1)

class CentralCorridor(Scene):
    def enter(self):
        print(dedent("""
        The Gothons of Planet Percal #25 have invaded your ship and
        destroyed your entire crew. You are the last surviving member.
        """))

        action = input("> ")

        if action == "shoot!":
            print("You missed. The Gothon kills you.")
            return 'death'
        elif action == "dodge!":
            print("You slipped and hit your head. You die.")
            return 'death'
        elif action == "tell a joke":
            print("The Gothon laughs, allowing you to escape.")
            return 'laser_weapon_armory'
        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'

class LaserWeaponArmory(Scene):
    def enter(self):
        print("You enter the Armory and find a neutron bomb.")

        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZZEDDD!")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print("You got the bomb! Head to the bridge.")
            return 'the_bridge'
        else:
            print("The lock closes forever. You die.")
            return 'death'

class TheBridge(Scene):
    def enter(self):
        print("You reach the bridge with the bomb.")

        action = input("> ")

        if action == "throw the bomb":
            print("You panic and throw the bomb. It explodes.")
            return 'death'
        elif action == "slowly place the bomb":
            print("You place the bomb and escape.")
            return 'escape_pod'
        else:
            print("DOES NOT COMPUTE!")
            return 'the_bridge'

class EscapePod(Scene):
    def enter(self):
        print("You reach the escape pods. Choose one.")

        good_pod = randint(1,5)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print("Wrong pod. You die.")
            return 'death'
        else:
            print("You escape successfully. You win!")
            return 'finished'

class Finished(Scene):
    def enter(self):
        print("You won! Good job.")
        return 'finished'

class Map:
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return self.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
