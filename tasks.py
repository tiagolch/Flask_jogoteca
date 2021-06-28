
from flask import Flask, render_template, request, redirect, session, flash, url_for


app = Flask(__name__)
app.secret_key='tiagochaves'


class User:
    def __init__(self, id, nome, senha):
        self.id = id
        self.nome = nome
        self.senha = senha


tiago = User('admin', 'Tiago Chaves', 'admin')
usuarios = {
    tiago.id: tiago
}


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


@app.route('/autenticar', methods=['POST',])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if usuario.senha == request.form['senha']:
            session['usuario_logado'] = usuario.id
            flash(usuario.nome + 'logou com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
        else:
            flash('Não logado, tente de novo!')
            return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Deslogado com sucesso.')
    return redirect(url_for('index'))


@app.route('/')
def index():
    return render_template('index.html', titulo='Pagina Principal', nome='Tiago Chaves')


app.run(debug=True)
