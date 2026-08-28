from abc import ABC, abstractmethod
class BaseStrategy(ABC):
    @abstractmethod
    def signal(self, df): pass
