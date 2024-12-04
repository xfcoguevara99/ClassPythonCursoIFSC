class Computador():
    def __init__(self,marca,memoria,placaV):
        self.__marca = marca
        self.memoria = memoria
        self.placaV = placaV
    def set_marca(self,marca):
        self.__marca = marca
    def set_memoria(self,memoria):
        self.memoria = memoria
    def set_placaV(self,placaV):
        self.placaV = placaV
    def get_computador(self):
        print("Marca do computador:", self.__marca)
    def get_memoria(self):
        print("Memória do computador:", self.memoria)
    def get_placaV(self):
        print("Placa de vídeo do computador:", self.placaV)

    def resumo(self):
        print("carateristicas da computadora: ")
        print("Marca: {}\nMemoria: {}\nPlaca de Video: {}\n".format(self.__marca,self.memoria,self.placaV))

    
marca = "DELL"
memoria = "16Gb"
placaV = "Nvdia"
        
computador1 = Computador(marca,memoria,placaV)
computador1.resumo()
"""computador1.get_computador()
computador1.get_memoria()
computador1.get_placaV()
computador1.set_memoria("256GB")
computador2 = Computador(marca,memoria,placaV)"""

