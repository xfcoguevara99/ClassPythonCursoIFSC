#coding: utf-8
import time as time
class Pasta():
    def __init__(self):
        self.id = " "
        self.documento = {}
    def CriarPastaVazia(self):
        self.id = input("Identificacao da pasta: ")
        self.id = str(int(time.time()))

    def get_idPasta(self):
        print("id = ",self.id)

if __name__ == "__main__":
    pasta1 = Pasta()
    pasta1.CriarPastaVazia()
    pasta1.get_idPasta()
    
        