
"""

Criando um banco de dados com python

lib: sqlite(pip install pysqlite3)

sqlite não é indicado para aplicações com grandes fluxos. 


"""

#impotando sqlite:
import sqlite3 as lite

try:
    
    conexao = lite.connect('dados.db') #Criar conexão:
    cursor = conexao.cursor() # É através desse cursor que vamos manipular o BD.


    #Criando tabelas:

    # #Tabelas categorias:
    # with conexao:
    #     cursor.execute(
    #     """  
    #         CREATE TABLE Categorias( 
            
    #         id INTEGER PRIMARY KEY AUTOINCREMENT,
    #         nome TEXT
            
    #         ) 
    #     """)
    # #Tabela de receitas:
    # with conexao:
    #     cursor.execute(
    #     """  
    #         CREATE TABLE Receitas(
            
    #         id INTEGER PRIMARY KEY AUTOINCREMENT,
    #         categoria TEXT,
    #         adicionado_em DATE,
    #         valor DECIMAL
            
    #         ) 
    #     """)
    # #Tabela de gastos:
    # with conexao:
    #     cursor.execute(
    #     """  
    #         CREATE TABLE Gastos(
            
    #         id INTEGER PRIMARY KEY AUTOINCREMENT,
    #         categoria TEXT,
    #         retirado_em DATE,
    #         valor DECIMAL
            
    #         ) 
    #     """)


    # #para visualizar os dados da tabela:
    # cursor.execute("SELECT * FROM nometabela")
    # print(cursor.fetchall())
    
except:
    print("ERRO!")

