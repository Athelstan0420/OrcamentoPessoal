#importando libre sqlite3
import sqlite3 as lite 
from criandoBD import tabelas


try:
#--------------------------------------------------------------------------------------------------------

    #Estabelecendo conexão com o BD:
    conexao = lite.connect("/home/adriel/Documentos/Develop/OrcamentoPessoal/dados.db")
    # Cursor que manipulará as tabela:
    cursor = conexao.cursor()

 #--------------------------------------------------------------------------------------------------------

    #Inserindo:

#--------------------------------------------------------------------------------------------------------

    def inserir_Cateorias():
        with conexao:
            consulta = "INSERT INTO Categorias (nome) VALUES (?)"
            cursor.execute(consulta, ["Compras"])
            #conexao.commit() #Para enviar dados a tabela. 
    # inserir_Cateorias()
    
    def inserir_Receitas(): 
        with conexao:
            consulta = "INSERT INTO Receitas (categoria, adicionado_em, valor) VALUES (?, ?, ?)"
            cursor.execute(consulta, ["teste1", "12/03/2020", "100"])
            # conexao.commit() #Para enviar dados a tabela. 
    # inserir_Receitas()
    
    def inserir_Gastos():
        with conexao:
            consulta = "INSERT INTO Gastos (categoria, retirado_em, valor) VALUES (?, ?, ?)"
            cursor.execute(consulta, ["teste3", "31/03/2015", "50"])
            #conexao.commit() #Para enviar dados a tabela. 
    # inserir_Gastos()
#--------------------------------------------------------------------------------------------------------

    # Deletando:

#--------------------------------------------------------------------------------------------------------

    def deletar_Categorias():
        with conexao:
            consulta = "DELETE FROM Categorias WHERE id=?"
            cursor.execute(consulta, "1")
    # deletar_Categorias()
    
    def deletar_Receitas():
        with conexao:
            consulta = "DELETE FROM Receitas WHERE id=?"
            cursor.execute(consulta, "1")
    # deletar_Receitas()

    def deletar_Gastos():
        with conexao:
            consulta = "DELETE FROM Gastos WHERE id=?"
            cursor.execute(consulta, "1")
    # deletar_Gastos()

#--------------------------------------------------------------------------------------------------------

    # Ver categorias

#--------------------------------------------------------------------------------------------------------

    tabelas()

    # lista_itens = []
    # with conexao:
    #     cursor.execute("SELECT * FROM Categorias")
    #     linha = cursor.fetchall()
    #     for lin in linha:
    #         lista_itens.append(lin)
    # print(lista_itens)

    # # Ver Receitas

    # lista_itens = []
    # with conexao:
    #     cursor.execute("SELECT * FROM Receitas")
    #     linha = cursor.fetchall()
    #     for lin in linha:
    #         lista_itens.append(lin)
    # print(lista_itens)

    # # Ver Gastos

    # lista_itens = []
    # with conexao:
    #     cursor.execute("SELECT * FROM Gastos")
    #     linha = cursor.fetchall()
    #     for lin in linha:
    #         lista_itens.append(lin)
    # print(lista_itens)


#--------------------------------------------------------------------------------------------------------

    # Ou apenas:
        # #para visualizar os dados da tabela:
        # cursor.execute("SELECT * FROM Categorias")
        # print(cursor.fetchall())

#--------------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------------





except:
    print("ERRO!")


