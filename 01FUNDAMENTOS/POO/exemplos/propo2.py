class ControleRemoto:
    def __init__(self):
        self.__ligado = False   #atributo privado
        self.__canal = 1        #atributo privado
        self.__volume = 10        #atributo privado

    def ligar(self):
        self.__ligado = True
        print("TV ligada!")

    def desligar(self):
        self.__ligado = False
        print("TV desligada!")

    def aumentar_volume(self):
        if self.__ligado:
            self.__volume += 1
            print(f"Volume: {self.__volume} ")
    def diminuir_volume(self):
        if self.__ligado and self.__volume > 0:
            self.__volume -= 1
            print(f"Volume: {self.__volume} ")

print(ControleRemoto().ligar())
print(ControleRemoto().desligar())
print(ControleRemoto().aumentar_volume())
print(ControleRemoto().diminuir_volume())