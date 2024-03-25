from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_quiz', methods=['POST'])
def submit_quiz():
    resposta1 = request.form['pergunta1']
    #resposta2 = request.form['pergunta2']
    #resposta3 = request.form['pergunta3']
    #resposta4 = request.form['pergunta4']
    #resposta5 = request.form['pergunta5']
    #resposta6 = request.form['pergunta6']
    #resposta7 = request.form['pergunta7']
    #resposta8 = request.form['pergunta8']
    #resposta9 = request.form['pergunta9']
    #resposta10 = request.form['pergunta10']
    #resposta11 = request.form['pergunta11']
    #resposta12 = request.form['pergunta12']
    #resposta13 = request.form['pergunta13']
    #resposta14 = request.form['pergunta14']
    #resposta15 = request.form['pergunta15']
    #resposta16 = request.form['pergunta16']
    #resposta17 = request.form['pergunta17']
    #resposta18 = request.form['pergunta18']
    #resposta19 = request.form['pergunt19']
    #resposta20 = request.form['pergunta20']

    #resultado = determinar_animal(resposta1, resposta2, resposta3, resposta4, resposta5, resposta6, resposta7, resposta8, resposta9, resposta10, resposta11, resposta12, resposta13, resposta14, resposta15, resposta16, resposta17, resposta18, resposta19, resposta20)

    resultado = determinar_animal(resposta1)
    return render_template('resultado.html', animal=resultado)

def calcular_animal():
    contador = 0
    for resposta in resultado:
        if resposta == 'carnivoro':
            contador += 1
    print(contador)
def determinar_animal(resposta1):
     #def   determinar_animal(resposta1, resposta2, resposta3, resposta4, resposta5, resposta6, resposta7, resposta8, resposta9, resposta10, resposta11, resposta12, resposta13, resposta14, resposta15, resposta16, resposta17, resposta18, resposta19, resposta20):
    if resposta1 == 'carnivoro':
        return 'Gato'

if __name__ == '__main__':
    app.run(debug=True)
