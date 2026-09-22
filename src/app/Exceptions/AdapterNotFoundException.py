class AdapterNotFoundException(Exception):
    def __init__(self, *args, **kwargs):
        print(f"Adaptador no encontrado: {args}")
        super().__init__(*args, **kwargs)
