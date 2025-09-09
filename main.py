# main.py - Controller file to run both assignments
from superhero import demonstrate_superheroes
from animals import demonstrate_polymorphism

def main():
    """Main function to run both assignments"""
    print("🎓 PYTHON OOP ASSIGNMENTS")
    print("=" * 50)
    
    # Run Assignment 1: Superhero Class Design
    demonstrate_superheroes()
    
    print("\n" + "=" * 50)
    
    # Run Assignment 2: Polymorphism Challenge
    demonstrate_polymorphism()
    
    print("\n✅ Both assignments completed successfully!")

if __name__ == "__main__":
    main()
