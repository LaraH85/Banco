# Em um formulário de cadastro, o usuário inseriu o telefone: "  (11)99999-1234  ".Limpe esse texto removendo os espaços
#das pontas, os parênteses e o traço, deixando apenas os caracteres numéricos.

numero = "  (11)99999-1234  "

numero_limpo = numero.strip().replace("  ", "").replace("(11)", "11").replace("-", "")
print(numero_limpo)