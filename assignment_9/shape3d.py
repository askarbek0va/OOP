from abc import ABC, abstractmethod

class Shape3D(ABC):

    @abstractmethod
    def surface_area(self) -> float:
        pass

    @abstractmethod
    def volume(self) -> float:
        pass
