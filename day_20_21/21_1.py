class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")



class Fish(Animal):
# How the Fish Class inherits everything that the Animal Class are available -> class Fish(Animal)

    def __ini__(self):
        super().__init__()

    def breathe(self):
        # if you want to make the same method like the one in super class or modify it of add some other thing in it,
        super().breathe()
        print("doing this underwater")
        
    def swim(self):
        print("moving in water")

nemo = Fish()
nemo.swim() # moving in water
nemo.breathe() # Inhale, exhale.
# Inhale, exhale.
# doing this underwater
print(nemo.num_eyes) # 2