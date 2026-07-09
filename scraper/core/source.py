from abc import ABC
from abc import abstractmethod


class Source(ABC):

    def __init__(self, name):

        self.name = name

    @abstractmethod
    def run(self):

        pass
