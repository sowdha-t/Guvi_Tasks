"""
Problem Statement 3:
Create a base class vehicle with attributes like model, rental rate  and a method calculate rent.
Inherit from this class to create subclass Car, Bike and Truck. Each subclass should have specific attributes
and calculations for rental rates. Implement polymorphism to calculate the rental cost of different vehicles
based on their type and rental duration
"""

#Base Class

class Vehicle:

    def __init__(self, model, rental_rate_per_day):
        self.model = model
        self.rental_rate_per_day = rental_rate_per_day

    def calculate_rent(self, days):
        return self.rental_rate_per_day * days

    def display_info(self):
        print(f"Model: {self.model}")
        print(f"Base Rate/Day: ₹{self.rental_rate_per_day}")


class Car(Vehicle):
    RATE_PER_DAY = 1500  # fixed rate for all cars

    def __init__(self, model, has_ac=True):
        super().__init__(model, self.RATE_PER_DAY)
        self.has_ac = has_ac

    def calculate_rent(self, days):
        rent = self.rental_rate_per_day * days
        if self.has_ac:
            rent += 200 * days
        return rent


class Bike(Vehicle):
    RATE_PER_DAY = 500  # fixed rate for all bikes

    def __init__(self, model, has_helmet_included=True):
        super().__init__(model, self.RATE_PER_DAY)
        self.has_helmet_included = has_helmet_included

    def calculate_rent(self, days):
        rent = self.rental_rate_per_day * days
        if not self.has_helmet_included:
            rent += 50

        return rent


class Truck(Vehicle):
    RATE_PER_DAY = 2500  # fixed rate for all trucks

    def __init__(self, model, load_capacity_tons):
        super().__init__(model, self.RATE_PER_DAY)
        self.load_capacity_tons = load_capacity_tons

    def calculate_rent(self, days):
        rent = self.rental_rate_per_day * days
        rent += self.load_capacity_tons * 300 * days
        return rent


def print_rental_cost(vehicle, days):
    vehicle.display_info()
    cost = vehicle.calculate_rent(days)
    print(f"Rental Duration: {days} day(s)")
    print(f"Total Rent: Rs.{cost:.2f}")
    print("-" * 30)

vehicles = [
        Car("Honda City", has_ac=True),
        Bike("Royal Enfield", has_helmet_included=False),
        Truck("Tata Ace", load_capacity_tons=1.5),
    ]

for v in vehicles:
    print_rental_cost(v, days=8)