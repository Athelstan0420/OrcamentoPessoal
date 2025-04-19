
from tkinter import * # Para criação de janelas em python;
from tkinter import Tk, ttk
from PIL import Image, ImageTk # Para manipular imagens em python;
from tkinter.ttk import Progressbar # Barra de progresso do tkinter;
#--------------------------------------------
# Libre: matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
#--------------------------------------------

#-------------------Cores-------------------------
cores = ['#5588bb', '#66bbbb', '#99bb55', '#ee9944', '#444466','#bb5555']
cor0 = "#2e2d2b" # preto
cor1 = "#feffff" # branco
cor2 = "#4fa882" # verde/azul claro
cor3 = "#38576b" # Azul meio escuro
cor4 = "#403d3d" # Preto
cor5 = "#e06636" # Laranja
cor6 = "#038cfc" # Azul claro
cor7 = "#3fbfb9" # azul + claro
cor8 = "#263238" # azul bem escuro
cor9 = "#e9edf5" # branco
#--------------------------------------------

janela = Tk()
janela.title("Orçamento Pessoal")
janela.geometry('900x650') # LarguraXComprimento;
janela.configure(background=cor9) # Cor do fundo;
janela.resizable(width=FALSE, height=FALSE)
estilo = ttk.Style(janela) # para aplicar estilo a janela;
estilo.theme_use("clam") #Aplicando um tema;

#------------------------------------------------------------------------------------------------------------
# Divisão de Frames para dividir a tela:
#------------------------------------------------------------------------------------------------------------
frame_cima = Frame(janela, width=1063, height=50, background=cor1, relief="flat")
frame_cima.grid(row=0, column=0)
#------------------------------------------------------------------------------------------------------------
frame_meio = Frame(janela, width=1043, height=361, background=cor1, relief="raised", pady=20)
frame_meio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)
#------------------------------------------------------------------------------------------------------------
frame_baixo = Frame(janela, width=1043, height=300, background=cor1, relief="flat") # flat = algo liso;
frame_baixo.grid(row=2, column=0, pady=0, padx=10, sticky=NSEW)
#------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------
# Trabalhando no Frame: (pip install pillow)
#------------------------------------------------------------------------------------------------------------

# Adicionando a logo e o título:

app_img = Image.open("/home/adriel/Documentos/Develop/OrcamentoPessoal/newlogo.png") # Acessar imagem;
app_img = app_img.resize((45,45)) #Altura e Largura;
app_img = ImageTk.PhotoImage(app_img) # Conversão/Preparação para a imagem ser usada;
app_logo = Label(frame_cima, image=app_img, text=" Orçamento Pessoal ", width=900, compound=LEFT, padx=5, relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=cor1, fg=cor4)
app_logo.place(x=0, y=0)

#------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------
#Porcetagem/Barra de progresso:
#------------------------------------------------------------------------------------------------------------

def porcentagem():

    l_nome = Label(frame_meio, text="Porcentagem da Receita Gasta", height=1, anchor=NW, font=('Verdana 12'), background=cor1, fg=cor4)
    l_nome.place(x=7, y=5)
    #Para barra de progresso:
    barra = Progressbar(frame_meio, length=180)
    barra.place(x=10, y=35)
    barra['value'] = 50 # Valor inicial predefinido. 
    #Para estilizar a barra:
    estilo = ttk.Style()
    estilo.theme_use('default')
    estilo.configure('black.Harizontal.TProgressbar', backgorund='#daed6b')
    estilo.configure('TProgressbar', thickness=25) # thickness = largura da barra de progresso; 
    # Porcentagem lateral:
    valor_ex = 50
    l_porcentagem = Label(frame_meio, text="{:,.2f}%".format(valor_ex), anchor=NW, font=('Verdana 12'), background=cor1, fg=cor4)
    l_porcentagem.place(x=200, y=35)

#------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------
# Gráfico de Barra: Utilizando matplotlib
#------------------------------------------------------------------------------------------------------------

def grafico_barra():

    lista_categorias = ['Renda', 'Despesas', 'Saldo']
    lista_valores = [3000, 2000, 6000]

    figura = plt.figure(figsize=(4, 3.35), dpi=60)
    ax = figura.add_subplot(111)
    # ax.autoscale(enable=True, axis='both', tight=None)

    ax.bar(lista_categorias, lista_valores, width=0.9) # O parametro "colors=cores" não estava funcionando;

    c = 0
    for i in ax.patches:
        ax.text(i.get_x()-.001, i.get_height()+.5, str("{:,.0f}".format(lista_valores[c])), fontsize=17, fontstyle='italic', verticalalignment='bottom', color='dimgrey')
        c+=1

    ax.set_xticklabels(lista_categorias, fontsize=16)

    ax.patch.set_facecolor('#ffffff')
    ax.spines['bottom'].set_color('#CCCCCC')
    ax.spines['bottom'].set_linewidth(1)
    ax.spines['right'].set_linewidth(0)
    ax.spines['top'].set_linewidth(0)
    ax.spines['left'].set_color('#CCCCCC')
    ax.spines['left'].set_linewidth(1)
    

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(bottom=False, left=False)
    ax.set_axisbelow(True)
    ax.yaxis.grid(False, color='#EEEEEE')
    ax.xaxis.grid(False)

    canva = FigureCanvasTkAgg(figura, frame_meio)
    canva.get_tk_widget().place(x=10, y=70)

#------------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------------
#Função Resumo:
#------------------------------------------------------------------------------------------------------------------------

def resumo():
    valor = [5000,6000,7000]
    l_linha = Label(frame_meio, text='', width=45, height=1, anchor=NW, font=('Arial 1'), bg='#545454' )
    l_linha.place(x=309, y=52)
    l_mensal_valor = Label(frame_meio, text='Total renda mensal      '.upper(), anchor=NW, font=('Verdana 12'), bg=cor1, fg=cor6)
    l_mensal_valor.place(x=309, y=35)
    l_mensal_valor = Label(frame_meio, text='R$ {:,.2f}'.format(valor[0]), anchor=NW, font=('Arial 12'), bg=cor1, fg=cor0)
    l_mensal_valor.place(x=309, y=70)
#------------------------------------------------------------------------------------------------------------------------
    l_linha = Label(frame_meio, text='', width=45, height=1, anchor=NW, font=('Arial 1'), bg='#545454' )
    l_linha.place(x=309, y=132)
    l_despesas_valor = Label(frame_meio, text='Total despesas mensais '.upper(), anchor=NW, font=('Verdana 12'), bg=cor1, fg=cor6)
    l_despesas_valor.place(x=309, y=115)
    l_despesas_valor = Label(frame_meio, text='R$ {:,.2f}'.format(valor[1]), anchor=NW, font=('Arial 12'), bg=cor1, fg=cor0)
    l_despesas_valor.place(x=309, y=150)
#------------------------------------------------------------------------------------------------------------------------
    l_linha = Label(frame_meio, text='', width=45, height=1, anchor=NW, font=('Arial 1'), bg='#545454' )
    l_linha.place(x=309, y=207)
    l_saldo_valor = Label(frame_meio, text='Total saldo caixa      '.upper(), anchor=NW, font=('Verdana 12'), bg=cor1, fg=cor6)
    l_saldo_valor.place(x=309, y=190)
    l_saldo_valor = Label(frame_meio, text='R$ {:,.2f}'.format(valor[2]), anchor=NW, font=('Arial 12'), bg=cor1, fg=cor0)
    l_saldo_valor.place(x=309, y=225)

#------------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------------
#Função Gráfico:
#------------------------------------------------------------------------------------------------------------------------

frame_grafico_pizza = Frame(frame_meio, width=580, height=250, background=cor1, relief="flat") # flat = algo liso;
frame_grafico_pizza.place(x=415, y=5)

def grafico_pizza():
    figura = plt.Figure(figsize=(5,3), dpi=90)
    ax = figura.add_subplot(111)

    lista_valores = [345,2345,234]
    lista_categorias = ['Renda', 'Despesas', 'saldo']


    explode = []

    for i in lista_categorias:
        explode.append(0.05)
    
    ax.pie(lista_valores, explode=explode, wedgeprops=dict(width=0.2), autopct='%1.1f%%', shadow=True, startangle=90)
    ax.legend(lista_categorias, loc='center right', bbox_to_anchor=(1.55, 0.50))

    canva_categoria = FigureCanvasTkAgg(figura, frame_grafico_pizza)
    canva_categoria.get_tk_widget().grid(row=0, column=0)

porcentagem()
grafico_barra()
resumo()
grafico_pizza()

#------------------------------------------------------------------------------------------------------------------------
janela.mainloop()

