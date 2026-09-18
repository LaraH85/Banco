# Escreva um script que verifique se uma string contendo um código de rastramento
# de objeto dos Correios começa obrigatoriamente com duas letras maiúsculas "BR" e termina com "BR".

codigo = input ('Digite um código em BR início e fim: ')

if codigo[0:1] in "BR" and codigo.endswith("BR"):
    print(f"O codigo deu certo!")

else:
    print(f"O codigo deu erro!")
