#importando libre sqlite3
import sqlite3 as lite 
from criandoBD import tabelas


try:
#--------------------------------------------------------------------------------------------------------

    #Estabelecendo conexão com o BD:
    conexaoBD = lite.connect("/home/adriel/Documentos/Develop/OrcamentoPessoal/dados.db")
    # Cursor que manipulará as tabela:
    cursorBD = conexaoBD.cursor()

 #--------------------------------------------------------------------------------------------------------
#Inserindo:
#--------------------------------------------------------------------------------------------------------

    def inserir_Categorias():
        with conexaoBD:
            consulta = "INSERT INTO Categorias (nome) VALUES (?)"
            cursorBD.execute(consulta, ["Compras"])
            #conexao.commit() #Para enviar dados a tabela. 
    # inserir_Cateorias()
    
    def inserir_Receitas(): 
        with conexaoBD:
            consulta = "INSERT INTO Receitas (categoria, adicionado_em, valor) VALUES (?, ?, ?)"
            cursorBD.execute(consulta, ["teste1", "12/03/2020", "100"])
            # conexao.commit() #Para enviar dados a tabela. 
    # inserir_Receitas()
    
    def inserir_Gastos():
        with conexaoBD:
            consulta = "INSERT INTO Gastos (categoria, retirado_em, valor) VALUES (?, ?, ?)"
            cursorBD.execute(consulta, ["teste3", "31/03/2015", "50"])
            #conexao.commit() #Para enviar dados a tabela. 
    # inserir_Gastos()
#--------------------------------------------------------------------------------------------------------
# Deletando:
#--------------------------------------------------------------------------------------------------------

    def deletar_Categorias():
        with conexaoBD:
            consulta = "DELETE FROM Categorias WHERE id=?"
            cursorBD.execute(consulta, "1")
    # deletar_Categorias()
    
    def deletar_Receitas():
        with conexaoBD:
            consulta = "DELETE FROM Receitas WHERE id=?"
            cursorBD.execute(consulta, "1")
    # deletar_Receitas()

    def deletar_Gastos():
        with conexaoBD:
            consulta = "DELETE FROM Gastos WHERE id=?"
            cursorBD.execute(consulta, "1")
    # deletar_Gastos()

#--------------------------------------------------------------------------------------------------------
# Ver categorias
#--------------------------------------------------------------------------------------------------------

    # tabelas()

    def vizualizar_categorias():
        lista_itens = []
        with conexaoBD:
            cursorBD.execute("SELECT * FROM Categorias")
            linha = cursorBD.fetchall()
            for lin in linha:
                lista_itens.append(lin)
        # print(lista_itens)

    # Ver Receitas
    def vizu_receitas():
        lista_itens = []
        with conexaoBD:
            cursorBD.execute("SELECT * FROM Receitas")
            linha = cursorBD.fetchall()
            for lin in linha:
                lista_itens.append(lin)
        # print(lista_itens)

    # Ver Gastos
    def vizu_gastos():
        lista_itens = []
        with conexaoBD:
            cursorBD.execute("SELECT * FROM Gastos")
            linha = cursorBD.fetchall()
            for lin in linha:
                lista_itens.append(lin)
        # print(lista_itens)


#--------------------------------------------------------------------------------------------------------

    # Ou apenas:
        # #para visualizar os dados da tabela:
        # cursor.execute("SELECT * FROM Categorias")
        # print(cursor.fetchall())

#--------------------------------------------------------------------------------------------------------

    # def tabela2_manipuldados():
    #     vizu_gastos = ''

#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------

except:
    print("ERRO!")


