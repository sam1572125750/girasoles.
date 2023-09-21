from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejecutar/<script_nombre>')
def ejecutar_script(script_nombre):
    try:
        # Verifica si el nombre del script es "flor.py" o "girasol.py"
        if script_nombre == 'flor.py' or script_nombre == 'girasol.py':
            # Ejecuta el script especificado
            resultado = subprocess.check_output(['python', script_nombre], universal_newlines=True)
            return resultado
        else:
            return "Script no válido"
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
