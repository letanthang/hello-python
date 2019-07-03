class Car:
    pass


class Vehicle:
    def __init__(self, number_of_wheels, type_of_tank, seating_capacity):
        self.number_of_wheels = number_of_wheels
        self.type_of_tank = type_of_tank
        self.seating_capacity = seating_capacity

    def set_number_of_wheels(self, number):
        self.number_of_wheels = number


tesla_model_s = Vehicle(4, 'electric', 5)
print(tesla_model_s.type_of_tank)
tesla_model_s.set_number_of_wheels(10)
print(tesla_model_s.number_of_wheels)
