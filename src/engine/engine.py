from abc import ABC

# Engine interface, extending Serviceable
class Engine(ABC):
    def needs_service(self):
        pass
