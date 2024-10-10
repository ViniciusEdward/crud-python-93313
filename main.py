import os
from sqlalchemy import create_engine, Column, String, Integer 
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando banco de dados
MEU_BANCO = create_engine("sqlite:///meubanco.db")

# Criando conexão com banco de dados.
Session = sessionmaker(bind=MEU_BANCO)
session = Session()


# Criando tabela.
Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    # Definindo campos da tabela.
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("emai", String)
    senha = Column("senha", String)

    # Definindo atributos da classe.
    def __init__(self, nome: str, email:str, senha:str):
        self.nome = nome
        self.email = email
        self.senha = senha

# Criando tabela no banco de dados.
Base.metadata.create_all(bind=MEU_BANCO)

# Salvar no banco de dados.
os.system("cls || clear")

print("Solicitando dados para o usuário")
insirir_nome = input("Digite seu nome: ")
insirir_email = input("Digite seu e-mail: ")
insirir_senha = input("Digite sua senha: ")

usuario = Usuario(nome=insirir_nome, email=insirir_email, senha=insirir_senha)
session.add(usuario)
session.commit()

# Listando todos os usuários do banco de dados.
print("\nExibindo todos os usuários do banco de dados.")
lista_usuarios = session.query(Usuario).all()

# Read
for usuario in lista_usuarios:
    print(f"{usuario.id} - Nome: {usuario.nome} - Email: {usuario.email} - Senha: {usuario.senha}")

# Delete
print("\nExcluindo um usuário.")
email_usuario = input("Informe o email do usuário para ser excluído: ")

usuario = session.query(Usuario).filter_by(email = email_usuario).first()
session.delete(usuario)
session.commit()

os.system("cls || clear")
print(f"{usuario.nome} excluído com sucesso.")

# Listando todos os usuários do banco de dados.
print("\nExibindo todos os usuários do banco de dados.")
lista_usuarios = session.query(Usuario).all()

# Read
for usuario in lista_usuarios:
    print(f"{usuario.id} - Nome: {usuario.nome} - Email: {usuario.email} - Senha: {usuario.senha}")

# Update
print("\nAtualizando dados do usuário.")
usuario = session.query(Usuario).filter_by(email = email_usuario).first()

novos_dados = Usuario(
    nome = input("Digite seu nome: "),
    email= input("Digite seu e-mail: "),
    senha = input("Digite sua senha: ")
)

usuario = novos_dados
session.add(usuario)
session.commit()

# Fechando conexão.    
session.close()