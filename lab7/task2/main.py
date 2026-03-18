# main.py
from models import Vehicle, Car, Motorcycle

def main():
    # Create objects
    v1 = Vehicle("Toyota", "Corolla", 2020)
    c1 = Car("BMW", "X5", 2022, 4)
    m1 = Motorcycle("Yamaha", "R1", 2021, 1000)

    vehicles = [v1, c1, m1]

    for v in vehicles:
        print(v)  
        print(v.start_engine())  
        print(v.stop_engine())

        # Call child-specific methods safely
        if isinstance(v, Car):
            print(v.honk())
        elif isinstance(v, Motorcycle):
            print(v.wheelie())

        print("-" * 40)


if __name__ == "__main__":
    main()
