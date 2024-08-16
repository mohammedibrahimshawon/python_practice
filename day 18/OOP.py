class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.is_running = False

    def start_engine(self):
        if not self.is_running:
            self.is_running = True
            print(f"{self.year} {self.make} {self.model}'s engine started.")
        else:
            print(f"{self.year} {self.make} {self.model}'s engine is already running.")

    def stop_engine(self):
        if self.is_running:
            self.is_running = False
            print(f"{self.year} {self.make} {self.model}'s engine stopped.")
        else:
            print(f"{self.year} {self.make} {self.model}'s engine is not running.")

    def display_info(self):
        print(f"Car Information: {self.year} {self.make} {self.model}, Color: {self.color}")

# Creating an instance of the Car class
my_car = Car("Toyota", "Camry", 2021, "Blue")

# Using the methods of the Car class
my_car.display_info()
my_car.start_engine()
my_car.stop_engine()
