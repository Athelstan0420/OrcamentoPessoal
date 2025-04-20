
"""
Frame = Elementos de uma interface gráfica;
"""
from tkinter import * # Para criação de janelas em python;
from tkinter import Tk, ttk
from PIL import Image, ImageTk # (Libre Pillow) Para manipular imagens em python;
from tkinter.ttk import Progressbar # Barra de progresso do tkinter;
from tkinter import messagebox
#--------------------------------------------
# Libre: matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
#--------------------------------------------
# importando tkcalendar(pip install)
from tkcalendar import Calendar, DateEntry
from datetime import date
#--------------------------------------------

#Importando manipulando dados:
#from manipulandoDados import vizualizar_categorias, inserir_Categorias, inserir_Receitas, inserir_Gastos

#--------------------------------------------

#-------------------Cores-------------------------
from cores import cor0,cor1,cor2,cor3,cor4,cor5,cor6,cor7,cor8,cor9
#-------------------------------------------------

#Primeiros passos para criar a janela tkinter:
janela = Tk() #Elemento essencial para criar a janela!
janela.title("Orçamento Pessoal") #Titulo da janela
janela.geometry('900x650') # LarguraXComprimento;
janela.configure(background=cor9) # Cor do fundo;
janela.resizable(width=FALSE, height=FALSE) #Permite redimensionar a tela ou não;
estilo = ttk.Style(janela) #para aplicar estilo a janela;
estilo.theme_use("clam") #Aplicando um tema;

#------------------------------------------------------------------------------------------------------------
# Divisão de Frames horizontais/ dividir a tela:
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
# Trabalhando no Frame: (pip install pillow) para manipular imagens;
#------------------------------------------------------------------------------------------------------------
# Adicionando a logo e o título/  Manipulando imagem:
logo_img = Image.open("/home/adriel/Documentos/Develop/OrcamentoPessoal/Imagens/newlogo.png") # Acessar imagem;
logo_img = logo_img.resize((45,45)) #Altura e Largura;
logo_img = ImageTk.PhotoImage(logo_img) # Conversão/Preparação para a imagem ser usada;
implementar_logo = Label(frame_cima, image=logo_img, text=" Orçamento Pessoal ", width=900, compound=LEFT, padx=5, relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=cor1, fg=cor4)
implementar_logo.place(x=0, y=0)
#------------------------------------------------------------------------------------------------------------


#Parte a ser analisada no final;
# global tree #Global/ Está sendo utilizado 
# def inserir_categorias_interface():
#     # #Caixa de entrada para categoria 2:
#     # new_categoria_valor = Entry(frame_receitas, width=14, justify='left', relief='solid')
#     # new_categoria_valor.place(x=112, y=140)
#     new_categoria_def = new_categoria_valor.get()
#     new_inserir_nomes_list = [new_categoria_def]

#     for i in new_inserir_nomes_list:
#         if i == '':
#             messagebox.showerro("Erro", "Preencha todos os campos!")
#             return 

#     inserir_Categorias(new_inserir_nomes_list)

#     messagebox.showinfo('Sucesso', 'Os dados foram inseridos!')

#     new_categoria_valor.delete(0,'end')

    # #Inserir Novas categorias:
    # nome_categoria2 = Label(frame_receitas, text='categoria', height=1,anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
    # nome_categoria2.place(x=10,y=140)


#------------------------------------------------------------------------------------------------------------
#Porcetagem/Barra de progresso:
#------------------------------------------------------------------------------------------------------------
def barra_progresso_def():
    titulo_barra_progresso = Label(frame_meio, text="Porcentagem da Receita Gasta", height=1, anchor=NW, font=('Verdana 12 bold'), background=cor1, fg=cor4)
    titulo_barra_progresso.place(x=7, y=5)
    #Para barra de progresso:
    barra_progress = Progressbar(frame_meio, length=180)
    barra_progress.place(x=10, y=35)
    barra_progress['value'] = 50 # Valor inicial predefinido. 
    #Para estilizar a barra:
    estilo = ttk.Style()
    estilo.theme_use('default')
    estilo.configure('black.Harizontal.TProgressbar', backgorund='#daed6b')
    estilo.configure('TProgressbar', thickness=25) # thickness = largura da barra de progresso; 
    # Porcentagem lateral:
    valor_ex = 50
    bar_progress_porcentageml = Label(frame_meio, text="{:,.2f}%".format(valor_ex), anchor=NW, font=('Verdana 12'), background=cor1, fg=cor4)
    bar_progress_porcentageml.place(x=200, y=35)
#------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------
# Gráfico de Barra: Utilizando matplotlib
#------------------------------------------------------------------------------------------------------------
def grafico_barra_def():

    lista_categorias_grafbar = ['Renda', 'Despesas', 'Saldo']
    lista_valores_grafbar = [3000, 2000, 6000]

    figura = plt.figure(figsize=(4, 3.35), dpi=60)
    ax = figura.add_subplot(111)
    # ax.autoscale(enable=True, axis='both', tight=None)

    ax.bar(lista_categorias_grafbar, lista_valores_grafbar, width=0.9) # O parametro "colors=cores" não estava funcionando;

    c = 0
    for i in ax.patches:
        ax.text(i.get_x()-.001, i.get_height()+.5, str("{:,.0f}".format(lista_valores_grafbar[c])), fontsize=17, fontstyle='italic', verticalalignment='bottom', color='dimgrey')
        c+=1

    ax.set_xticklabels(lista_categorias_grafbar, fontsize=16)

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
def resumo_renda_despesas_saldo_def():

    #Total de renda mensal:
    valores_resumo = [5000,6000,7000]

    linha_horizontal = Label(frame_meio, text='', width=45, height=1, anchor=NW, font=('Arial 1'), bg='#545454' )
    linha_horizontal.place(x=309, y=52)

    mensal_titulo = Label(frame_meio, text='Total renda mensal      '.upper(), anchor=NW, font=('Verdana 12'), bg=cor1, fg=cor6)
    mensal_titulo.place(x=309, y=35)

    mensal_valor = Label(frame_meio, text='R$ {:,.2f}'.format(valores_resumo[0]), anchor=NW, font=('Arial 12'), bg=cor1, fg=cor0)
    mensal_valor.place(x=309, y=70)
#------------------------------------------------------------------------------------------------------------------------
    linha_horizontal = Label(frame_meio, text='', width=45, height=1, anchor=NW, font=('Arial 1'), bg='#545454' )
    linha_horizontal.place(x=309, y=132)

    despesas_titulo = Label(frame_meio, text='Total despesas mensais '.upper(), anchor=NW, font=('Verdana 12'), bg=cor1, fg=cor6)
    despesas_titulo.place(x=309, y=115)

    despesas_valor = Label(frame_meio, text='R$ {:,.2f}'.format(valores_resumo[1]), anchor=NW, font=('Arial 12'), bg=cor1, fg=cor0)
    despesas_valor.place(x=309, y=150)
#------------------------------------------------------------------------------------------------------------------------
    linha_horizontal = Label(frame_meio, text='', width=45, height=1, anchor=NW, font=('Arial 1'), bg='#545454' )
    linha_horizontal.place(x=309, y=207)

    saldo_titulo = Label(frame_meio, text='Total saldo caixa      '.upper(), anchor=NW, font=('Verdana 12'), bg=cor1, fg=cor6)
    saldo_titulo.place(x=309, y=190)

    saldo_valor = Label(frame_meio, text='R$ {:,.2f}'.format(valores_resumo[2]), anchor=NW, font=('Arial 12'), bg=cor1, fg=cor0)
    saldo_valor.place(x=309, y=225)
#------------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------------
#Função Gráfico pizza:
#------------------------------------------------------------------------------------------------------------------------

frame_grafico_pizza = Frame(frame_meio, width=580, height=250, background=cor1, relief="flat") # flat = algo liso;
frame_grafico_pizza.place(x=415, y=5)

def grafico_pizza_def():

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
#--------------------------------------------------------------------------------------------------------------

barra_progresso_def()
grafico_barra_def()
resumo_renda_despesas_saldo_def()
grafico_pizza_def()

#--------------------------------------------------------------------------------------------------------------
# Frames da parte de baixo:
#--------------------------------------------------------------------------------------------------------------

titulo_tabela_receitas = Label(frame_meio, text="Tabelas de Receitas e Despesas",anchor=NW, font=("Verdana 12 bold"), bg=cor1, fg=cor4)
titulo_tabela_receitas.place(x=5, y=309)

frame_tabela = Frame(frame_baixo, width=300, height=250, bg=cor1)
frame_tabela.grid(row=0, column=0)

frame_inserir_despesas = Frame(frame_baixo, width=220, height=250, bg=cor1)
frame_inserir_despesas.grid(row=0, column=1, padx=5)

frame_inserir_receitas = Frame(frame_baixo, width=220, height=250, bg=cor1)
frame_inserir_receitas.grid(row=0, column=2, padx=5)

#--------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------
# Função para mostrar tabela:
#--------------------------------------------------------------------------------------------------------------

def mostrar_Tabela_renda():

    cabecalho_tabela = ['#Id', 'Categorias', 'Data', 'Quantia']

    lista_itens = [[0,2,3,4],[0,2,3,4],[0,2,3,4],[0,2,3,4]]

    global tree

    tree = ttk.Treeview(frame_tabela, selectmode='extended', columns=cabecalho_tabela, show='headings')

    barra_vertical_scroll = ttk.Scrollbar(frame_tabela, orient='vertical', command=tree.yview)

    barra_horizontal_scroll = ttk.Scrollbar(frame_tabela, orient='horizontal', command=tree.xview)

    tree.configure(yscrollcommand=barra_vertical_scroll.set, xscrollcommand=barra_horizontal_scroll.set)

    tree.grid(column=0,row=0,sticky='nsew')
    barra_vertical_scroll.grid(column=1,row=0,sticky='ns')
    barra_horizontal_scroll.grid(column=0,row=1,sticky='ew')

    hd = ['center','center', 'center', 'center']
    h = [30,100,100,100]
    n=0

    for coluna in cabecalho_tabela:
        tree.heading(coluna, text=coluna.title(), anchor=CENTER)
        tree.column(coluna,width=h[n], anchor=hd[n])

        n+=1
    
    for item in lista_itens:
        tree.insert('', 'end', values=item)
mostrar_Tabela_renda()
#------------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------
# Inserir novas despesas:
#--------------------------------------------------------------------------------------------------------------

#pip install tkcaledndar;

#Configuração despesas:
nome_despesas = Label(frame_inserir_despesas, text='Inserir novas despesas', height=1,anchor=NW, font=('Verdana 10 bold'), bg=cor1, fg=cor4)
nome_despesas.place(x=10,y=10)
nome_categoria = Label(frame_inserir_despesas, text='Categoria', height=1,anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
nome_categoria.place(x=10,y=40)

# Pegando/criando categoria:
lista_categorias = ['Viagem', 'Comida']
categorias = []
for i in lista_categorias:
    categorias.append(i[:])

#Criando caixa de seleção:
combo_categoria_despesas = ttk.Combobox(frame_inserir_despesas, width=10, font=('Ivy 10'))
combo_categoria_despesas['values'] = (categorias)
combo_categoria_despesas.place(x=112, y=41)

#Criando calendário:
nome_data = Label(frame_inserir_despesas, text='Data', height=1,anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
nome_data.place(x=10,y=70)
calendario = DateEntry(frame_inserir_despesas, width=12, background='darkblue', forefround='white', borderwidth=2, year=2022)
calendario.place(x=112, y=71)

#Quantia total / Caixa de entrada para valor:
nome_quantia = Label(frame_inserir_despesas, text='Quantia total', height=1,anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
nome_quantia.place(x=10,y=100)
quantia_valor = Entry(frame_inserir_despesas, width=14, justify='left', relief='solid')
quantia_valor.place(x=112, y=100)

#Botão de inserir:
pegar_img1 = Image.open("/home/adriel/Documentos/Develop/OrcamentoPessoal/adicionar.png") # Acessar imagem;
pegar_img1 = pegar_img1.resize((17,17)) #Altura e Largura;
pegar_img1 = ImageTk.PhotoImage(pegar_img1) # Conversão/Preparação para a imagem ser usada;
botao1 = Button(frame_inserir_despesas, image=pegar_img1, text="Adicionar".upper(), width=80, compound=LEFT, anchor=NW, font=('Ivy 7'), bg=cor1, fg=cor0, overrelief=RIDGE)
botao1.place(x=112, y=131)

#Botão remover:
pegar_img2 = Image.open("/home/adriel/Documentos/Develop/OrcamentoPessoal/deletar.png") # Acessar imagem;
pegar_img2 = pegar_img2.resize((17,17)) #Altura e Largura;
pegar_img2 = ImageTk.PhotoImage(pegar_img2) # Conversão/Preparação para a imagem ser usada;
excluir_acao = Label(frame_inserir_despesas, text='Excluir ação', height=1,anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
excluir_acao.place(x=10,y=180)
botao2 = Button(frame_inserir_despesas, image=pegar_img2, text="Deletar".upper(), width=80, compound=LEFT, anchor=NW, font=('Ivy 7'), bg=cor1, fg=cor0, overrelief=RIDGE)
botao2.place(x=112, y=180)
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
# Configurando Receitas:
#--------------------------------------------------------------------------------------------------------------

#Configuração receitas:
nome_receitas = Label(frame_inserir_receitas, text='Inserir novas receitas', height=1,anchor=NW, font=('Verdana 10 bold'), bg=cor1, fg=cor4)
nome_receitas.place(x=10,y=10)

#data 2:
nome_data2 = Label(frame_inserir_receitas, text='Data', height=1,anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
nome_data2.place(x=10,y=40)
#Criando calendário:
calendario2 = DateEntry(frame_inserir_receitas, width=12, background='darkblue', forefround='white', borderwidth=2, year=2022)
calendario2.place(x=112, y=41)

#Quantia total / Caixa de entrada para valor2:
nome_quantia2 = Label(frame_inserir_receitas, text='Quantia total', height=1,anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
nome_quantia2.place(x=10,y=70)
quantia_valor2 = Entry(frame_inserir_receitas, width=14, justify='left', relief='solid')
quantia_valor2.place(x=112, y=71)

#Botão de inserir3:
pegar_img3 = Image.open("/home/adriel/Documentos/Develop/OrcamentoPessoal/adicionar.png") # Acessar imagem;
pegar_img3 = pegar_img3.resize((17,17)) #Altura e Largura;
pegar_img3 = ImageTk.PhotoImage(pegar_img3) # Conversão/Preparação para a imagem ser usada;
botao1 = Button(frame_inserir_receitas, image=pegar_img3, text="Adicionar".upper(), width=80, compound=LEFT, anchor=NW, font=('Ivy 7'), bg=cor1, fg=cor0, overrelief=RIDGE)
botao1.place(x=112, y=100)

#Inserir Novas categorias:
nome_categoria2 = Label(frame_inserir_receitas, text='categoria', height=1,anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
nome_categoria2.place(x=10,y=140)
#Caixa de entrada para categoria 2:
new_categoria_valor = Entry(frame_inserir_receitas, width=14, justify='left', relief='solid')
new_categoria_valor.place(x=112, y=140)

#Botão de inserir 4:
pegar_img4 = Image.open("/home/adriel/Documentos/Develop/OrcamentoPessoal/adicionar.png") # Acessar imagem;
pegar_img4 = pegar_img4.resize((17,17)) #Altura e Largura;
pegar_img4 = ImageTk.PhotoImage(pegar_img4) # Conversão/Preparação para a imagem ser usada;
botao1 = Button(frame_inserir_receitas, image=pegar_img4, text="Adicionar".upper(), width=80, compound=LEFT, anchor=NW, font=('Ivy 7'), bg=cor1, fg=cor0, overrelief=RIDGE)
botao1.place(x=112, y=170)

#--------------------------------------------------------------------------------------------------------------

janela.mainloop()

