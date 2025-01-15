# Base class
class Smartphone:
    def __init__(self, brand, model, price):
        self.__brand = brand  # Private attribute
        self.model = model
        self.price = price

    def display_info(self):
        """Displays the basic information about the smartphone."""
        return f"Brand: {self.__brand}, Model: {self.model}, Price: ${self.price:.2f}"

    def apply_discount(self, percentage):
        """Applies a discount to the price."""
        self.price -= self.price * (percentage / 100)
        return f"New price after {percentage}% discount: ${self.price:.2f}"

    # Getter for brand (to demonstrate encapsulation)
    def get_brand(self):
        return self.__brand

    # Setter for brand (to demonstrate encapsulation)
    def set_brand(self, brand):
        self.__brand = brand


# Derived class
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, price, gpu, refresh_rate):
        super().__init__(brand, model, price)  # Initialize base class attributes
        self.gpu = gpu
        self.refresh_rate = refresh_rate

    def display_info(self):
        """Overrides the base class method to add more details."""
        basic_info = super().display_info()  # Call the base class method
        return (
            f"{basic_info}, GPU: {self.gpu}, Refresh Rate: {self.refresh_rate}Hz"
        )

    def enhance_performance(self):
        """Enhances performance by overclocking the GPU."""
        return f"The GPU '{self.gpu}' has been overclocked for better gaming performance!"


# Demonstrating the classes
def main():
    # Creating an object of the base class
    phone1 = Smartphone("Apple", "iPhone 14", 999)
    print(phone1.display_info())
    print(phone1.apply_discount(10))
    print()

    # Creating an object of the derived class
    gaming_phone = GamingSmartphone("Asus", "ROG Phone 7", 1199, "Adreno 740", 144)
    print(gaming_phone.display_info())
    print(gaming_phone.enhance_performance())
    print()

    # Encapsulation example
    print("Original brand:", gaming_phone.get_brand())
    gaming_phone.set_brand("Asus Republic of Gamers")
    print("Updated brand:", gaming_phone.get_brand())


if __name__ == "__main__":
    main()
