from flask import Flask, g
import sqlite3


DATABASE = "blog.db"
SECRET_KEY = "pave"

app = Flask(__name__) # variavel que pega o nome do arquivo app.py
app.config.from_object(__name__) # pega a vonfig do proprio arquivo

def conectar_db():
    return sqlite3.connect(DATABASE)

@app.before_request # antes de cada requisição, conecta com banco
def antes_requisicao():
    g.db = conectar_db()

@app.teardown_request # ao fim de cada requisição, fecha o banco
def fim_requisicao(exc):
    g.db.close()

@app.route('/')
def exibir_entradas():
    sql = "SELECT titulo, texto FROM entradas ORDER BY id DESC"
    cur = g.db.execute(sql)
    entradas = []
    return str(entradas)
