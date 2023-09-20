from servacible import Serviceable  


# Define the Car class
class Car(Serviceable):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()
    
    