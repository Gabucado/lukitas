
from src.app.common.IContainer import IContainer
from src.app.Exceptions.AdapterNotFoundException import AdapterNotFoundException
from src.app.Exceptions.ModelNotFoundException import ModelNotFoundException
from src.app.Exceptions.ServiceNotFoundException import ServiceNotFoundException


class Container(IContainer):
    models = {}
    services = {}
    adapters = {}

    def __init__(self):
        self.__initialize_models()
        self.__initialize_services()
        self.__initialize_adapters()

    def __initialize_models(self):
        print("models")

    def __initialize_services(self):
        print("services")

    def __initialize_adapters(self):
        print("adapters")

    def get_model(self, key:str):
        try:
            return self.models[key]
        except KeyError:
            raise ModelNotFoundException(key)

    def get_service(self, key:str):
        try:
            return self.services[key]
        except KeyError:
            raise ServiceNotFoundException(key)

    def get_adapter(self, key:str):
        try:
            return self.adapters[key]
        except KeyError:
            raise AdapterNotFoundException(key)
