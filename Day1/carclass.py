# author Paul Upendo
class Car(object):
    name = 'General'
    model = 'GM'
    car_type = ''
    num_of_doors = 4
    num_of_wheels = 4
    speed = 0

    def __init__(self, name='General', model='GM', car_type=None):  # Definition of class car arguments
        self.name = name
        self.model = model
        self.car_type = car_type
        self.test_properties()

    def test_properties(self):
        if self.name == 'Porshe' or self.name == 'Koenigsegg':  # condition to check number of doors
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4

        if self.car_type == 'trailer':  # condition to check number of wheels
            self.num_of_wheels = 8

    def is_saloon(self):
        if self.car_type != 'Trailer':  # condition to check car type
            self.car_type = 'Saloon'

        return self.car_type

    def drive(self, speed):  # function to calculate different car type speeds. Is instance of car class
        if self.car_type == 'trailer':
            self.speed = 77
        else:
            self.speed = pow(10, speed)
        return speed
