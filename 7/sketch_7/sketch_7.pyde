from abc import ABCMeta, abstractmethod
class Pet():
    __metaclass__=ABCMeta
    @abstractmethod
    def speak(self):
        super().__init__()
        return 'no sound'
class Cat(Pet):
    def __init__(self, name):
        self.name = name
    def speak(self):
        text('meow', random(60, width-60), random(50, height-50))
        return 'meow'
class Dog(Pet):
    def __init__(self, name):
        self.name = name
    def speak(self):
        text('woof', random(50, width-70), random(50, height-50))
        return 'woof'
    def gimmePaw(self):
        image(loadImage("lapa.png"), random(50, width-70), random(50, height-100))
    def __add__(self, other):
        return self.name[0]+ ' i ' + other.name[0]
class Bird(Pet):
    def __init__(self, name):
        self.name = name
    def speak(self):
        text('tweet', random(50, width-70), random(50, height-50))
        return 'tweet'
    def __sub__(self, other):
        return 'none'
    
def setup():
    size(400,400)
    textSize(20)
    rex = Dog('Rex')
    benio = Dog('Benio')
    skrypcik = Cat('Skrypcik')
    felek = Bird('Felek')
    kolo = Bird('Kolo')
    global list_of_pets
    list_of_pets = [rex, benio, skrypcik, felek, kolo]
    print(isinstance(skrypcik, Pet))
    print(rex+benio)
    print(felek-kolo)

def draw():
    pass
    
def mouseClicked():
    for pet in list_of_pets:
        pet.speak()
        if isinstance(pet, Dog):
            pet.gimmePaw()
            
# 1,75pkt
