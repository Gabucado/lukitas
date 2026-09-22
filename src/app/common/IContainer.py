from abc import ABC, abstractmethod


class IContainer(ABC):
    @abstractmethod
    def get_model(self, key:str):...

    @abstractmethod
    def get_service(self, key:str):...

    @abstractmethod
    def get_adapter(self, key:str):...
