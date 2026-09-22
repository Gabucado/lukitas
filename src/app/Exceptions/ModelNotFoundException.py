class ModelNotFoundException(Exception):
    def __init__(self, *args, **kwargs):
        print(f"Modelo no encontrado: {args}")
        super().__init__(*args, **kwargs)
