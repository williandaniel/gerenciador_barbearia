import re

import inquirer


def menuPrincipal():
    principal = [
        inquirer.List('opcao',
                        message="Escolha a opção desejada",
                        choices=['Exibir', 'Adicionar', 'Remover', 'Editar', 'Relatórios', 'Sair'],
                    ),
    ]
    answers = inquirer.prompt(principal)
    return answers

def menuExibir():
        exibir = [
                inquirer.List('opcao',
                                message="Escolha uma tabela para Visualizar",
                                choices=['Clientes', 'Funcionarios', 'Endereço', 'Serviços', 'Agendamentos', 'Voltar'],
                            ),
            ]
        answers = inquirer.prompt(exibir)
        return answers

def menuAdicionar():
        adicionar = [
                inquirer.List('opcao',
                                message="Escolha uma opção para Adicionar",
                                choices=['Clientes', 'Funcionarios', 'Serviços', 'Agendamentos', 'Voltar'],
                            ),
            ]
        answers = inquirer.prompt(adicionar)
        return answers

def menuRemover():
        remover = [
                inquirer.List('opcao',
                                message="Qual deseja Remover",
                                choices=['Cliente', 'Funcionario', 'Endereço', 'Serviço', 'Agendamento', 'Voltar'],
                            ),
            ]
        answers = inquirer.prompt(remover)
        return answers

def menuEditar():
        editar = [
                inquirer.List('opcao',
                                message="Qual deseja Editar",
                                choices=['Cliente', 'Funcionario', 'Endereço', 'Serviço', 'Agendamento', 'Voltar'],
                            ),
            ]
        answers = inquirer.prompt(editar)
        return answers

def menuRelatorios():
        relatorio = [
                inquirer.List('opcao',
                                message="Qual relatorio deseja Exibir",
                                choices=['Total Ganho por Funcionário', 'Quantidade de Cancelamentos por Cliente', 'Futuros Ganhos por Funcionário', 'Voltar'],
                            ),
            ]
        answers = inquirer.prompt(relatorio)
        return answers

def generoC():
        genero = [
                inquirer.List('opcao',
                                message="Genero Cliente",
                                choices=['Não Informar','Marculino', 'Feminino'],
                            ),
            ]
        answers = inquirer.prompt(genero)
        return answers


def generoF():
        genero = [
                inquirer.List('opcao',
                                message="Genero Funcionario",
                                choices=['Marculino', 'Feminino'],
                            ),
            ]
        answers = inquirer.prompt(genero)
        return answers

def estadocivil():
        estadoc = [
                inquirer.List('opcao',
                                message="Estado Civil",
                                choices=['Solteiro', 'Casado','Separado','Divorciado','Viúvo'],
                            ),
            ]
        answers = inquirer.prompt(estadoc)
        return answers

def editarEnderecoNull():
        edend = [
                inquirer.List('opcao',
                                message="Escolha uma opção",
                                choices=['Manter Null','Cadastrar Endereço'],
                            ),
            ]
        answers = inquirer.prompt(edend)
        return answers

def confirmarRemocao():
        remove = [
                inquirer.List('opcao',
                                message="Deseja realmente Remover?",
                                choices=['Sim','Não'],
                            ),
            ]
        answers = inquirer.prompt(remove)
        return answers

def confirmarAgendamento():
        confirma = [
                inquirer.List('opcao',
                                message="Deseja realmente Agendar?",
                                choices=['Sim','Não'],
                            ),
            ]
        answers = inquirer.prompt(confirma)
        return answers

def operacaoAgendamento():
        confirma = [
                inquirer.List('opcao',
                                message="Qual operação deseja executar?",
                                choices=['Mudar a Situação','Mudar os Dados de Agendamentos'],
                            ),
            ]
        answers = inquirer.prompt(confirma)
        return answers

def situacaoAgendamento():
        confirma = [
                inquirer.List('opcao',
                                message="Para qual Situação do Agendamento deseja mudar?",
                                choices=['Cancelado','Finalizado'],
                            ),
            ]
        answers = inquirer.prompt(confirma)
        return answers

def confirmar():
    conf = [
        inquirer.Confirm("opcao", message="Deseja realizar essa ação?"),
    ]
    answers = inquirer.prompt(conf)
    return answers

def endereco():
    end = [
        inquirer.Confirm("opcao", message="Deseja adicionar um endereço?"),
    ]
    answers = inquirer.prompt(end)
    return answers
