
def main():
    class Persona():
        #datos se ejecutan automáticamente
        def __init__(self): #constructor, ejecuta el método cada vez q llame la clase
         
            self.nombre =input ("Ingrese el nombre: ")
            self.apellido =input ("Ingrese el apellido: ")
            self.direccion =input ("Ingrese la direccion: ")
            self.telefono =input ("Ingrese el telefono: ")
        
        def mostrarPersona(self):
         
            print (f"Nombre: {self.nombre} {self.apellido}")
    # persona1 = Persona()
    # persona1.mostrarPersona()
    
    # persona2 = Persona ()
    # persona2.mostrarPersona()

    class Empleado(Persona):
        def __init__(self):
            super().__init__() #super: va hasta el padre y ejecuta el método de la clase padre (método init)
            
            #__sueldo: __ esto no permite que accedan desde afuera, protege la variable
            self.__sueldo = float(input("Ingrese el sueldo: "))
            
            self.alimentacion = 0
            self.transporte = 0
            
            if (self.__sueldo<2000000):
                  self.alimentacion = 80000
                  self.transporte = 60000
           
            self.pension = (self.__sueldo*4)/100
            self.salud = (self.__sueldo*3.375)/100
            self.calcular_devengado()
            self.calcular_deduccion()
        
        def mostrarEmpleado(self):
            print ("")
            print("----------------")
            super().mostrarPersona() #ejecuta el método de la clase padre
            
            print(f"Sueldo: {self.__sueldo}")
            print(f"Transporte: {self.transporte}")
            print(f"Alimentacion: {self.alimentacion}")
            print(f"Pension: {self.pension}")
            print(f"Salud: {self.salud}")
            print ("")
            print (f"Devengado:  {self.devengado}")
            print (f"Deduccion:  {self.deduccion}")
        

        def calcular_devengado(self):
            self.devengado = self.alimentacion + self.transporte + self.__sueldo

        
        def calcular_deduccion(self):
            self.deduccion = self.__sueldo - self.salud + self.pension

        

#calcular devengado (alimentacion+ tranporte+sueldo) y calcular deduccion (salud+pension-sueldo)
#sueldo<2.000.000, se paga alimentacion 80.000, transporte 60,000
#sueldo >= 2.000.000, tranporte y alimentacion 0 
#pension=4%
#salud = 3.375%
    empleado1 = Empleado()
    #empleado1.__sueldo = 4000000
    empleado1.mostrarEmpleado()





if __name__ == "__main__":
    main()