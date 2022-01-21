from flask import Flask, render_template, request, redirect, url_for, flash
from extensions import db, migrate
from models.models import Funcionarios


def build_app():
    app = Flask('__name__')
    app.config.from_object('extensions.config.LocalConfig')

    db.app = app
    db.init_app(app)

    migrate.init_app(app, db)

    return app

app = build_app()


@app.route('/')
def index():
    funcionarios = db.session.query(Funcionarios).all()
    # funcionarios = Funcionarios.query.all() / Modo como o maluco do vídeo fez

    return render_template('index.html', funcionarios=funcionarios)


@app.route('/cadastrar', methods=['POST'])
def cadastrar_funcionario():
    if request.method == 'POST':
        funcionarios = Funcionarios()

        funcionarios.nome = request.form['nome']
        funcionarios.email = request.form['email']
        funcionarios.celular = request.form['celular']

        db.session.add(funcionarios)
        db.session.commit()

        flash(f'Funcionário {funcionarios.nome} cadastrado com sucesso!')

        return redirect(url_for('index'))


@app.route('/editar', methods=['GET', 'POST'])
def editar():
    if request.method == 'POST':
        funcionario = Funcionarios.query.get(request.form.get('id'))

        funcionario.nome = request.form['nome']
        funcionario.email = request.form['email']
        funcionario.celular = request.form['celular']

        db.session.commit()

        flash(f'Funcionário {funcionario.nome} atualizado com sucesso!')

        return redirect(url_for('index'))


@app.route('/deletar/<id>', methods=['GET', 'POST'])
def deletar(id):
    # funcionario = Funcionarios.query.get(id)
    funcionario = db.session.query(Funcionarios).filter_by(id=id).first()

    db.session.delete(funcionario)
    db.session.commit()

    flash(f'Funcionário {funcionario.nome} deletado com sucesso!')

    return redirect(url_for('index'))


if __name__ == "__main__":
    db.create_all()
    db.session.commit()
    app.run(debug=True)