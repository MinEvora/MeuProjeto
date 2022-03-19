from flask import Flask, render_template

app = Flask("__name__", template_folder="src/templates", static_folder="src/static")


@app.route('/')
@ app . route ( "/home" )
def home():
    return render_template("home.html")

@app.route('/estudos')
def estudos():
    return render_template("estudos.html")

@app.route('/projetos')
def projetos():
    return render_template("projetos.html")

    
if __name__ == "__main__":
 app.run()
 