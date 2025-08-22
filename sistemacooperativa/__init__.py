from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
import sqlalchemy
import locale
from datetime import datetime
from flask_migrate import Migrate



# ----- Configura formatação de moeda e data para o Brasil -----
try:
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
except locale.Error:
    locale.setlocale(locale.LC_ALL, '')  # Usa locale padrão do sistema se o pt_BR não existir

# ----- Funções de formatação -----
def format_currency(value):
    try:
        return f"R$ {float(value):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    except:
        return value

def format_date(value):
    if isinstance(value, datetime):
        return value.strftime('%d/%m/%Y')
    try:
        return datetime.strptime(str(value), "%Y-%m-%d").strftime('%d/%m/%Y')
    except:
        return value

# ----- Configuração do Flask -----
app = Flask(__name__)
app.config['SECRET_KEY'] = 'e14fbbd6f299c6454f3094c9db985177'

# ----- Configuração do banco de dados -----
if os.getenv("DATABASE_URL"):
    uri = os.getenv("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config['SQLALCHEMY_DATABASE_URI'] = uri
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cooperativa.db'

# ----- Inicializa extensões -----
database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert-info'

# Flask-Migrate
migrate = Migrate(app, database)

# ----- Registra filtros no Jinja -----
app.jinja_env.filters['currency'] = format_currency
app.jinja_env.filters['brdate'] = format_date

# ----- Importa models e rotas -----
from sistemacooperativa import models
from sistemacooperativa import routes

# ----- Verifica e cria tabelas se não existirem -----
engine = sqlalchemy.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
inspector = sqlalchemy.inspect(engine)

if not inspector.has_table("usuario"):
    with app.app_context():
        database.create_all()
        print("Base de dados criada")
else:
    print("Base de dados já existente")

