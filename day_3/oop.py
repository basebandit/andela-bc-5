class Vehicle(object):
'''**kwargs refer to a dict.So this function expects a dictionary'''

    def __init__(self, engine_type, **kwargs):
        self.engine_type = engine_type
        for k, v in kwargs.items():
            setattr(self, k, v)

    def set_color(self, color):
        self.color = color

    def set_speed(self, speed):
        self.speed = speed

'''A car is a vehicle'''


class Car(Vehicle):
    def __init__(self, engine_type, car_category, **kwargs):
        super(Car, self).__init__(engine_type, **kwargs)
        self.car_category = car_category
        self.doors = 5
        self.wheels = 4


benz = Car("VTI-120", "saloon", engine_cc=1500, color='red', max_speed=120)
print benz.max_speed

