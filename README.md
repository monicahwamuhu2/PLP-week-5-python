H
# Python Class Projects 📱✈️🚗

This repository contains two Python projects that explore object-oriented programming concepts including classes, inheritance, polymorphism, and encapsulation.

## Project 1: Smartphone Class 📱

This project demonstrates the creation of a `Smartphone` class with attributes, methods, and inheritance. It includes a `GamingSmartphone` class that extends the base class and overrides methods to add unique functionality.

### Features:
- **Smartphone Class**:
  - Stores basic smartphone information (brand, model, price).
  - Allows for applying a discount on the price.
  - Uses encapsulation to protect the `brand` attribute.

- **GamingSmartphone Class**:
  - Inherits from `Smartphone` and adds new attributes for gaming features like GPU and refresh rate.
  - Overrides the `display_info()` method to show additional details.
  - Includes a method to enhance performance by overclocking the GPU.

### Example Usage:
```python
# Creating a basic smartphone
phone1 = Smartphone("Apple", "iPhone 14", 999)
print(phone1.display_info())

# Creating a gaming smartphone
gaming_phone = GamingSmartphone("Asus", "ROG Phone 7", 1199, "Adreno 740", 144)
print(gaming_phone.display_info())
```

---

## Project 2: Polymorphism Challenge 🎭

This project demonstrates **polymorphism** in Python by creating different vehicle classes (`Car`, `Plane`, and `Boat`) that all have the same method `move()`, but each implements it differently.

### Features:
- **Vehicle Class**:
  - A generic base class with a `move()` method.
  
- **Car Class**:
  - Overrides `move()` to print "Driving 🚗".

- **Plane Class**:
  - Overrides `move()` to print "Flying ✈️".

- **Boat Class**:
  - Overrides `move()` to print "Sailing ⛵".

### Example Usage:
```python
# Creating vehicle objects
car = Car()
plane = Plane()
boat = Boat()

# Calling the move() method on each vehicle
car.move()   # Output: Driving 🚗
plane.move() # Output: Flying ✈️
boat.move()  # Output: Sailing ⛵
```

---

## How to Run the Projects

1. Clone or download the repository to your local machine.
2. Open the project directory in your terminal or IDE.
3. For each project, run the Python script:
   ```bash
   python smartphone_project.py  # For the Smartphone class project
   python polymorphism_project.py # For the Polymorphism Challenge project
   ```

## Requirements

- Python 3.x

---

## License

This project is open-source and available for personal use and modification.
```

