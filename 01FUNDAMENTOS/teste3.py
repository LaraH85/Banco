class veiculo:
    def __init__(self,rodas, portas, combustivel):
        self.rodas = rodas
        self.portas = portas
        self.combustivel = combustivel
    def calculo(self):
        return (self.rodas + self.portas)/2

caminhao = veiculo(16,2,"gasolina")
print(caminhao.calculo())



