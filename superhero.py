# superhero.py
class Superhero:
    """Base class for all superheroes"""
    
    def __init__(self, name, secret_identity, power_level, city):
        self.name = name
        self.secret_identity = secret_identity
        self.power_level = power_level
        self.city = city
        self.energy = 100
        self.is_hero = True
    
    def use_power(self, power_name, energy_cost=10):
        """Use a superhero power"""
        if self.energy >= energy_cost:
            self.energy -= energy_cost
            return f"{self.name} uses {power_name}! Energy: {self.energy}%"
        else:
            return f"{self.name} is too tired to use {power_name}! Need to rest."
    
    def rest(self):
        """Rest to regain energy"""
        self.energy = min(100, self.energy + 30)
        return f"{self.name} rests. Energy: {self.energy}%"
    
    def introduce(self):
        """Introduce the superhero"""
        return f"I am {self.name}, protector of {self.city}! My secret identity is {self.secret_identity}."
    
    def __str__(self):
        return f"{self.name} (Power: {self.power_level}, Energy: {self.energy}%)"


# Inheritance layer - Different types of superheroes
class FlyingSuperhero(Superhero):
    """A superhero with flying abilities"""
    
    def __init__(self, name, secret_identity, power_level, city, max_altitude):
        super().__init__(name, secret_identity, power_level, city)
        self.max_altitude = max_altitude
        self.is_flying = False
    
    def fly(self, altitude):
        """Fly to a certain altitude"""
        if altitude <= self.max_altitude:
            if self.energy >= 15:
                self.energy -= 15
                self.is_flying = True
                return f"{self.name} flies to {altitude} meters! Energy: {self.energy}%"
            else:
                return f"{self.name} is too tired to fly!"
        else:
            return f"{self.name} can't fly that high! Max altitude: {self.max_altitude}m"
    
    def land(self):
        """Land from flying"""
        self.is_flying = False
        return f"{self.name} lands safely."


class TechSuperhero(Superhero):
    """A superhero who uses technology"""
    
    def __init__(self, name, secret_identity, power_level, city, gadgets):
        super().__init__(name, secret_identity, power_level, city)
        self.gadgets = gadgets
        self.active_gadget = None
    
    def use_gadget(self, gadget_name):
        """Use a specific gadget"""
        if gadget_name in self.gadgets:
            if self.energy >= 8:
                self.energy -= 8
                self.active_gadget = gadget_name
                return f"{self.name} uses {gadget_name}! Energy: {self.energy}%"
            else:
                return f"{self.name} is too tired to use gadgets!"
        else:
            return f"{self.name} doesn't have {gadget_name} gadget."


def demonstrate_superheroes():
    """Demonstrate superhero classes - Assignment 1"""
    print("🦸‍♂️ SUPERHERO DEMONSTRATION 🦸‍♀️")
    print("=" * 50)
    
    # Create different types of superheroes
    superman = FlyingSuperhero("Superman", "Clark Kent", 95, "Metropolis", 10000)
    iron_man = TechSuperhero("Iron Man", "Tony Stark", 90, "New York", 
                           ["Repulsor Beams", "Arc Reactor", "Jarvis AI"])
    wonder_woman = Superhero("Wonder Woman", "Diana Prince", 92, "Themyscira")
    
    # Demonstrate their abilities
    heroes = [superman, iron_man, wonder_woman]
    
    for hero in heroes:
        print(hero.introduce())
        if isinstance(hero, FlyingSuperhero):
            print(hero.fly(5000))
            print(hero.land())
        elif isinstance(hero, TechSuperhero):
            print(hero.use_gadget("Repulsor Beams"))
        print(hero.use_power("Super Strength", 20))
        print(hero.rest())
        print("-" * 40)


# Run this file independently if needed
if __name__ == "__main__":
    demonstrate_superheroes()