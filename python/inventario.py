class Objeto:

    def __init__(self, nombre):
        self.nombre = nombre
        self.cantidad = 0

    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad += nueva_cantidad

if __name__ == "__main__":
    botella_de_agua = Objeto(nombre = "Botella de agua")
    botella_de_agua.actualizar_cantidad(nueva_cantidad = 10)
    print(botella_de_agua.nombre)
