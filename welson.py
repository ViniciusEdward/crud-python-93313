import os
os.system("cls || clear")
from sqlalchemy import create_engine, Column, String, Integer, Float
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando banco de dados
MEU_BANCO = create_engine("sqlite:///meubanco.db")

# Criando conexão com banco de dados.
Session = sessionmaker(bind=MEU_BANCO)
session = Session()

# Criando tabela.
Base = declarative_base()

class Empresa(Base):
    __tablename__ = "usuarios"

    # Definindo campos da tabela.
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    idade = Column("Idade", Integer)
    cpf = Column("CPF", String)
    setor= Column("Setor", String)
    funcao= Column("Função", String)
    salario= Column("Salario", Integer)
    telefone= Column("Telefone", String)
    # Definindo atributos da classe.
    def __init__(self, nome: str, idade:int,cpf:str, setor:str, 
                 funcao:str, salario:float, telefone:str):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.setor = setor
        self.funcao = funcao
        self.salario = salario
        self.telefone = telefone
        
# Criando tabela no banco de dados.
Base.metadata.create_all(bind=MEU_BANCO)

#limpa tela
os.system("cls || clear")

# Listando todos os usuários do banco de dados.
print("\nExibindo todos os usuários do banco de dados.")
lista_empresa = session.query(Empresa).all()

# Lendo a lista
for bens in lista_empresa:
    print(f"{bens.id} - Nome: {bens.nome} - Idade: {bens.idade} - CPF: {bens.cpf} -Setor: {bens.setor} -Função: {bens.funcao} -Salario: {bens.salario} -Telefone: {bens.telefone}")

#limpa tela
os.system("cls || clear")

# Listando todos os usuários do banco de dados.
print("\nExibindo todos os usuários do banco de dados.")
lista_empresa = session.query(Empresa).all()

# lendo a lista
for bens in lista_empresa:
        print(f"{bens.id} - Nome: {bens.nome} - Idade: {bens.idade} - CPF: {bens.cpf} -Setor: {bens.setor} -Função: {bens.funcao} -Salario: {bens.salario} -Telefone: {bens.telefone}")

# atualizando os dados da empresa
print("\nAtualizando dados da empresa.")
bens_capitais = session.query(Empresa).filter_by(cpf=cpf_paixao).first()

print("""
=== RH System ===
1- Adicionar funcionario
2- Consultar um funcionario
3- Atualizar os dados de um funcionario
4- Excluir um funcionario
5- Listar todos os funcionarios
0- Sair do sistema
      """)

opcao=int(input("Digite um numero correspondente a sua opção"))
match(opcao):
    case 1:
        # Salvar no banco de dados.
        print("---Solicitando dados para o usuário---")
        insirir_nome = input("Digite seu nome: ")
        insirir_idade = int(input("Digite sua idade: "))
        insirir_cpf = input("Digite seu CPF: ")
        insirir_setor = input("Digite seu Setor: ")
        insirir_funcao = input("Digite sua Função: ")
        insirir_salario = float(input("Digite seu Salario: "))
        insirir_telefone = input("Digite seu telefone: ")

        bens_capitais = Empresa(nome=insirir_nome, idade=insirir_idade, cpf=insirir_cpf, 
                  setor=insirir_setor, funcao=insirir_funcao, salario=insirir_salario,
                  telefone=insirir_telefone)
        session.add(bens_capitais)
        session.commit()
    case 2:
        # Listando todos os usuários do banco de dados.
        print("\nConsultando  os dados de um funcionario.")
        cpf_funcionario=input("Digite o CPF do funcionario:")
        lista_empresa = session.query(Empresa).all(cpf_funcionario)
    case 3:
        # atualizando os dados da empresa
        print("\nAtualizando dados da empresa.")
        bens_capitais = session.query(Empresa).filter_by(cpf=cpf_paixao).first()

        novos_dados = Empresa(
            nome = input("Digite seu nome: "),
            idade= int(input("Digite sua Idade: ")),
            cpf = input("Digite seu CPF: "),
            setor= input("Digite seu Setor:"),
            funcao= input("Digite sua função:"),
            salario= float(input("Digite seu Salario")),
            telefone= input("Digite seu telfone")   
        )
        bens_capitais = novos_dados
        session.add(bens_capitais)
        session.commit()

        # Fechando conexão.    
        session.close()
    case 4:
        # Apagar o excesso
        print("\nApagando a preguiça.")
        cpf_paixao = input("Informe o CPF do trabalhador, para o clthanos fazer o trabalho: ")

        # Otmizando os dados da empresa 
        print("\nAtualizando dados da empresa.")
        bens_capitais = session.query(bens_capitais).filter_by(cpf = cpf_paixao).first()
        session.delete(bens_capitais)
        session.commit()

        print(f"{bens_capitais.nome} excluído com sucesso.")