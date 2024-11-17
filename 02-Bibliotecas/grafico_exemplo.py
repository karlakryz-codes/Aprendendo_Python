import matplotlib.pyplot as plt
import os

# Dados para o gráfico
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

# Criando o gráfico
plt.plot(x, y)

# Definindo o caminho da pasta onde deseja salvar a imagem
diretorio = 'C:/Users/Windows 11/estudoPython/02-Bibliotecas/'  # Caminho completo
arquivo = 'grafico_exemplo.png'

# Salvando o gráfico na pasta correta
plt.savefig(os.path.join(diretorio, arquivo))

# Exibindo o gráfico
plt.show()
