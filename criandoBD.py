"""

Criando um banco de dados com python

lib: sqlite(pip install pysqlite3)

sqlite não é indicado para aplicações com grandes fluxos. 


"""

#impotando sqlite:
import sqlite3 as lite

try:
    
    conexao = lite.connect('/home/adriel/Documentos/Develop/OrcamentoPessoal/dados.db') #Criar conexão e BD:
    cursor = conexao.cursor() # É através desse cursor que vamos manipular o BD.

#--------------------------------------------------------------------------------------------------
    #Criando tabelas:
#--------------------------------------------------------------------------------------------------

    #Tabela categoria:
    def tab_Categorias():
        with conexao:
            cursor.execute(
            """  
                CREATE TABLE Categorias( 
                
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT
                
                ) 
            """)
    #Tabela de receitas:
    def tab_Receitas():
        with conexao:
            cursor.execute(
            """  
                CREATE TABLE Receitas(
                
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                categoria TEXT,
                adicionado_em DATE,
                valor DECIMAL
                
                ) 
            """)

    #Tabela de gastos:
    def tab_Gastos():
        with conexao:
            cursor.execute(
            """  
                CREATE TABLE Gastos(
                
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                categoria TEXT,
                retirado_em DATE,
                valor DECIMAL
                
                ) 
            """)

    # tab_Categorias()
    # tab_Receitas()
    # tab_Gastos()

    #para visualizar os dados da tabela:
    def tabelas():
        cursor.execute("SELECT * FROM Categorias")
        print(cursor.fetchall())
        cursor.execute("SELECT * FROM Receitas")
        print(cursor.fetchall())
        cursor.execute("SELECT * FROM Gastos")
        print(cursor.fetchall())
    #tabelas()
    
except:
    print("ERRO!")

