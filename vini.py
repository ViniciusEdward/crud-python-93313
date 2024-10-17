import os
from sqlalchemy import create_engine, Column, String, Integer 
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando banco de dados
FUNCIONARIO = create_engine("sqlite:///funcionario.db")

# Criando conexão com banco de dados.
Session = sessionmaker(bind=FUNCIONARIO)
session = Session()

# Criando tabela.
Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    # Definindo campos da tabela.
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("Nome", String)
    idade = Column("Idade", String)
    cpf = Column("CPF", String)
    setor = Column("Setor", String)
    funcao = Column("Função", String)
    salario = Column("Salário", String)
    telefone = Column("Telefone", String)

    # Definindo atributos da classe.
    def __init__(self, nome: str, idade:str, cpf:str, setor:str, funcao:str, salario:str, telefone:str):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.setor = setor
        self.funcao = funcao
        self.salario = salario 
        self.telefone = telefone 

# Criando tabela no banco de dados.
Base.metadata.create_all(bind=FUNCIONARIO)

# Salvar no banco de dados.
os.system("cls || clear")
def exibindo_funcionario():
    lista_funcionarios = session.query(Usuario).all()

    for funcionario in lista_funcionarios:
        print(f"{funcionario.id} - Nome: {funcionario.nome} - Idade: {funcionario.idade} - CPF: {funcionario.cpf} - Setor: {funcionario.setor} - Função: {funcionario.funcao} - Salário: {funcionario.salario} - Telefone: {funcionario.telefone}")

print("""
    === RH SYSTEM ===
1 - Adicionar funcionário
2 - Consultar funcionário
3 - Atualizar dados de um funcionário
4 - Excluir um funcionário
5 - Listar todos os funcionários
0 - Sair do sistema
      """)

opcao = input("Digite o que deseja: ")
while True:
    match(opcao):
        case '1':
            print("Solicitando dados para o funcionário")
            insirir_nome = input("Digite seu nome: ")
            inserir_idade = input("Digite sua idade: ")
            inserir_cpf = input("Digite seu cpf: ")
            inserir_setor = input("Digite o setor do seu trabalho: ")
            inserir_funcao = input("Digite sua função na empresa: ")
            inserir_salario = input("Digite seu salário: ")
            inserir_telefone = input("Digite seu telefone: ")

            funcionario = Usuario(nome=insirir_nome, idade=inserir_idade, cpf= inserir_cpf, setor= inserir_setor, funcao= inserir_funcao, salario= inserir_salario, telefone= inserir_telefone)
            session.add(funcionario)
            session.commit()

        case '2':
            print("\nExibindo o usuário desejado")
            exibindo_funcionario()

        case '3':
            print("\nAtualizando dados do usuário.")
            funcionario = session.query(Usuario).filter_by(cpf = cpf_usuario).first()

            novos_dados = Usuario(
                nome = input("Digite seu nome: "),
                idade= input("Digite sua idade: "),
                cpf = input("Digite seu CPF: "),
                setor = input("Digite seu setor: "),
                funcao = input("Digite sua função: "),
                salario = input("Digite seu salário: "),
                telefone = input("Digite seu telefone: ")
            )

            funcionario = novos_dados
            session.add(funcionario)
            session.commit()

        case '4':
            print("\nExcluindo um usuário.")
            cpf_usuario = input("Digite o cpf do usuário para ser excluído: ")

            funcionario = session.query(Usuario).filter_by(cpf = cpf_usuario).first()
            session.delete(funcionario)
            session.commit()

            os.system("cls || clear")
            print(f"{funcionario.nome} excluído com sucesso.")

        case '5':
            print("\nExibindo todos os usuários do banco de dados.")
            lista_funcionarios = session.query(Usuario).all()

            for funcionario in lista_funcionarios:
                print(f"{funcionario.id} - Nome: {funcionario.nome} - Idade: {funcionario.idade} - CPF: {funcionario.cpf} - Setor: {funcionario.setor} - Função: {funcionario.funcao} - Salário: {funcionario.salario} - Telefone: {funcionario.telefone}")
        case _:
            print("\nSaindo do sistema")
            break

