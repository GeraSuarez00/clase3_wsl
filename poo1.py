
def main():
    class Persona():
        nombre= "Geraldine"
        apellido = "Suarez Solano"
        direccion ="Km 1"
        telefono = "3012621366"

        def mostrarPersona(self):
            print (f"Nombre: {self.nombre} {self.apellido}")

    persona1 = Persona () #crea una instancia de la clase (Objeto)
    persona1.nombre = "Gera"
    #print(persona1.nombre)   #Muestra el nombre d la persona1
    persona1.mostrarPersona() #ejecuta el método mostrar persona

    persona2 = Persona()
    persona2.nombre = "Karina"
    persona2.apellido = "Suarez"
    persona2.direccion = "Cra 9"
    persona2.telefono = "3012454120"
    persona2.mostrarPersona()


