# Base class for vehicles
class Vehicle:
    def move(self):
        """Generic move method, can be overridden in subclasses."""
        print("Vehicle is moving")

# Derived class for Car
class Car(Vehicle):
    def move(self):
        """Overrides the move method to represent a car's movement."""
        print("Driving 🚗")

# Derived class for Plane
class Plane(Vehicle):
    def move(self):
        """Overrides the move method to represent a plane's movement."""
        print("Flying ✈️")

# Derived class for Boat
class Boat(Vehicle):
    def move(self):
        """Overrides the move method to represent a boat's movement."""
        print("Sailing ⛵")

# Function to demonstrate polymorphism
def demonstrate_polymorphism():
    # Create instances of different vehicles
    car = Car()
    plane = Plane()
    boat = Boat()
    
    # Call the same method move() on different objects
    vehicles = [car, plane, boat]
    for vehicle in vehicles:
        vehicle.move()

# Run the demonstration
if __name__ == "__main__":
    demonstrate_polymorphism()
