#coding: utf-8
import time
class caixa_acoplada():
    def __init__(self):
        self.nivel_agua = 0
        self.nivel_maximo = 5
        self.estado = 0
        self.vazao = 0.5
    def encher_caixa(self):
        print("enchendo...")
        while (self.nivel_agua < self.nivel_maximo):
            self.nivel_agua += self.vazao
            time.sleep(self.vazao)
            print("nivel da agua: {}".format(self.nivel_agua))

    def acionar_botao(self):
        pass
    def acionar_entrada_agua():
        pass

class comporta_vedacao(self):
    def abrir_comporta(self):
        pass
    def fechar_comporta(self):
        pass

class alavanca_acionamento(self):
    def __init__(self):
        self.contador = 0
    def acionar_alavanca(self):
        pass
    







if __name__ == "__main__":
    pass