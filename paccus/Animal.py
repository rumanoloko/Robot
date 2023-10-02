from abc import ABC, abstractmethod

class Animal(ABC):

    def hablar (self):
        print("Soy un animal, no puedo hablar")

    def caminar (self):
        print("soy un animal y puedo caminar")


anim = Animal()
anim.hablar()
