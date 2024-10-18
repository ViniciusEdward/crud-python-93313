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
def rh_system():
    print("""
    === RH SYSTEM ===
1 - Adicionar funcionário
2 - Consultar funcionário
3 - Atualizar dados de um funcionário
4 - Excluir um funcionário
5 - Listar todos os funcionários
0 - Sair do sistema
      """)

def exibindo_funcionario(funcionario):
    print(f"{funcionario.id} - Nome: {funcionario.nome} - Idade: {funcionario.idade} - CPF: {funcionario.cpf} - Setor: {funcionario.setor} - Função: {funcionario.funcao} - Salário: {funcionario.salario} - Telefone: {funcionario.telefone}")

def adicionar_funcionario(session):
    print("\nSolicitando dados para o funcionário")
    funcionario = Usuario(
        nome=input("\nDigite seu nome: "),
        idade=input("Digite sua idade: "),
        cpf=input("Digite seu cpf: "),
        setor=input("Digite o setor do seu trabalho: "),
        funcao=input("Digite sua função na empresa: "),
        salario=input("Digite seu salário: "),
        telefone=input("Digite seu telefone: ")
    )
    session.add(funcionario)
    session.commit()

def consultar_funcionario(session):
    cpf_usuario = input("\nDigite o cpf do usuário desejado: ")
    funcionario = session.query(Usuario).filter_by(cpf=cpf_usuario).first()
    if funcionario:
        exibindo_funcionario(funcionario)
    else:
        print("Funcionário não encontrado.")

def atualizar_funcionario(session):
    cpf_usuario = input("\nDigite o cpf do usuário para atualizar: ")
    funcionario = session.query(Usuario).filter_by(cpf=cpf_usuario).first()
    if funcionario:
        funcionario.nome = input("Digite seu nome: ")
        funcionario.idade = input("Digite sua idade: ")
        funcionario.cpf = input("Digite seu CPF: ")
        funcionario.setor = input("Digite seu setor: ")
        funcionario.funcao = input("Digite sua função: ")
        funcionario.salario = input("Digite seu salário: ")
        funcionario.telefone = input("Digite seu telefone: ")
        session.commit()
        print("Dados atualizados com sucesso.")
    else:
        print("Funcionário não encontrado.")

def excluir_funcionario(session):
    cpf_usuario = input("\nDigite o cpf do usuário para ser excluído: ")
    funcionario = session.query(Usuario).filter_by(cpf=cpf_usuario).first()
    if funcionario:
        session.delete(funcionario)
        session.commit()
        print(f"{funcionario.nome} excluído com sucesso.")
    else:
        print("Funcionário não encontrado.")

def listar_funcionarios(session):
    print("\nExibindo todos os usuários do banco de dados.")
    lista_funcionarios = session.query(Usuario).all()
    for funcionario in lista_funcionarios:
        exibindo_funcionario(funcionario)

rh_system()

while True:
    opcao = input("\nDigite o que deseja: ")
    match(opcao):
        case '1':
            adicionar_funcionario(session)

        case '2':
            exibindo_funcionario(session)

        case '3':
            atualizar_funcionario(session)

        case '4':
            excluir_funcionario(session)

        case '5':
            listar_funcionarios(session)

        case _:
            print("Saindo do sistema")
            break

