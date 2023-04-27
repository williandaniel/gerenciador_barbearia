import psycopg2
from menu import *
import sys, subprocess
import pyfiglet
import pandas as pd
from tabulate import tabulate

def clear_screen():
    operating_system = sys.platform
    if operating_system == 'win32':
        subprocess.run('cls', shell=True)
    elif operating_system == 'linux' or operating_system == 'darwin':
        subprocess.run('clear', shell=True)

db = psycopg2.connect(database = 'db_barbearia', user = 'postgres', password = 'barbearia', host = 'localhost', port = 5433)

print("Connection Successful to PostgreSQL")

cursor = db.cursor()


while True:
    # clear_screen() # Caso queira que limpe a tela do terminal
    print(pyfiglet.figlet_format('Barbearia'))
    res = menuPrincipal()
# ----------------------------EXIBIR-------------------------------------------
    if res['opcao'] == 'Exibir':
        exibir = menuExibir()

        if exibir['opcao'] == 'Clientes':
            cursor.execute("SELECT * FROM cliente ORDER BY codcliente ASC")
            result = cursor.fetchall()
            if result == []:
                print('Tabela Vazia')
            else:
                print(tabulate(result, tablefmt='outline', showindex='always', headers=['codcliente','nome','sobrenome','telefone','cpf','rg','dtnascimento','genero','idendereco']))
            input("Press Enter to continue...")

        if exibir['opcao'] == 'Funcionarios':
            cursor.execute("SELECT * FROM funcionario ORDER BY codfuncionario ASC")
            result = cursor.fetchall()
            if result == []:
                print('Tabela Vazia')
            else:
                print(tabulate(result, tablefmt='outline', showindex='always', headers=['codfuncionario','nome','sobrenome','telefone','cpf','rg','email','dtnascimento','genero','estadocivil','idendereco']))
            input("Press Enter to continue...")

        if exibir['opcao'] == 'Endereço':
            cursor.execute("SELECT * FROM endereco ORDER BY idendereco ASC")
            result = cursor.fetchall()
            if result == []:
                print('Tabela Vazia')
            else:
                print(tabulate(result, tablefmt='outline', showindex='always', headers=['idendereco','bairro','rua','numero','complemento','uf','cidade']))
            input("Press Enter to continue...")
            
        if exibir['opcao'] == 'Serviços':
            cursor.execute("SELECT * FROM servico ORDER BY codservico ASC")
            result = cursor.fetchall()

            if result == []:
                print('Tabela Vazia')
            else:
                print(tabulate(result, tablefmt='outline', showindex='always', headers=['codservico','tiposervico','preco','tempomedio']))
            input("Press Enter to continue...")

        if exibir['opcao'] == 'Agendamentos':
            cursor.execute("SELECT * FROM agendamento ORDER BY codagendamento ASC")
            result = cursor.fetchall()
            if result == []:
                print('Tabela Vazia')
            else:
                print(tabulate(result, tablefmt='outline', showindex='always', headers=['codagendamento','dataagendamento','hora','situacao','codfuncionario','codcliente','codservico']))
            input("Press Enter to continue...")

        if exibir['opcao'] == 'Voltar':
            continue
# ---------------------------ADICIONAR--------------------------------------------
    if res['opcao'] == 'Adicionar':
        adicionar = menuAdicionar()

        if adicionar['opcao'] == 'Clientes':  
            nome = input("Nome: ")
            sobrenome = input("Sobrenome: ")
            telefone = input("Telefone: ")
            cpf = input("CPF: ")
            if len(cpf) == 0:
                cpf = None
            rg = input("RG: ")
            if len(rg) == 0:
                rg = None
            dtnascimento = input("Data Nascimento (ano-mes-dia): ")
            if len(dtnascimento) == 0:
                dtnascimento = None
            gen = generoC()
            if gen['opcao'] == 'Não Informar':
                gen['opcao'] = None
            end = endereco()
            
            if end['opcao'] == True:
                bairro = input("Bairro: ")
                rua = input("Rua: ")
                numero = input("Número: ")
                complemento = input("Complemento: ")
                if len(complemento) == 0:
                    complemento = None
                uf = input("UF: ")
                cidade = input("Cidade: ")
                cursor.execute("INSERT INTO endereco (bairro, rua, numero, complemento, uf, cidade) VALUES (%s, %s, %s, %s, %s, %s);", (bairro, rua, numero, complemento, uf, cidade))
                db.commit()

                cursor.execute("SELECT idendereco FROM endereco ORDER BY 1 DESC LIMIT 1;")
                idendereco = cursor.fetchone()
            else:
                idendereco = None
            
            cursor.execute("INSERT INTO cliente (nome, sobrenome, telefone, cpf, rg, dtnascimento, genero, idendereco) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);", (nome, sobrenome, telefone, cpf, rg, dtnascimento, gen['opcao'], idendereco))
            db.commit()
            input("Press Enter to continue...")

        if adicionar['opcao'] == 'Funcionarios':
            nome = input("Nome: ")
            sobrenome = input("Sobrenome: ")
            telefone = input("Telefone: ")
            cpf = input("CPF: ")
            rg = input("RG: ")
            email = input("E-mail: ")
            dtnascimento = input("Data Nascimento (ano-mes-dia): ")
            gen = generoF()
            estcivil = estadocivil()

            bairro = input("Bairro: ")
            rua = input("Rua: ")
            numero = input("Número: ")
            complemento = input("Complemento: ")
            if len(complemento) == 0:
                complemento = None
            uf = input("UF: ")
            cidade = input("Cidade: ")

            cursor.execute("INSERT INTO endereco (bairro, rua, numero, complemento, uf, cidade) VALUES (%s, %s, %s, %s, %s, %s);", (bairro, rua, numero, complemento, uf, cidade))
            db.commit()

            cursor.execute("SELECT idendereco FROM endereco ORDER BY 1 DESC LIMIT 1;")
            idendereco = cursor.fetchone()
            
            cursor.execute("INSERT INTO funcionario (nome, sobrenome, telefone, cpf, rg, email, dtnascimento, genero, estadocivil, idendereco) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);", (nome, sobrenome, telefone, cpf, rg, email, dtnascimento, gen['opcao'], estcivil['opcao'], idendereco))
            db.commit()
            input("Press Enter to continue...")

        if adicionar['opcao'] == 'Serviços':
            tiposervico = input("Tipo de Serviço: ")
            preco = int(input("Preço: "))
            tempomedio = int(input("Tempo Médio do Serviço: "))
            cursor.execute("INSERT INTO servico (tiposervico, preco, tempomedio) VALUES (%s, %s, %s);", (tiposervico, preco, tempomedio))
            db.commit()
            input("Press Enter to continue...")

        if adicionar['opcao'] == 'Agendamentos':
            dataagendamento = input("Informe a Data do Agendamento: ")
            cursor.execute("SELECT a.hora, (a.hora + interval '1 minutes' * b.tempomedio), a.codfuncionario FROM agendamento a JOIN servico b ON a.codservico = b.codservico AND a.dataagendamento = %s AND a.situacao = 'agendado' ORDER BY a.hora", (dataagendamento,))
            horadata = cursor.fetchall()
            if horadata == []:
                print('Não existe nenhum agendamento para esta Data')
            else:
                print("Tabela das horas agendadas nessa data: ")
                print(tabulate(horadata, tablefmt='outline', showindex='always', headers=['Hora Inicio','Hora Fim', 'Cod. Funcionario']))

            hora = input("Informe a Hora: ")
            codfuncionario = input("Informe o Codigo do Funcionario: ")
            codcliente = input("Informe o Codigo do Cliente: ")
            codservico = input("Informe o Codigo do servico: ")
            
            cursor.execute("SELECT * FROM funcionario WHERE codfuncionario = %s;", (codfuncionario,))
            result = cursor.fetchall()
            if result == []:
                print('Codigo do Funcionario não Existe')
                input("Press Enter to continue...")
                continue
            else:
                print(tabulate(result, tablefmt='outline', showindex='always', headers=['codfuncionario','nome','sobrenome','telefone','cpf','rg','email','dtnascimento','genero','estadocivil','idendereco']))

            cursor.execute("SELECT * FROM cliente WHERE codcliente = %s;", (codcliente,))
            result = cursor.fetchall()
            if result == []:
                print('Codigo do Cliente não Existe')
                input("Press Enter to continue...")
                continue
            else:
                print(tabulate(result, tablefmt='outline', showindex='always', headers=['codcliente','nome','sobrenome','telefone','cpf','rg','dtnascimento','genero','idendereco']))
            
            cursor.execute("SELECT * FROM servico WHERE codservico = %s;", (codservico,))
            result = cursor.fetchall()
            if result == []:
                print('Codigo do Serviço não Existe')
                input("Press Enter to continue...")
                continue
            else:
                print(tabulate(result, tablefmt='outline', showindex='always', headers=['codservico','tiposervico','preco','tempomedio']))


            cursor.execute("SELECT tempomedio FROM servico WHERE codservico = %s;", (codservico,))
            result = cursor.fetchone()
            interval = str(result[0]) + ' minutes'
            cursor.execute("SELECT time %s + interval %s;", (hora,interval,))
            horafim = cursor.fetchone()

            if horadata == []:
                confirma = confirmarAgendamento()
                if confirma['opcao'] == 'Sim':
                    cursor.execute("INSERT INTO agendamento (dataagendamento, hora, codfuncionario, codcliente, codservico) VALUES (%s, %s, %s, %s, %s);", (dataagendamento, hora, codfuncionario, codcliente, codservico))
                    db.commit()
            else:
                cursor.execute("SELECT COUNT(*) FROM agendamento a JOIN servico s on s.codservico = a.codservico WHERE a.dataagendamento = %s AND ((%s >= a.hora AND %s < (a.hora + (s.tempomedio || ' minutes')::interval)) OR (%s > a.hora AND %s <= (a.hora + (s.tempomedio || ' minutes')::interval)) OR (%s < a.hora AND %s > (a.hora + (s.tempomedio || ' minutes')::interval))) AND a.codfuncionario = %s AND a.situacao = 'agendado';", (dataagendamento,hora,hora,horafim,horafim,hora,horafim,codfuncionario))
                result = cursor.fetchone()  
                if result[0] >= 1:
                    print("Existe conflito no agendamento, selecione outro horario!")
                else:
                    cursor.execute("INSERT INTO agendamento (dataagendamento, hora, codfuncionario, codcliente, codservico) VALUES (%s, %s, %s, %s, %s);", (dataagendamento, hora, codfuncionario, codcliente, codservico))
                    db.commit()
            input("Press Enter to continue...")

        if adicionar['opcao'] == 'Voltar':
            continue

# -------------------------------REMOVER----------------------------------------    
    if res['opcao'] == 'Remover':
        rem = menuRemover()
        
        if rem['opcao'] == 'Cliente':
            codcliente = input("Insira o Codigo do Cliente: ")
            cursor.execute("SELECT * FROM cliente WHERE codcliente = %s;", (codcliente,))
            result = cursor.fetchall()
            if result == []:
                print('Codigo do Cliente não Existe')
                input("Press Enter to continue...")
                continue
            else:
                print(tabulate(result, tablefmt='outline', showindex='always', headers=['codcliente','nome','sobrenome','telefone','cpf','rg','dtnascimento','genero','idendereco']))
            
            remov = confirmarRemocao()

            if remov['opcao'] == 'Sim':

                cursor.execute("SELECT idendereco FROM cliente WHERE codcliente = %s;", (codcliente,))
                result = cursor.fetchone()
                if result[0] != None:
                    cursor.execute("DELETE FROM endereco WHERE idendereco = %s;", (result[0],))
                    db.commit()

                    cursor.execute("DELETE FROM cliente WHERE codcliente = %s;", (codcliente,))
                    db.commit()
                    input("Press Enter to continue...")
                else:
                    cursor.execute("DELETE FROM cliente WHERE codcliente = %s;", (codcliente,))
                    db.commit()
                    input("Press Enter to continue...")
            else:
                input("Press Enter to continue...")

        if rem['opcao'] == 'Funcionario':
            codfuncionario = input("Insira o Codigo do Funcionario: ")
            cursor.execute("SELECT * FROM funcionario WHERE codfuncionario = %s;", (codfuncionario,))
            result = cursor.fetchall()
            if result == []:
                print('Codigo do Funcionario não Existe')
                input("Press Enter to continue...")
                continue
            else:
                print(tabulate(result, tablefmt='outline', showindex='always', headers=['codfuncionario','nome','sobrenome','telefone','cpf','rg','email','dtnascimento','genero','estadocivil','idendereco']))
            
            remov = confirmarRemocao()

            if remov['opcao'] == 'Sim':
                cursor.execute("SELECT idendereco FROM funcionario WHERE codfuncionario = %s;", (codfuncionario,))
                result = cursor.fetchone()

                cursor.execute("DELETE FROM funcionario WHERE codfuncionario = %s;", (codfuncionario,))
                db.commit()

                cursor.execute("DELETE FROM endereco WHERE idendereco = %s;", (result[0],))
                db.commit()
                input("Press Enter to continue...")
            else:
                input("Press Enter to continue...")

        if rem['opcao'] == 'Endereço':
            idendereco = input("Insira o ID do Endereço: ")
            cursor.execute("SELECT * FROM endereco WHERE idendereco = %s;", (idendereco,))
            result = cursor.fetchall()
            if result == []:
                print('Codigo do Cliente não Existe')
                input("Press Enter to continue...")
                continue
            else:
                print(tabulate(result, tablefmt='outline', showindex='always', headers=['idendereco','bairro','rua','numero','complemento','uf','cidade']))
            
            remov = confirmarRemocao()

            if remov['opcao'] == 'Sim':
                cursor.execute("SELECT COUNT(*) FROM funcionario WHERE idendereco = %s;", (idendereco,))
                result = cursor.fetchone()
                if result[0] >= 1:
                    print("Existe dependencia entre as Tabalas Funcionario e Endereço")
                    input("Press Enter to continue...")
                else:
                    cursor.execute("DELETE FROM endereco WHERE idendereco = %s;", (idendereco,))
                    db.commit()
                    input("Press Enter to continue...")
            else:
                input("Press Enter to continue...")
                

        if rem['opcao'] == 'Serviço':
            codservico = input("Insira o Codigo do Serviço: ")
            cursor.execute("SELECT * FROM servico WHERE codservico = %s;", (codservico,))
            result = cursor.fetchall()
            if result == []:
                print('Codigo do Serviço não Existe')
                input("Press Enter to continue...")
                continue
            else:
                print(tabulate(result, tablefmt='outline', showindex='always', headers=['codservico','tiposervico','preco','tempomedio']))
            
            remov = confirmarRemocao()

            if remov['opcao'] == 'Sim':
                cursor.execute("DELETE FROM servico WHERE codservico = %s;", (codservico,))
                db.commit()
                input("Press Enter to continue...")
            else:
                input("Press Enter to continue...")

        if rem['opcao'] == 'Agendamento':
            codagendamento = input("Insira o Codigo do Agendamento: ")
            cursor.execute("SELECT * FROM agendamento WHERE codagendamento = %s;", (codagendamento,))
            result = cursor.fetchall()
            if result == []:
                print('Codigo do Serviço não Existe')
                input("Press Enter to continue...")
                continue
            else:
                print(tabulate(result, tablefmt='outline', showindex='always', headers=['codagendamento','dataagendamento','hora','situacao','codfuncionario','codcliente','codservico']))

            remov = confirmarRemocao()

            if remov['opcao'] == 'Sim':
                cursor.execute("DELETE FROM agendamento WHERE codagendamento = %s;", (codagendamento,))
                db.commit()
                input("Press Enter to continue...")
            else:
                input("Press Enter to continue...")

        if rem['opcao'] == 'Voltar':
            continue
# ---------------------------EDITAR------------------------------------
    if res['opcao'] == 'Editar':
        ed = menuEditar()
        
        if ed['opcao'] == 'Cliente':
            codcliente = input("Insira o Codigo do Cliente: ")
            cursor.execute("SELECT * FROM cliente WHERE codcliente = %s;", (codcliente,))
            result = cursor.fetchall()
            if result == []:
                print('Codigo do Cliente não Existe')
                input("Press Enter to continue...")
                continue
            else:
                print(tabulate(result, tablefmt='outline', showindex='always', headers=['codcliente','nome','sobrenome','telefone','cpf','rg','dtnascimento','genero','idendereco']))
            cursor.execute("SELECT idendereco FROM cliente WHERE codcliente = %s;", (codcliente,))
            result = cursor.fetchone()

            nome = input("Nome: ")
            sobrenome = input("Sobrenome: ")
            telefone = input("Telefone: ")
            cpf = input("CPF: ")
            rg = input("RG: ")
            dtnascimento = input("Data Nascimento (ano-mes-dia): ")
            if len(dtnascimento) == 0:
                dtnascimento = None
            gen = generoC()
            if gen['opcao'] == 'Não Informar':
                gen['opcao'] = None

            if result[0] == None:
                edend = editarEnderecoNull()
                if edend['opcao'] == 'Manter Null':
                    idendereco = None
                if edend['opcao'] == 'Cadastrar Endereço':
                    bairro = input("Bairro: ")
                    rua = input("Rua: ")
                    numero = input("Número: ")
                    complemento = input("Complemento: ")
                    if len(complemento) == 0:
                        complemento = None
                    uf = input("UF: ")
                    cidade = input("Cidade: ")

                    cursor.execute("INSERT INTO endereco (bairro, rua, numero, complemento, uf, cidade) VALUES (%s, %s, %s, %s, %s, %s);", (bairro, rua, numero, complemento, uf, cidade))
                    db.commit()
                    cursor.execute("SELECT idendereco FROM endereco ORDER BY 1 DESC LIMIT 1;")
                    idendereco = cursor.fetchone()
                
                cursor.execute("UPDATE cliente SET nome = %s, sobrenome = %s, telefone = %s, cpf = %s, rg = %s, dtnascimento = %s, genero = %s, idendereco = %s WHERE codcliente = %s;", (nome, sobrenome, telefone, cpf, rg, dtnascimento, gen['opcao'], idendereco, codcliente))
                db.commit()
                input("Press Enter to continue...")
            else:
                cursor.execute("UPDATE cliente SET nome = %s, sobrenome = %s, telefone = %s, cpf = %s, rg = %s, dtnascimento = %s, genero = %s WHERE codcliente = %s;", (nome, sobrenome, telefone, cpf, rg, dtnascimento, gen['opcao'], codcliente))
                db.commit()
                input("Press Enter to continue...")


        if ed['opcao'] == 'Funcionario':
            codfuncionario = input("Insira o Codigo do Funcionario: ")
            cursor.execute("SELECT * FROM funcionario WHERE codfuncionario = %s;", (codfuncionario,))
            result = cursor.fetchall()
            if result == []:
                print('Codigo do Funcionario não Existe')
                input("Press Enter to continue...")
                continue
            else:
                print(tabulate(result, tablefmt='outline', showindex='always', headers=['codfuncionario','nome','sobrenome','telefone','cpf','rg','email','dtnascimento','genero','estadocivil','idendereco']))
            
            nome = input("Nome: ")
            sobrenome = input("Sobrenome: ")
            telefone = input("Telefone: ")
            cpf = input("CPF: ")
            rg = input("RG: ")
            email = input("E-mail: ")
            dtnascimento = input("Data Nascimento (ano-mes-dia): ")
            gen = generoF()
            estcivil = estadocivil()

            cursor.execute("UPDATE funcionario SET nome = %s, sobrenome = %s, telefone = %s, cpf = %s, rg = %s, email = %s, dtnascimento = %s, genero = %s, estadocivil = %s WHERE codfuncionario = %s;", (nome, sobrenome, telefone, cpf, rg, email, dtnascimento, gen['opcao'], estcivil['opcao'], codfuncionario))
            db.commit()
            input("Press Enter to continue...")

        if ed['opcao'] == 'Endereço':
            idendereco = input("Insira o ID do Endereço: ")
            cursor.execute("SELECT * FROM endereco WHERE idendereco = %s;", (idendereco,))
            result = cursor.fetchall()
            if result == []:
                print('ID do Endereço não Existe')
                input("Press Enter to continue...")
                continue
            else:
                print(tabulate(result, tablefmt='outline', showindex='always', headers=['idendereco','bairro','rua','numero','complemento','uf','cidade']))
            
            bairro = input("Bairro: ")
            rua = input("Rua: ")
            numero = input("Número: ")
            complemento = input("Complemento: ")
            if len(complemento) == 0:
                complemento = None
            uf = input("UF: ")
            cidade = input("Cidade: ")

            cursor.execute("UPDATE endereco SET bairro = %s, rua = %s, numero = %s, complemento = %s, uf = %s, cidade = %s WHERE idendereco = %s;", (bairro, rua, numero, complemento, uf, cidade, idendereco))
            db.commit()
            input("Press Enter to continue...")

        if ed['opcao'] == 'Serviço':
            codservico = input("Insira o Codigo do Serviço: ")
            cursor.execute("SELECT * FROM servico WHERE codservico = %s;", (codservico,))
            result = cursor.fetchall()
            if result == []:
                print('Codigo do Serviço não Existe')
                input("Press Enter to continue...")
                continue
            else:
                print(tabulate(result, tablefmt='outline', showindex='always', headers=['codservico','tiposervico','preco','tempomedio']))

            tiposervico = input("Tipo de Serviço: ")
            preco = int(input("Preço: "))
            tempomedio = int(input("Tempo Médio do Serviço: "))
            cursor.execute("UPDATE servico SET tiposervico = %s, preco  = %s, tempomedio  = %s WHERE codservico = %s;", (tiposervico, preco, tempomedio, codservico))
            db.commit()
            input("Press Enter to continue...")

        if ed['opcao'] == 'Agendamento':
            codagendamento = str(input("Insira o Codigo do Agendamento: "))
            
            cursor.execute("SELECT * FROM agendamento WHERE codagendamento = %s AND situacao = 'agendado';", (codagendamento,))
            result = cursor.fetchall()
            if result == []:
                print('Codigo do Serviço não Existe ou a Situação não está mais como Agendado')
                input("Press Enter to continue...")
                continue
            else:
                print(tabulate(result, tablefmt='outline', showindex='always', headers=['codagendamento','dataagendamento','hora','situacao','codfuncionario','codcliente','codservico']))

            op = operacaoAgendamento()
            if op['opcao'] == 'Mudar a Situação':
                sit = situacaoAgendamento()
                if sit['opcao'] == 'Cancelado':
                    cursor.execute("UPDATE agendamento SET situacao = 'cancelado' WHERE codagendamento = %s;", (codagendamento,))
                    db.commit()
                    input("Press Enter to continue...")
                else:
                    cursor.execute("UPDATE agendamento SET situacao = 'finalizado' WHERE codagendamento = %s;", (codagendamento,))
                    db.commit()
                    input("Press Enter to continue...")
            if op['opcao'] == 'Mudar os Dados de Agendamentos':
                dataagendamento = input("Informe a Data do Agendamento: ")
                cursor.execute("SELECT a.hora, (a.hora + interval '1 minutes' * b.tempomedio), a.codfuncionario FROM agendamento a JOIN servico b ON a.codservico = b.codservico AND a.dataagendamento = %s AND a.situacao = 'agendado' ORDER BY a.hora", (dataagendamento,))
                horadata = cursor.fetchall()
                if horadata == []:
                    print('Não existe nenhum agendamento para esta Data')
                else:
                    print("Tabela das horas agendadas nessa data: ")
                    print(tabulate(horadata, tablefmt='outline', showindex='always', headers=['Hora Inicio','Hora Fim', 'Cod. Funcionario']))

                hora = input("Informe a Hora: ")
                codfuncionario = input("Informe o Codigo do Funcionario: ")
                codcliente = input("Informe o Codigo do Cliente: ")
                codservico = input("Informe o Codigo do servico: ")
                

                cursor.execute("SELECT tempomedio FROM servico WHERE codservico = %s;", (codservico,))
                result = cursor.fetchone()
                interval = str(result[0]) + ' minutes'
                cursor.execute("SELECT time %s + interval %s;", (hora,interval,))
                horafim = cursor.fetchone()
                
                if horadata == []:
                    confirma = confirmarAgendamento()
                    if confirma['opcao'] == 'Sim':
                        cursor.execute("UPDATE agendamento SET dataagendamento = %s, hora = %s, codfuncionario = %s, codcliente = %s, codservico = %s WHERE codagendamento = %s;", (dataagendamento, hora, codfuncionario, codcliente, codservico, codagendamento))
                        db.commit()
                else:
                    cursor.execute("SELECT COUNT(*) FROM agendamento a JOIN servico s on s.codservico = a.codservico WHERE a.dataagendamento = %s AND ((%s >= a.hora AND %s < (a.hora + (s.tempomedio || ' minutes')::interval)) OR (%s > a.hora AND %s <= (a.hora + (s.tempomedio || ' minutes')::interval)) OR (%s < a.hora AND %s > (a.hora + (s.tempomedio || ' minutes')::interval))) AND a.codfuncionario = %s AND a.situacao = 'agendado';", (dataagendamento,hora,hora,horafim,horafim,hora,horafim,codfuncionario))
                    result = cursor.fetchone()  
                    if result[0] >= 1:
                        print("Existe conflito no agendamento, selecione outro horario!")
                    else:
                        cursor.execute("UPDATE agendamento SET dataagendamento = %s, hora = %s, codfuncionario = %s, codcliente = %s, codservico = %s WHERE codagendamento = %s;", (dataagendamento, hora, codfuncionario, codcliente, codservico, codagendamento))
                        db.commit()
                input("Press Enter to continue...")

        if ed['opcao'] == 'Voltar':
            continue
# -----------------------------RELATORIOS------------------------------------------
    if res['opcao'] == 'Relatórios':
        rel = menuRelatorios()
        
        if rel['opcao'] == 'Total Ganho por Funcionário':
            cursor.execute("SELECT f.codfuncionario, f.nome, f.sobrenome, COUNT(a.codagendamento) AS quantidade, SUM(s.preco) AS total FROM agendamento a JOIN funcionario f ON a.codfuncionario = f.codfuncionario JOIN servico s ON a.codservico = s.codservico AND a.situacao = 'finalizado' GROUP BY f.codfuncionario ORDER BY total DESC")
            result = cursor.fetchall()
            if result == []:
                print('Tabela Vazia')
            else:
                print(tabulate(result, tablefmt='outline', showindex='always', headers=['codfuncionario','nome','sobrenome','quantidade','total']))
            input("Press Enter to continue...")

        if rel['opcao'] == 'Quantidade de Cancelamentos por Cliente':
            cursor.execute("SELECT c.codcliente, c.nome, c.sobrenome, e.bairro, SUM(s.preco) AS total, COUNT(a.codagendamento) AS quantidade FROM cliente c LEFT JOIN endereco e ON e.idendereco = c.idendereco JOIN agendamento a ON c.codcliente = a.codcliente JOIN servico s ON s.codservico = a.codservico AND a.situacao = 'cancelado' GROUP BY c.codcliente, e.bairro ORDER BY quantidade DESC, c.codcliente")
            result = cursor.fetchall()
            if result == []:
                print('Tabela Vazia')
            else:
                print(tabulate(result, tablefmt='outline', showindex='always', headers=['codcliente','nome','sobrenome','bairro','total','quantidade']))
            input("Press Enter to continue...")

        if rel['opcao'] == 'Futuros Ganhos por Funcionário':
            cursor.execute("SELECT f.codfuncionario, f.nome, f.sobrenome, COUNT(a.codagendamento) AS quantidade, SUM(s.preco) AS total FROM agendamento a JOIN funcionario f ON a.codfuncionario = f.codfuncionario JOIN servico s ON a.codservico = s.codservico AND a.situacao = 'agendado' GROUP BY f.codfuncionario ORDER BY total DESC")
            result = cursor.fetchall()
            if result == []:
                print('Tabela Vazia')
            else:
                print(tabulate(result, tablefmt='outline', showindex='always', headers=['codfuncionario','nome','sobrenome','quantidade','total']))
            input("Press Enter to continue...")
# -----------------------------------------------------------------------       
    if res['opcao'] == 'Sair':
        db.close()
        break