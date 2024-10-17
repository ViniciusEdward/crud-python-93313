import os
from sqlalchemy import create_engine, Column, String, Integer, Float
from sqlalchemy.orm import sessionmaker, declarative_base

# Limpa a tela
os.system("cls || clear")

# Criando banco de dados
MEU_BANCO = create_engine("sqlite:///meubanco.db")

# Criando conexão com o banco de dados
Session = sessionmaker(bind=MEU_BANCO)
session = Session()

# Criando tabela
Base = declarative_base()

class Empresa(Base):
    __tablename__ = "Empresa"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    idade = Column("Idade", Integer)
    cpf = Column("CPF", String)
    setor = Column("Setor", String)
    funcao = Column("Função", String)
    salario = Column("Salario", Float)  
    telefone = Column("Telefone", String)

    def __init__(self, nome: str, idade: int, cpf: str, setor: str, 
                 funcao: str, salario: float, telefone: str):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.setor = setor
        self.funcao = funcao
        self.salario = salario
        self.telefone = telefone

# Criando tabela no banco de dados
Base.metadata.create_all(bind=MEU_BANCO)

# Listando todos os usuários do banco de dados
print("\nExibindo todos os usuários do banco de dados.")
lista_empresa = session.query(Empresa).all()
for bens in lista_empresa:
    print(f"{bens.id} - Nome: {bens.nome} - Idade: {bens.idade} - CPF: {bens.cpf} - Setor: {bens.setor} - Função: {bens.funcao} - Salário: {bens.salario} - Telefone: {bens.telefone}")

# Menu de opções
while True:
    print("""
    === RH System ===
    1- Adicionar funcionário
    2- Consultar um funcionário
    3- Atualizar os dados de um funcionário
    4- Excluir um funcionário
    5- Listar todos os funcionários
    0- Sair do sistema
    """)
    
    opcao = int(input("Digite um número correspondente à sua opção: "))
    
    match(opcao):
        case 1:
            # Adicionar funcionário
            print("--- Solicitando dados para o usuário ---")
            insirir_nome = input("Digite seu nome: ")
            insirir_idade = int(input("Digite sua idade: "))
            insirir_cpf = input("Digite seu CPF: ")
            insirir_setor = input("Digite seu Setor: ")
            insirir_funcao = input("Digite sua Função: ")
            insirir_salario = float(input("Digite seu Salário: "))
            insirir_telefone = input("Digite seu telefone: ")

            novo_funcionario = Empresa(
                nome=insirir_nome,
                idade=insirir_idade,
                cpf=insirir_cpf,
                setor=insirir_setor,
                funcao=insirir_funcao,
                salario=insirir_salario,
                telefone=insirir_telefone
            )
            session.add(novo_funcionario)
            session.commit()
            print("Funcionário adicionado com sucesso.")

        case 2:
            # Consultar funcionário
            print("\nConsultando os dados de um funcionário.")
            cpf_funcionario = input("Digite o CPF do funcionário: ")
            funcionario = session.query(Empresa).filter_by(cpf=cpf_funcionario).first()
            if funcionario:
                print(f"{funcionario.id} - Nome: {funcionario.nome} - Idade: {funcionario.idade} - CPF: {funcionario.cpf} - Setor: {funcionario.setor} - Função: {funcionario.funcao} - Salário: {funcionario.salario} - Telefone: {funcionario.telefone}")
            else:
                print("Funcionário não encontrado.")

        case 3:
            # Atualizar dados do funcionário
            print("\nAtualizando dados do funcionário.")
            cpf_paixao = input("Digite o CPF do funcionário: ")
            funcionario = session.query(Empresa).filter_by(cpf=cpf_paixao).first()
            if funcionario:
                funcionario.nome = input("Digite seu nome: ")
                funcionario.idade = int(input("Digite sua Idade: "))
                funcionario.cpf = input("Digite seu CPF: ")
                funcionario.setor = input("Digite seu Setor: ")
                funcionario.funcao = input("Digite sua função: ")
                funcionario.salario = float(input("Digite seu Salário: "))
                funcionario.telefone = input("Digite seu telefone: ")
                
                session.commit()
                print("Dados atualizados com sucesso.")
            else:
                print("Funcionário não encontrado.")

        case 4:
            # Excluir funcionário
            print("\nExcluindo um funcionário.")
            cpf_paixao = input("Informe o CPF do funcionário para exclusão: ")
            funcionario = session.query(Empresa).filter_by(cpf=cpf_paixao).first()
            if funcionario:
                session.delete(funcionario)
                session.commit()
                print(f"{funcionario.nome} excluído com sucesso.")
            else:
                print("Funcionário não encontrado.")

        case 5:
            # Listar todos os funcionários
            print("\nExibindo todos os usuários do banco de dados.")
            lista_empresa = session.query(Empresa).all()
            for bens in lista_empresa:
                print(f"{bens.id} - Nome: {bens.nome} - Idade: {bens.idade} - CPF: {bens.cpf} - Setor: {bens.setor} - Função: {bens.funcao} - Salário: {bens.salario} - Telefone: {bens.telefone}")

        case 0:
            # Sair do sistema
            print("Saindo do sistema...")
            session.close()
            exit()

        case _:
            print("Opção inválida. Tente novamente.")
