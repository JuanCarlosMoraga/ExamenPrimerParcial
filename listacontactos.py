class Contacto:
    def __init__(self, nombre, numero):
        self.nombre = nombre
        self.numero = numero

    def __str__(self):
        return f"{self.nombre} - {self.numero}"

contactos = [
    Contacto("Juan", "89443880"),
    Contacto("Carlos", "89079597"),
    Contacto("Luis", "88907830")
]

for contacto in contactos:
    print(contacto)