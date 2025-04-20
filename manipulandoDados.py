#importando libre sqlite3
import sqlite3 as lite 
#from criandoBD import tabelas


try:
#--------------------------------------------------------------------------------------------------------

    #Estabelecendo conexão com o BD:
    conexaoBD = lite.connect("/home/adriel/Documentos/Develop/OrcamentoPessoal/dados.db")
    # Cursor que manipulará as tabela:
    cursorBD = conexaoBD.cursor()

 #--------------------------------------------------------------------------------------------------------
#Inserindo:
#--------------------------------------------------------------------------------------------------------

    def BD_inserir_Categorias():
        with conexaoBD:
            consultaBD = "INSERT INTO Categorias (nome) VALUES (?)"
            cursorBD.execute(consultaBD, ["Compras"])
            #conexao.commit() #Para enviar dados a tabela. 
    # inserir_Cateorias()
    
    def BD_inserir_Receitas(): 
        with conexaoBD:
            consultaBD = "INSERT INTO Receitas (categoria, adicionado_em, valor) VALUES (?, ?, ?)"
            cursorBD.execute(consultaBD, ["teste1", "12/03/2020", "100"])
            # conexao.commit() #Para enviar dados a tabela. 
    # inserir_Receitas()
    
    def BD_inserir_Gastos():
        with conexaoBD:
            consultaBD = "INSERT INTO Gastos (categoria, retirado_em, valor) VALUES (?, ?, ?)"
            cursorBD.execute(consultaBD, ["teste3", "31/03/2015", "50"])
            #conexao.commit() #Para enviar dados a tabela. 
    # inserir_Gastos()
#--------------------------------------------------------------------------------------------------------
# Deletando:
#--------------------------------------------------------------------------------------------------------

    def BD_deletar_Categorias():
        with conexaoBD:
            consultaBD = "DELETE FROM Categorias WHERE id=?"
            cursorBD.execute(consultaBD, "1")
    # deletar_Categorias()
    
    def BD_deletar_Receitas():
        with conexaoBD:
            consultaBD = "DELETE FROM Receitas WHERE id=?"
            cursorBD.execute(consultaBD, "1")
    # deletar_Receitas()

    def BD_deletar_Gastos():
        with conexaoBD:
            consultaBD = "DELETE FROM Gastos WHERE id=?"
            cursorBD.execute(consultaBD, "1")
    # deletar_Gastos()

#--------------------------------------------------------------------------------------------------------
# Ver categorias
#--------------------------------------------------------------------------------------------------------

    # tabelas()

    def BD_vizualizar_categorias():
        lista_itens = []
        with conexaoBD:
            cursorBD.execute("SELECT * FROM Categorias")
            linha = cursorBD.fetchall()
            for lin in linha:
                lista_itens.append(lin)
        # print(lista_itens)

    # Ver Receitas
    def BD_vizu_receitas():
        lista_itens = []
        with conexaoBD:
            cursorBD.execute("SELECT * FROM Receitas")
            linha = cursorBD.fetchall()
            for lin in linha:
                lista_itens.append(lin)
        # print(lista_itens)

    # Ver Gastos
    def BD_vizu_gastos():
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


