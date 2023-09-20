from datetime import date
from servacible import Serviceable  



# Engine interface, extending Serviceable
class Engine(Serviceable):
    pass


# Battery interface, extending Serviceable
class Battery(Serviceable):
    pass


# Define the Car class
class Car:
    def __init__(self, engine: Engine, battery: Battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()
    
    
# CarFactory class
class CarFactory:
    @staticmethod
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = Engine(last_service_mileage, current_mileage)
        battery = Battery(last_service_date, current_date)
        return Car(engine, battery)

    @staticmethod
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = Engine(last_service_mileage, current_mileage)
        battery = Battery(last_service_date, current_date)
        return Car(engine, battery)

    @staticmethod
    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool) -> Car:
        engine = Engine(0, 0)
        battery = Battery(last_service_date, current_date)
        return Car(engine, battery)

    @staticmethod
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = Engine(last_service_mileage, current_mileage)
        battery = Battery(last_service_date, current_date)
        return Car(engine, battery)

    @staticmethod
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = Engine(last_service_mileage, current_mileage)
        battery = Battery(last_service_date, current_date)
        return Car(engine, battery)