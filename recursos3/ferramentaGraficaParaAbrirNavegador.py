'''
bibliotecas:

webbrowser - fornece uma interface de alto nível para permitir a exibição de documentos web aos usuários.

tkinter - forneceinterface padrão do Python para o kit de ferramentas gráficas Tk.



'''

# Importa o módulo webbrowser para lidar com operações de navegação na web
import webbrowser

# Importa todas as classes e funções do módulo tkinter
from tkinter import *

# Cria uma instância da classe Tk, que representa a janela principal da interface gráfica
root = Tk()

# Define o título da janela principal
root.title('Abrir Browser')

# Define a geometria (largura x altura) da janela principal
root.geometry('300x200')

# Define uma função chamada google, que será chamada quando o botão for pressionado
def google():
    # Abre o navegador padrão com o site do Google
    webbrowser.open('www.google.com')

# Cria um botão na janela principal com o texto 'Abrir o Google' e vincula a função google ao evento de clique
# O método pack() é chamado imediatamente após a criação do botão para empacotá-lo na janela
# A variável mygoogle recebe o objeto Button criado
# pady=20 define o espaçamento vertical entre o botão e os elementos adjacentes
mygoogle = Button(root, text='Abrir o Google', command=google).pack(pady=20)

# Inicia o loop principal de eventos, que aguarda e responde às interações do usuário na interface gráfica
root.mainloop()
