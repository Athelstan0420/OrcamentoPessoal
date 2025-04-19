#importando libre sqlite3
import sqlite3 as lite 

try:
#--------------------------------------------------------------------------------------------------------

    #Estabelecendo conexão com o BD:
    conexao = lite.connect("/home/adriel/Documentos/Develop/OrcamentoPessoal/dados.db")
    # Cursor que manipulará as tabela:
    cursor = conexao.cursor()

 #--------------------------------------------------------------------------------------------------------

    # #Inserindo:

#--------------------------------------------------------------------------------------------------------

    # with conexao:
    #     consulta = "INSERT INTO Categorias (nome) VALUES (?)"
    #     cursor.execute(consulta, ["Pão"])
    #     conexao.commit() #Para enviar dados a tabela. 

    # with conexao:
    #     consulta = "INSERT INTO Receitas (categoria, adicionado_em, valor) VALUES (?, ?, ?)"
    #     cursor.execute(consulta, ["teste1", "12032020", "100"])
    #     conexao.commit() #Para enviar dados a tabela. 

    # with conexao:
    #     consulta = "INSERT INTO Gastos (categoria, retirado_em, valor) VALUES (?, ?, ?)"
    #     cursor.execute(consulta, ["teste1", "31031015", "50"])
    #     conexao.commit() #Para enviar dados a tabela. 

#--------------------------------------------------------------------------------------------------------

    # Deletando:

#--------------------------------------------------------------------------------------------------------

    # with conexao:
    #     consulta = "DELETE FROM Categorias WHERE id=?"
    #     cursor.execute(consulta, "")
        
    # with conexao:
    #     consulta = "DELETE FROM Receitas WHERE id=?"
    #     cursor.execute(consulta, "")
    # with conexao:
    #     consulta = "DELETE FROM Gastos WHERE id=?"
    #     cursor.execute(consulta, "")

#--------------------------------------------------------------------------------------------------------

    # Ver categorias

#--------------------------------------------------------------------------------------------------------

    lista_itens = []
    with conexao:
        cursor.execute("SELECT * FROM Categorias")
        linha = cursor.fetchall()
        for lin in linha:
            lista_itens.append(lin)
    print(lista_itens)

    # Ver Receitas

    lista_itens = []
    with conexao:
        cursor.execute("SELECT * FROM Receitas")
        linha = cursor.fetchall()
        for lin in linha:
            lista_itens.append(lin)
    print(lista_itens)

    # Ver Gastos

    lista_itens = []
    with conexao:
        cursor.execute("SELECT * FROM Gastos")
        linha = cursor.fetchall()
        for lin in linha:
            lista_itens.append(lin)
    print(lista_itens)


#--------------------------------------------------------------------------------------------------------

    # Ou apenas:
        # #para visualizar os dados da tabela:
        # cursor.execute("SELECT * FROM Categorias")
        # print(cursor.fetchall())

#--------------------------------------------------------------------------------------------------------


except:
    print("ERRO!")

