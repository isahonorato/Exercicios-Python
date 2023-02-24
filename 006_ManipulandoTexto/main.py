#Chamamos uma frase de 'cadeia de caracteres' ou string.

#Fatiamento
frase = 'Bom dia amigos e amigas!'
frase [5:4:2]
print(frase)

#Análise
frase.count('o') #contando quantas vezes há a letra "o"
frase.find('ami') #contando em qual posição ele encontrou o "ami"

'dia' in frase #Existe "dia" em frase? se sim, ele retornará TRUE

#Transformação
frase.replace('amigos,' 'Android') #Onde tiver amigos ele substituíra por android
frase.upper() #Upper significa pra cima, ou seja, transforma em maiúsculas
frase.lower() #Lower é para baixo, ou seja transforma em minúsculos
frase.capitalize() #Joga todos os caracteres para minúsculos e somente o primeiro caractere em maiúsculo
frase.title() #Analisa quantas palavras tem a frase e realiza o captalize palavra por palavra
frase.strip() #Remove os espaços que houverem no começo da frase e no final
frase.rstrip() #Remove somente os últimos espaços (direita) da string
frase.lstrip() #Remove somente os espacços do começo (esquerda)

#26:38