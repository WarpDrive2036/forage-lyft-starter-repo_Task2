from abc import ABC,abstractmethod

# Interface for serviceable parts
class Serviceable(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass
