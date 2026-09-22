class ServiceNotFoundException(Exception):
    def __init__(self, *args, **kwargs):
        print(f"Servicio no encontrado: {args}")
        super().__init__(*args, **kwargs)
