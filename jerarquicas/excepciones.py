class DuplicatedKeyError(Exception):
    def __init__(self, nueva_clave) -> None:
        super().__init__(f"La clave: {nueva_clave} se encuentra duplicada")
class HomogenetyError(Exception):
    def __init__(self, nueva_clave) -> None:
        super().__init__(f"La clave: {nueva_clave} no coincide con el tipo del arbol")