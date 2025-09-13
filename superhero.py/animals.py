# animals.py
class Animal:
    """Base class for all animals"""
    
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat
    
    def move(self):
        """Base move method - to be overridden by subclasses"""
        return f"{self.name} moves in some way."
    
    def speak(self):
        """Base speak method"""
        return f"{self.name} makes a sound."
    
    def __str__(self):
        return f"{self.name} from {self.habitat}"


# Different animal classes with polymorphic move() method
class Bird(Animal):
    def __init__(self, name, habitat, wingspan):
        super().__init__(name, habitat)
        self.wingspan = wingspan
    
    def move(self):
        return f"{self.name} is flying! 🕊️ Wingspan: {self.wingspan}cm"
    
    def speak(self):
        return f"{self.name} says: Tweet tweet! 🎵"


class Fish(Animal):
    def __init__(self, name, habitat, fin_type):
        super().__init__(name, habitat)
        self.fin_type = fin_type
    
    def move(self):
        return f"{self.name} is swimming! 🐟 Using {self.fin_type} fins"
    
    def speak(self):
        return f"{self.name} says: Blub blub! 💧"


class Mammal(Animal):
    def __init__(self, name, habitat, leg_count):
        super().__init__(name, habitat)
        self.leg_count = leg_count
    
    def move(self):
        if self.leg_count == 4:
            return f"{self.name} is running! 🐾 Using all {self.leg_count} legs"
        elif self.leg_count == 2:
            return f"{self.name} is walking upright! 🚶‍♂️"
        else:
            return f"{self.name} is moving strangely with {self.leg_count} legs"
    
    def speak(self):
        return f"{self.name} says: Grrr! 🐾"


class Snake(Animal):
    def __init__(self, name, habitat, length):
        super().__init__(name, habitat)
        self.length = length
    
    def move(self):
        return f"{self.name} is slithering! 🐍 Length: {self.length}cm"
    
    def speak(self):
        return f"{self.name} says: Hisss! 🐍"


def animal_parade(animals):
    """Demonstrate polymorphism with animal movements"""
    print("\n🐾 ANIMAL PARADE - POLYMORPHISM DEMONSTRATION 🐾")
    print("=" * 60)
    
    for animal in animals:
        print(f"{animal}")
        print(f"Movement: {animal.move()}")
        print(f"Sound: {animal.speak()}")
        print("-" * 40)


def demonstrate_polymorphism():
    """Demonstrate polymorphism - Assignment 2"""
    # Create different animals
    eagle = Bird("Bald Eagle", "Mountains", 200)
    goldfish = Fish("Goldfish", "Freshwater", "caudal")
    cheetah = Mammal("Cheetah", "Savannah", 4)
    human = Mammal("Human", "Various", 2)
    python_snake = Snake("Python", "Jungle", 300)
    
    # Put them in a list (polymorphism in action!)
    animals = [eagle, goldfish, cheetah, human, python_snake]
    
    # Demonstrate how they all have move() but behave differently
    animal_parade(animals)


# Run this file independently if needed
if __name__ == "__main__":
    demonstrate_polymorphism()