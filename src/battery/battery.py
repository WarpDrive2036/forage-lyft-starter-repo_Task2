from abc import ABC


# Battery interface, extending Serviceable
class Battery(ABC):
    def needs_service(self):
        pass




