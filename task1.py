from abc import abstractmethod, ABC

from logger import logger


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass


class Car(Vehicle):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        logger.info(f"{self.make} {self.model}: Двигун запущено")


class Motorcycle(Vehicle):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        logger.info(f"{self.make} {self.model}: Мотор заведено")


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self):
        pass

    @abstractmethod
    def create_motorcycle(self):
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(f"{make} (US Spec)", model)

    def create_motorcycle(self, make, model):
        return Motorcycle(f"{make} (US Spec)", model)


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(f"{make} (EU Spec)", model)

    def create_motorcycle(self, make, model):
        return Motorcycle(f"{make} (EU Spec)", model)


if __name__ == "__main__":
    eu_vehicle_factory = EUVehicleFactory()
    eu_car = eu_vehicle_factory.create_car("VW", "T-Cross")
    eu_motorcycle = eu_vehicle_factory.create_motorcycle("Ducati", "PaulSmart 9000")
    eu_car.start_engine()
    eu_motorcycle.start_engine()

    us_vehicle_factory = USVehicleFactory()
    us_car = us_vehicle_factory.create_car("Ford", "Mustang")
    us_motorcycle = us_vehicle_factory.create_motorcycle("Harley-Davidson", "Sportster")
    us_car.start_engine()
    us_motorcycle.start_engine()
