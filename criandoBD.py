
"""
- Criando um banco de dados com python
- lib: sqlite(pip install pysqlite3)
- sqlite não é indicado para aplicações com grandes fluxos. 
"""

#impotando sqlite - Para utilizar o MySQL:
import sqlite3 as lite

try:
    
    conexaoBD = lite.connect('/home/adriel/Documentos/Develop/OrcamentoPessoal/dados.db') #Criar conexão e BD:
    cursorBD = conexaoBD.cursor() # É através desse cursor que vamos manipular o BD.

#--------------------------------------------------------------------------------------------------
    #Criando tabelas:
#--------------------------------------------------------------------------------------------------

    #Tabela categoria:
    def BD_tab_Categorias():
        with conexaoBD:
            cursorBD.execute(
            """  
                CREATE TABLE Categorias( 
                
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT
                
                ) 
            """)
    #Tabela de receitas:
    def BD_tab_Receitas():
        with conexaoBD:
            cursorBD.execute(
            """  
                CREATE TABLE Receitas(
                
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                categoria TEXT,
                adicionado_em DATE,
                valor DECIMAL
                
                ) 
            """)

    #Tabela de gastos:
    def BD_tab_Gastos():
        with conexaoBD:
            cursorBD.execute(
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


    # #para visualizar os dados da tabela:
    # def tabelas():
    #     cursor.execute("SELECT * FROM Categorias")
    #     print(cursor.fetchall())
    #     cursor.execute("SELECT * FROM Receitas")
    #     print(cursor.fetchall())
    #     cursor.execute("SELECT * FROM Gastos")
    #     print(cursor.fetchall())
    #tabelas()
    
except:
    print("ERRO!")

