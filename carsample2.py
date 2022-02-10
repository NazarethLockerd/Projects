class Vehicle(object):

    def __init__(self, typ, make, engine, color, year, miles):
        self.typ = typ
        self.make = make
        self.engine = engine
        self.color = color
        self.year = year
        self.miles = miles

    def vehicle_print(self):
            print('Vehicle Type: ' + str(self.typ))
            print('Make: ' + str(self.make))
            print('Engine: ' + str(self.engine))
            print('Color: ' + str(self.color))
            print('Year: ' + str(self.year))
            print('Miles driven: ' + str(self.miles))


class GasVehicle(Vehicle):

    def __init__(self, fuel_tank, *args):
        self.fuel_tank = fuel_tank
        Vehicle.__init__(self, *args)

    def vehicle_print(self):
        Vehicle.vehicle_print(self)
        print('Fuel capacity (gallons): ' + str(self.fuel_tank))

class HighPerformance(GasVehicle):

    def __init__(self, hp, top_speed, *args):
        self.hp = hp
        self.top_speed = top_speed
        GasVehicle.__init__(self, *args)

    def vehicle_print(self):
        GasVehicle.vehicle_print(self)
        print('Horse power: ' + str(self.hp))
        print('Top speed: ' + str(self.top_speed))


class SportCar(HighPerformance):

    def __init__(self, gear_box, drive_system, *args):
        self.gearbox = gear_box
        self.drive_system = drive_system
        HighPerformance.__init__(self, *args)

    def vehicle_print(self):
        HighPerformance.vehicle_print(self)
        print('Gear box: ' + self.gearbox)
        print('Drive system: ' + self.drive_system)

bmw = GasVehicle(30, 'SUV', 'BMW', 'X5', 'silver', 2003, 120300)  # regular car
bmw.vehicle_print()
print
lambo = SportCar('manual', 'rear wheel', 650, 160, 23, 'race car', 'Lamborgini', 'V12', 'dark silver', 2014, 3500)  # sportscar
lambo.vehicle_print()
print
