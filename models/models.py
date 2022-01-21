from extensions import db


#  Para criar via cmd: acessar python, após from app import db, após db.create_all()
class Funcionarios(db.Model):
    __tagle_args__ = {'extend_existing': True}
    __tablename__ = 'funcionarios'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    celular = db.Column(db.String(20), nullable=False)

    # def __init__(self, nome, email, celular):
    #     self.nome = nome
    #     self.email = email
    #     self.celular = celular
