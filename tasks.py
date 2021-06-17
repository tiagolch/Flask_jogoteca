
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', titulo='Pagina Principal', nome='Tiago Chaves')

if __name__ == "__main__":
    app.run()
