# models.py
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        return f"{self.brand} {self.model}'s engine is starting."

    def stop_engine(self):
        return f"{self.brand} {self.model}'s engine is stopping."

    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"


# Child Class 1
class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors

    def start_engine(self):  # Overriding method
        return f"Car {self.brand} {self.model} starts with a key or button."

    def honk(self):
        return "Beep beep!"


# Child Class 2
class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, engine_capacity):
        super().__init__(brand, model, year)
        self.engine_capacity = engine_capacity

    def start_engine(self):  # Overriding method
        return f"Motorcycle {self.brand} {self.model} roars to life!"

    def wheelie(self):
        return "Doing a wheelie!"
