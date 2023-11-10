from abc import ABC, abstractmethod

class Environnement(ABC):
    @abstractmethod
    def __init__(self):
        # initialise l'environnement
        pass

    @abstractmethod
    def applyAction(self, action):
        # applique l'action à l'environnement
        pass

    @abstractmethod
    def getState(self):
        # retourne l'état de l'environnement
        pass